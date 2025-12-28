/* ===== FUNCTIONS TO REGULATE EXPERIMENTAL FLOW ===== */
var timers = [];
var popup = 0; /* legacy for experiments which are compiled before October 2020 */

$('html').bind('keypress', function (e) {
    if (e.keyCode === 13) {
        return false;
    }
});


function getCookieValue(a) {
    var b = document.cookie.match('(^|;)\\s*' + a + '\\s*=\\s*([^;]+)');
    return b ? b.pop() : '';
}

/**
 * @deprecated This is called via worker now and this function is only for backup reasons.
 */
function clientConnected(playerNr) {
    $.ajax({
        type: 'POST',
        url: path + 'ajax/clientConnected.php',
        data: {playerNr: playerNr},
        async: true
    });
}


/* count number of failures in the quiz */
function quizFail(playerNr, readonly, wronganswers) {

    $.ajax({
        type: 'POST',
        url: path + 'ajax/quizFail.php',
        data: {playerNr: playerNr, readonly: readonly, wronganswers: wronganswers},
        async: false,
        success: function (data) {
            numFails = data;
        }
    });
    return numFails;
}

/* loop through text changes in task bar to attract attention if screen is minimised (e.g. in lobby) */
function decisionAlert(docTitle) {
    var oldTitle = docTitle;
    var msg = 'THE EXPERIMENT CONTINUES NOW.';
    var timeoutId;
    var blink = function () {
        if (document.title == oldTitle) document.title = msg;
        else document.title = oldTitle;
    };
    var clear = function () {
        clearInterval(timeoutId);
        document.title = oldTitle;
        window.onmousemove = null;
        timeoutId = null;
    };
    if (!timeoutId) {
        timeoutId = setInterval(blink, 750);
        window.onmousemove = clear;
    }
}

function validEntry(value) {
    if (value == null || value == "" || isNaN(value)) {
        alert('Please enter your response.');
        return false;
    }
}

function showNext(url, nextstage, stageNr) {

    var timeRecName = "time_" + stageNr;
    var timeOnThisPage = getServerTime() - tStart;
    setValue(timeRecName, timeOnThisPage);
    for (var i = 0; i < timers.length; i++) {
        clearTimeout(timers[i]);
    }

    location.replace(url);


}


/* validate the value of an integer */
function validInteger(value, min, max) {
    if (value == null || value == "" || isNaN(value) || value < min || value > max) {
        alert('Please enter a number between ' + min + ' and ' + max + '!');
        return false;
    }
    if (value % 1 != 0) {    /* the client entered a decimal number */
        alert('Please do not use decimals.');
        return false;
    }
    return true;
}

/* check if the entry is already present */
function entryPresent(variable) {
    var presentYesOrNo = false;
    if (getValue('decisions', 'playerNr=' + playerNr + ' and period=' + period, variable)) presentYesOrNo = true;
    return presentYesOrNo;
}

/* a few simple functions to write stuff to the decisions table */
function record_decisions(varName, value) {
    if (arguments.length == 1) {
        var value = varName.value1;
        var name = varName.name;
        setValue('decisions', 'playerNr=' + playerNr + ' and period=' + period, name, value);
    } else setValue('decisions', 'playerNr=' + playerNr + ' and period=' + period, varName, value);
}

/* this function should replace the record_decisions() function above */
function record(varName, value) {
    if (arguments.length == 1) {
        var value = varName.value1;
        var name = varName.name;
        setValue('decisions', 'playerNr=' + playerNr + ' and period=' + period, name, value);
    } else setValue('decisions', 'playerNr=' + playerNr + ' and period=' + period, varName, value);
}

function waitingAnimation() {
    document.write('<center><img src="' + path + 'pic/working.gif"></center>');
}


/* method for sorting numerical arrays */
function sortNumber(a, b) {
    return a - b;
}

function groupSizeAlert(text) {
    if (arguments.length == 0) txt1 = 'Note: one or more members of your group have dropped out. <br>You can continue with the remaining members. ';
    else txt1 = text;
    if (currentGroupSize != groupSize) {
        var alertTxt = '<div class="alert-danger" style="text-align:center">';
        alertTxt += txt1;
        alertTxt += '</div>';
        document.write(alertTxt);
    }
}

