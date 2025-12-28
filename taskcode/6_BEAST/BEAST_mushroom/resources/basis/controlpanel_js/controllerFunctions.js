/**
 * Created by Marcus on 31.07.2016.
 */



$(document).click(function () {

});

function terminatePlayer(playerNr) {
    if (typeof playerNr !== undefined && playerNr != null && playerNr !== '') {

        return $.ajax({
            type: 'POST',
            async: true,
            url: 'controlpanel_functions/terminatePlayer.php',
            cache: false,
            data: ({
                playerNr: playerNr
            }),
            success: function (result) {

                showMessage('Player ' + playerNr + ' terminated.');

            }
        });


    } else {

    }
}

path = '';

function switchTestMode(switcher) {

    var container = $('#testmode');
    var testplayer = $('#testplayer');
    var testbot = $('#testbot');
    var testplayer_off = $('#testplayer_off');
    var testbot_off = $('#testbot_off');
    let testMode = getParameter('testMode');

    if ((testMode == 0 && switcher === true) || (testMode == 1 && switcher === false)) {
        if (switcher) setValue('globals', 'name="testMode"', 'value', 1);
        container.addClass('btn-success');
        container.html('test mode on');

        testplayer.show();
        testbot.show();
        testplayer_off.hide();
        testbot_off.hide();


    } else {
        if (switcher) setValue('globals', 'name="testMode"', 'value', 0);
        container.removeClass('btn-success');
        container.html('test mode off');
        testplayer_off.show();
        testbot_off.show();
        testplayer.hide();
        testbot.hide();
    }

}

function switchActive(switcher) {
    var container = $('#gameactive');

    active = getParameter('active');

    if ((active == 0 && switcher === true) || (active == 1 && switcher === false)) {
        if (switcher) setValue('globals', 'name="active"', 'value', 1);
        container.addClass('btn-success');
        container.html('experiment active');


    } else {
        if (switcher) setValue('globals', 'name="active"', 'value', 0);
        container.removeClass('btn-success');
        container.html('experiment inactive');

    }

}

function fileExists(url) {
    if (url) {
        var req = new XMLHttpRequest();
        req.open('GET', url, false);
        req.send();
        return req.status === 200;
    } else {
        return false;
    }
}

function getParameter(name) {


    return JSON.parse($.ajax({
        type: 'POST',
        async: false,
        url: 'ajax/getValue.php',
        data: {tableName: 'globals', condition: 'name="' + name + '"', varName: 'value'},
        success: function (data) {
            return data;
        }
    }).responseText);


}

function showMessage(message) {


    var container = $('#messages');
    var body = $("#message_body");
    body.addClass('alert alert-warning');
    body.html(message);
    container.show();
    container.delay(10000).fadeOut(800);

}

