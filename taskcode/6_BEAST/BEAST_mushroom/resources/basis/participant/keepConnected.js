/**
 * Created by molleman on 10/10/2017.
 */
var pNr;
self.addEventListener("message", function (e) {
    pNr = e.data;
    var xhttp = new XMLHttpRequest(); // web workers do not support AJAX

    var callClientConnected = function () {
        xhttp.open("POST", "../ajax/clientConnected.php", true);
        xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhttp.send("playerNr=" + pNr);
        setTimeout(callClientConnected, 3000);
    };
    callClientConnected();
    /* the passed-in data is available via e.data */
}, false);