/* timer for the page */
function countdownTimer(screenTimeout, timeoutPage, kickout) {
    document.write('<div class="row" style="text-align: center; margin-top: 2px;"><div  class="alert alert-info" id="countdown"><span id="countdown_text">Remaining time: &nbsp;</span><span id="countdown_timer"></span></div></div>');

    $(window).on('load', function () {
        var locationName = window.location.href.replace(/\W/g, '');
        if ((getCookieValue(locationName) === "") || (performance.navigation.type === 0) || (performance.navigation.type === 255)) {
            var time = new Date().getTime();
            document.cookie = '' + locationName + '=' + time + '; path=/; samesite=lax';

        }
        var start = getCookieValue(locationName);
        var now = new Date().getTime();
        var seconds = screenTimeout - Math.round(now / 1000) + Math.round(start / 1000);
        timers.push(setInterval(function () {
            var remainingSeconds = seconds % 60;
            var remainingMinutes = Math.floor(seconds / 60);

            var txt = "";
            if (remainingMinutes < 10) txt = txt.concat("0");
            txt = txt.concat(remainingMinutes + ":");
            if (remainingSeconds < 10) txt = txt.concat('0');
            txt = txt.concat(remainingSeconds);
            if (seconds <= 0) txt = "00:00";
            document.getElementById('countdown_timer').innerHTML = txt;
            if (seconds <= 0 && kickout) {
                location.replace(timeoutPage);
            } else if (seconds > 0) seconds--;
            if (seconds < 10) {
                $('#countdown').removeClass("alert-info").addClass("alert-danger");
                document.getElementById('countdown').setAttribute("style", "color: red");
            }
        }, 1000));
    });
}

/* timer for the button to make it appear later */
function timer(time, update, complete) {

    $(window).on('load', function () {
        var start = new Date().getTime();
        var interval = setInterval(function () {
            var now = time - (new Date().getTime() - start);
            if (now <= 0) {
                clearInterval(interval);
                complete();
            } else update(Math.floor(now / 1000));
        }, 100);
    })
}

/* specify a script that counts the number of players we are waiting for to form a group */
function lobbyInfo() {
    var countReady = getNumberReadyLobby(role);
    var waitFor = (groupSize - countReady) % groupSize;
    var txt = 'We are waiting for <b>' + waitFor + '</b> more participant';
    if (waitFor > 1) txt = txt + 's';
    txt = txt += '...';
    if (waitFor == 0) txt = '';
    document.getElementById('waitingFor').innerHTML = txt;
}


function lobbyCheck(nextPage) {
    /* move on once a group number has been allocated */
    setInterval(function () {
        var groupNumber = getValue('core', 'playerNr=' + playerNr, 'groupNr');
        if (groupNumber > 0) location.replace(nextPage);
    }, 3000);
    /* regularly execute the above two functions so we start as soon as we are ready */
}

function checkReady(nextPage1, nextPage2) {
    waitingAnimation();
    var finalStage = 0;
    /* this is the final stage of this period */
    if (nextPage2) {
        setValue('core', 'playerNr=' + playerNr, 'wait_lastInPeriod', 1);
        var interval = setInterval(function () {
            var periodReady = getValue('core', 'playerNr=' + playerNr, 'periodReady');
            if (periodReady == 1) {
                var nextPeriod = getValue('core', 'playerNr=' + playerNr, 'period');
                if (nextPeriod > parseInt(numberPeriods)) { /* we are finished */
                    clearInterval(interval);
                    window.location.replace(nextPage1);
                } else {/* we are not finished yet */
                    clearInterval(interval);
                    window.location.replace(nextPage2);
                }
            }
        }, 1000);
    }

    /* this is a 'normal' waiting page, NOT the final stage of this period */
    else {
        var interval = setInterval(function () {
            var countReady = getNumberReady(playerNr);
            var currentGroupSize = getValue('core', 'playerNr=' + playerNr, 'currentGroupSize');
            if (countReady == currentGroupSize) {
                clearInterval(interval);
                window.location.replace(nextPage1);
            }
        }, 1000);
    }
}

/* shuffle an array */
function shuffle(o) {
    for (var j, x, i = o.length; i; j = Math.floor(Math.random() * i), x = o[--i], o[i] = o[j], o[j] = x) ;
    return o;
}

/* ===== INTERACTING WITH THE DATABASE ===== */


/* inserting a record in the database */
function insertRecord(tableName, varNames, values) {
    var valStr = values.toString();
    var json_varNames = JSON.stringify(varNames);
    var json_values = JSON.stringify(valStr);

    $.ajax({
        type: 'POST',
        url: path + 'ajax/insertRecord.php',
        data: {
            tableName: tableName,
            varNames: json_varNames,
            values: json_values
        },
        async: false
    });
}