function emptyDataTables(projectID) {
    var xmlhttp;
    if (window.XMLHttpRequest) {
        xmlhttp = new XMLHttpRequest();
    } else {
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.open("POST", "controlpanel_functions/emptyDatatables.php?projectID =" + projectID);
    xmlhttp.send();
}

// define function for viewing the variables
function loadVariables(tableNameActive) {
    return JSON.parse($.ajax({
        type: 'GET',
        url: 'controlpanel_functions/loadVariables.php',
        dataType: 'json',
        data: {tableName: tableNameActive},
        global: false,
        async: false,
        success: function (data) {
            return data;
        }
    }).responseText);
}

// menu for (de)selecting variables
function loadVariables2(tableNameActive) {
    // asynchronously interacting with the database
    var xmlhttp;
    if (window.XMLHttpRequest) {
        xmlhttp = new XMLHttpRequest();
    } else {
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange = function () {
        // when we are ready, show the variables
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            // which variables does the experimenter want to see?
            var variables = JSON.parse(xmlhttp.responseText);
            for (var i = 0; i < variables.length; i++) {
                if (variables[i].substring(0, 5) === 'time_') {
                    var key1 = variables[i].substring(5);
                    var pos = stageNrs.indexOf(parseInt(key1));
                    var stageName = stageNames[pos];
                    variables[i] = 'time_' + stageName;
                }
            }
            var txt = '';

            // define the show/hide variables menu. give ids according to the order in which they appear
            txt += '<form name="tcol" onsubmit="return false"><p>Click variables to show/hide</p>';
            for (var i = 0; i < variables.length; i++) {
                txt += '<button id=' + tableNameActive + '_col' + i + ' name=' + tableNameActive + '_col' + i + ' onclick="toggleVis(this.name); loadTable()" class="btn';
                // if the variable has been selected, make it blue
                if (localStorage[tableNameActive + '_tcol' + i]) txt += ' btn-info';
                else txt += '';
                txt += '">' + variables[i] + '</button>';
                if (i < (variables.length - 1)) txt += '&nbsp&nbsp';
            }
            txt += '</form>';

            // table sorting form
            txt += '<form onsubmit="sortTable(); loadTable(); return false">';
            txt += 'Sort table by ';
            txt += '<select id="sortBy">';
            for (var i = 0; i < variables.length; i++) {
                txt += '<option value=' + i;
                if (localStorage[tableNameActive + '_orderByVar'] == variables[i]) txt += ' selected';
                txt += '>' + variables[i] + '</option>';
            }
            txt += '</select>';

            txt += '<select id="sortOrder">';
            txt += '<option value="0"';
            if (localStorage[tableNameActive + '_ascOrDesc'] == 0) txt += ' selected';
            txt += '> Ascending </option>';
            txt += '<option value="1"';
            if (localStorage[tableNameActive + '_ascOrDesc'] == 1) txt += ' selected';
            txt += '> Decending </option>';
            txt += '</select>';
            txt += '<input type="submit" value="Sort" class="btn">';
            txt += '</form>';

            //print the whole thing to the screen
            document.getElementById("varMenu").innerHTML = txt;
        }
    };
    // check which variables should be read from the database
    var reqVars = 'controlpanel_functions/loadVariables.php?tableName=' + tableNameActive;
    xmlhttp.open("GET", reqVars, true);
    xmlhttp.send();
}

// the function loading the data from the database
function loadTable() {
    // look in this table
    var tableNameActive = tables[localStorage['activeTable']];
    // these variables should be retrieved
    var tabNames = loadVariables(tableNameActive);
    var xmlhttp;
    if (window.XMLHttpRequest) {
        xmlhttp = new XMLHttpRequest();
    } else {
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange = function () {
        if (xmlhttp.readyState === 4 && xmlhttp.status === 200) {
            document.getElementById("showTableMonitor").innerHTML = xmlhttp.responseText;
        }
    };

    // check which variables should be read from the database
    // compose a search query called 'reqCols' (sent to server at the end)
    var reqCols = 'controlpanel_functions/showTableMonitor.php?projectID=<?php echo PROJECTID?>&';
    var firstVar = 0;
    var cntVars = 0;
    for (var i = 0; i < tabNames.length; i++) {
        var varName = localStorage.getItem(tableNameActive + '_tcol' + i);
        if (varName) {
            if (firstVar == 1) reqCols += '&';
            reqCols += 'q' + cntVars + '=' + tabNames[i];
            firstVar = 1;
            cntVars++;
        }
    }
    reqCols += '&orderBy=' + localStorage[tableNameActive + '_orderByVar'];
    reqCols += '&ascOrDesc=' + localStorage[tableNameActive + '_ascOrDesc'];

    reqCols += '&n=' + cntVars;
    // this should be changed!
    reqCols += '&tableName=' + tableNameActive;

    xmlhttp.open("GET", reqCols, true);
    xmlhttp.send();
}

function sortTable() {
    var tableNameActive = tables[localStorage['activeTable']];
    var tabNames = loadVariables(tableNameActive);
    var varNameID = document.getElementById('sortBy').value;
    localStorage[tableNameActive + '_orderByVar'] = tabNames[varNameID];
    var ascDesc = document.getElementById('sortOrder').value;
    localStorage[tableNameActive + '_ascOrDesc'] = ascDesc;
}

// show and hide table elements
function toggleVis(btn1) {
    var tableNameActive = tables[localStorage['activeTable']];
    var btn = btn1.substr(btn1.length - 1);
    if (btn1.substr(btn1.length - 2, btn1.length - 1) % 1 == 0) btn = btn1.substr(btn1.length - 2);
    if (btn1.substr(btn1.length - 3, btn1.length - 2) % 1 == 0) btn = btn1.substr(btn1.length - 3);

    if (localStorage[tableNameActive + '_tcol' + btn] != 1) {
        localStorage[tableNameActive + '_tcol' + btn] = 1;
        document.getElementById(btn1).className = 'btn btn-info';
    } else {
        localStorage.removeItem(tableNameActive + '_tcol' + btn);
        document.getElementById(btn1).className = 'btn';
    }
}

function toggleVarMenu() {

    var e = document.getElementById('varMenu');
    if (e.style.display === 'block') {
        e.style.display = 'none';
        document.getElementById("button_sign").innerHTML = ">";
        localStorage.removeItem('varMenu');
    } else {
        e.style.display = 'block';
        document.getElementById("button_sign").innerHTML = "v";
        localStorage['varMenu'] = 1;
    }
}

