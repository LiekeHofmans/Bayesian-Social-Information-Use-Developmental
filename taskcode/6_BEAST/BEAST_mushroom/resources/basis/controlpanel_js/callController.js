var projectid;
onmessage = function(e){
    projectid = e.data;
    var xhttp = new XMLHttpRequest(); // web workers do not support AJAX
        var callControllerAlg = function () {
            xhttp.open("GET", "../controlpanel_functions/controllerAlgorithm.php?projectID="+projectid, true);
            xhttp.send();
            xhttp.onreadystatechange = function () {
                if (xhttp.readyState == 4 && xhttp.status == 200) {
                    postMessage(xhttp.responseText);
                }
            };
            setTimeout(callControllerAlg, 1000);
        };
    callControllerAlg();
};