/* updating one value in the database */
function setValue(tableName, condition, varName, value) {
    /* we have received an object if argument.length ==1 ??*/


    if (arguments.length === 2) {
        varName = arguments[0];
        value = arguments[1];
        tableName = 'decisions';
        condition = 'playerNr=' + playerNr + ' and period=' + period;
    }

    $.ajax({
        type: 'POST',
        url: path + 'ajax/setValue.php',
        data: {
            tableName: tableName,
            condition: condition,
            varName: varName,
            value: value
        },
        async: false,
        cache: false,
        headers: {
            "cache-control": "no-cache"
        }
    });
}


function setValueAtTimeout(tableName, condition, varName, value) {

    /* we have received an object if argument.length ==1 ??*/


    if (arguments.length === 2) {
        varName = arguments[0];
        value = arguments[1];
        tableName = 'decisions';
        condition = 'playerNr=' + playerNr + ' and period=' + period;
    }

    $(window).on('unload', function () {

        var data = new FormData();
        data.append('tableName', tableName);
        data.append('condition', condition);
        data.append('varName', varName);
        data.append('value', value);
        navigator.sendBeacon(path + 'ajax/setValue.php', data);

    });


}

function setValueAtTimeout2(tableName, condition, varName, value) {

    /* we have received an object if argument.length ==1 ??*/


    if (arguments.length === 2) {
        varName = arguments[0];
        value = arguments[1];
        tableName = 'decisions';
        condition = 'playerNr=' + playerNr + ' and period=' + period;
    }


    var data = new FormData();
    data.append('tableName', tableName);
    data.append('condition', condition);
    data.append('varName', varName);
    data.append('value', value);
    navigator.sendBeacon(path + 'ajax/setValue.php', data);


}

function setBonus(amount) {
    setValue('session', 'playerNr=' + playerNr, 'bonusAmount', amount);
    var totalDollarsEarned = parseFloat(amount) + parseFloat(participationFee);
    var totalEarned = totalDollarsEarned.toFixed(2);
    setValue('session', 'playerNr=' + playerNr, 'totalEarnings', totalEarned);
}

function getRandomID() {
    return getInt('session', 'playerNr=' + playerNr, 'randomid');
}

/* get a parameter value from the database */
function getParameter(parName) {
    return getValue('globals', 'name=\'' + parName + '\'', 'value');
}

function getGlobal(parName) {
    return getValue('globals', 'name=\'' + parName + '\'', 'value');
}

function setGlobal(parName, value) {
    setValue('globals', 'name=\'' + parName + '\'', 'value', value);
}

/* getting values from the database tables */
function getValue(tableName, condition, varName) {
    if (arguments.length === 1) {
        varName = arguments[0];
        tableName = 'decisions';
        condition = 'playerNr=' + playerNr + ' and period=' + period;
    }
    return JSON.parse($.ajax({
        type: 'POST',
        url: path + 'ajax/getValue.php',
        dataType: 'json',
        data: {tableName: tableName, condition: condition, varName: varName},
        global: false,
        async: false,
        cache: false,
        headers: {
            "cache-control": "no-cache"
        },
        success: function (data) {
            return data;
        }
    }).responseText);
}


/* getting values from the database tables FROM THE PREVIOUS PERIOD */
function getOldValue(tableName, condition, varName) {
    if (arguments.length === 1) {
        varName = arguments[0];
        tableName = 'decisions';
        condition = 'playerNr=' + playerNr + ' and period=' + (period - 1);
    }
    return getValue(tableName, condition, varName);

}

/* get multiple values from the database and return as array */
function getValues(tableName, condition, varName, sortBy, ascOrDesc) {
    if (arguments.length === 1) {
        varName = arguments[0];
        tableName = 'decisions';
        condition = 'groupNr=' + groupNr + ' and period=' + period;
    }
    if (arguments.length < 4) {
        var sortBy = 'playerNr';
    }
    return JSON.parse($.ajax({
        type: 'POST',
        url: path + 'ajax/getValues.php',
        dataType: 'json',
        data: {tableName: tableName, condition: condition, varName: varName, sortBy: sortBy},
        global: false,
        async: false,
        success: function (data) {
            return data;
        }
    }).responseText);
}

/* get multiple values from the database and return as array */
function getOldValues(tableName, condition, varName, sortBy, ascOrDesc) {
    if (arguments.length === 1) {
        varName = arguments[0];
        tableName = 'decisions';
        condition = 'groupNr=' + groupNr + ' and period=' + (period - 1);
    }
    if (arguments.length < 4) {
        sortBy = 'playerNr';
    }
    return JSON.parse($.ajax({
        type: 'POST',
        url: path + 'ajax/getValues.php',
        dataType: 'json',
        data: {tableName: tableName, condition: condition, varName: varName, sortBy: sortBy},
        global: false,
        async: false,
        success: function (data) {
            return data;
        }
    }).responseText);
}


/* get multiple values from the database and return as array PREVIOUS PERIOD */
function getValuesOthers(varName) {
    var tableName = 'decisions';
    var condition = 'groupNr=' + groupNr + ' and period=' + period + ' and playerNr!=' + playerNr;
    var sortBy = 'subjectNr';
    return JSON.parse($.ajax({
        type: 'POST',
        url: path + 'ajax/getValues.php',
        dataType: 'json',
        data: {tableName: tableName, condition: condition, varName: varName, sortBy: sortBy},
        global: false,
        async: false,
        success: function (data) {
            return data;
        }
    }).responseText);
}

/* get multiple values from the database and return as array PREVIOUS PERIOD */
function getOldValuesOthers(varName) {
    var tableName = 'decisions';
    var condition = 'groupNr=' + groupNr + ' and period=' + (period - 1) + ' and playerNr!=' + playerNr;
    var sortBy = 'subjectNr';
    return JSON.parse($.ajax({
        type: 'POST',
        url: path + 'ajax/getValues.php',
        dataType: 'json',
        data: {tableName: tableName, condition: condition, varName: varName, sortBy: sortBy},
        global: false,
        async: false,
        success: function (data) {
            return data;
        }
    }).responseText);
}


/* getting values from the database tables */
function getInt(tableName, condition, varName) {
    if (arguments.length === 1) {
        varName = arguments[0];
        tableName = 'decisions';
        condition = 'playerNr=' + playerNr + ' and period=' + period;
    }
    return getValue(tableName, condition, varName);
}

/* get multiple values from the database and return as array */
function getInts(tableName, condition, varName, sortBy, ascOrDesc) {
    if (arguments.length === 1) {
        varName = arguments[0];
        tableName = 'decisions';
        condition = 'groupNr=' + groupNr + ' and period=' + period;
    }
    if (arguments.length < 4) {
        sortBy = 'playerNr';
    }
    return getValues(tableName, condition, varName, sortBy, ascOrDesc)
}

/* getting values from the database tables */
function getFloat(tableName, condition, varName) {
    if (arguments.length === 1) {
        varName = arguments[0];
        tableName = 'decisions';
        condition = 'playerNr=' + playerNr + ' and period=' + period;
    }
    return getValue(tableName, condition, varName);
}

/* get multiple values from the database and return as array */
function getFloats(tableName, condition, varName, sortBy, ascOrDesc) {
    if (arguments.length === 1) {
        varName = arguments[0];
        tableName = 'decisions';
        condition = 'groupNr=' + groupNr + ' and period=' + period;
    }
    if (arguments.length < 4) {
        sortBy = 'playerNr';
    }
    return getValues(tableName, condition, varName, sortBy, ascOrDesc)
}

/* get multiple values from the database and return as array */
function getIntsOthers(varName) {
    return getValuesOthers(varName);
}

/* get multiple values from the database and return as array */
function getFloatsOthers(varName) {
    return getValuesOthers(varName);
}

/* get the role of the current player from the database */
function getRole() {
    return getValue('core', 'playerNr=' + playerNr, 'role');
}

/* set the role of the current player to the database */
function setRole(role) {
    setValue('core', 'playerNr=' + playerNr, 'role', role);
}

/* count how many are ready in lobby */
function getNumberReadyLobby(role) {
    return parseInt(JSON.parse($.ajax({
        type: 'POST',
        url: path + 'ajax/numberReadyLobby.php',
        dataType: 'json',
        data: {role: role},
        global: false,
        async: false,
        success: function (data) {
            return data;
        }
    }).responseText));
}

/* count how many are ready to proceed to the next step (define checkervar yourself) */
function getNumberReady(playerNr) {
    return parseInt(JSON.parse($.ajax({
        type: 'POST',
        url: path + 'ajax/numberReadyNextStep.php',
        dataType: 'json',
        data: {playerNr: playerNr},
        global: false,
        async: false,
        success: function (data) {
            return data;
            /* cache: false; */
        }
    }).responseText));
}

/* get the number of seconds since 1st January 1970 */
function getServerTime() {
    return parseInt(JSON.parse($.ajax({
        type: 'GET',
        url: path + 'ajax/getServerTime.php',
        dataType: 'json',
        global: false,
        async: false,
        success: function (data) {
            return data;
        }
    }).responseText));
}


/* this is executed in the first stage of a period only */
function firstStage() {
    setValue('core', 'playerNr=' + playerNr, 'periodReady', 0);
    var perInDB = getValue('decisions', 'playerNr=' + playerNr + ' and period=' + period, 'groupNr');
    if (!perInDB) insertRecord('decisions', 'playerNr, groupNr, subjectNr, period', [playerNr, groupNr, subjectNr, period]);
}

function htmlEncode(html) {
    return encodeURI(html);
}

function changeMultiElement(fieldnumber, valueadd) {

    var field = $("#field" + fieldnumber);
    let values = field.val();

    if (values !== "") values = values.split(",");
    else values = [];

    var index = values.indexOf(valueadd.toString());

    var add = true;
    if (index === -1) {
        values.push(valueadd);
    } else {
        add = false;
        values.splice(index, 1);

    }
    if (values.length > 1) {
        field.val(values.sort().toString());
    } else {
        field.val(values[0]);

    }
    return add;


}

function getMessageStream(labelname, idElement) {

    let ownmessages = getValue(labelname);

    let othermessages = getValuesOthers(labelname);

    let allmessages = decodeMessages(ownmessages, "[You]: ");

    for (var i = 0; i < othermessages.length; i++) {
        let textother = "[Other]: ";
        if (othermessages.length > 1) {
            textother = "[Other " + (i + 1) + "]: ";
        }

        let otherm = decodeMessages(othermessages[i], textother);

        allmessages = Object.assign(allmessages, otherm);

    }
    let messagestream = "";
    const ordered = {};
    Object.keys(allmessages).sort().forEach(function (key) {
        ordered[key] = allmessages[key];
        messagestream += decodeURI(allmessages[key]) + "<br>";
    });


    if (messagestream !== "") {
        var messagestreamcont = $("#messagestream" + idElement);
        messagestreamcont.html(messagestream);
        messagestreamcont.scrollTop(messagestreamcont[0].scrollHeight);

    }


}

function decodeMessages(messagestring, addtext = false) {

    let messageobject = {};

    if (messagestring !== null) {

        let parts = messagestring.split("####");

        for (var i = 0; i < parts.length; i++) {

            let parts2 = parts[i].split("$$$");
            let fulltext = "";
            if (addtext) {
                fulltext = addtext.toString() + parts2[1];
            } else {
                fulltext = parts2[1];
            }
            messageobject[parts2[0]] = (fulltext);
        }
    }
    return messageobject;
}

function encodeMessages(messageobject) {

    let messagestring = "";

    for (var key in messageobject) {
        if (messageobject.hasOwnProperty(key)) {
            if (messagestring !== "") messagestring = messagestring + "####";
            messagestring = messagestring + key + "$$$" + messageobject[key];
        }
    }


    return messagestring;
}

function changeRadio(value, field) {


    $(".radiobuttons" + field).css("background-position", "0 0");
    $("#radiobutton" + field + value).css("background-position", "0 -50px");
    $("#field" + field).val(value);


}


/**
 * Ajax Request Pool
 *
 * @author Oliver Nassar <onassar@gmail.com>
 * @see    http://stackoverflow.com/questions/1802936/stop-all-active-ajax-requests-in-jquery
 */
jQuery.xhrPool = [];

/**
 * jQuery.xhrPool.abortAll
 *
 * Retrieves all the outbound requests from the array (since the array is going
 * to be modified as requests are aborted), and then loops over each of them to
 * perform the abortion. Doing so will trigger the ajaxComplete event against
 * the document, which will remove the request from the pool-array.
 *
 * @access public
 * @return void
 */
jQuery.xhrPool.abortAll = function () {
    var requests = [];
    for (var index in this) {
        if (isFinite(index) === true) {
            requests.push(this[index]);
        }
    }
    for (index in requests) {
        requests[index].abort();
    }
};

/**
 * jQuery.xhrPool.remove
 *
 * Loops over the requests, removes it once (and if) found, and then breaks out
 * of the loop (since nothing else to do).
 *
 * @access public
 * @param  Object jqXHR
 * @return void
 */
jQuery.xhrPool.remove = function (jqXHR) {
    for (var index in this) {
        if (this[index] === jqXHR) {
            jQuery.xhrPool.splice(index, 1);
            break;
        }
    }
};

/**
 * Below events are attached to the document rather than defined the ajaxSetup
 * to prevent possibly being overridden elsewhere (presumably by accident).
 */
$(document).ajaxSend(function (event, jqXHR, options) {
    jQuery.xhrPool.push(jqXHR);
});
$(document).ajaxComplete(function (event, jqXHR, options) {
    jQuery.xhrPool.remove(jqXHR);
});
