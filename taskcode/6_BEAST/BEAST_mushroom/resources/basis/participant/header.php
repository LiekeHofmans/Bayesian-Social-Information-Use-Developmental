<?php
include(PATH . "basis/common.php");
include(PATH . "basis/sqlLibrary.php");

if (!$_COOKIE['clientcookie']) {
    header("Location: " . PATH . "basis/participant/terminated.php?m=" . base64_encode(serialize(['messageNr' => 3, 'projectID' => PROJECTID])));
    exit();
}
$testMode = getParameter('testMode');

if ($testMode == 1) {
    $playerNr = readcookie("testcookie" . $_SESSION['sessionID'])[0];
    $bot = readcookie("botcookie" . $_SESSION['sessionID'])[0];
} else {
    $playerNr = readcookie("clientcookie")[0];
    $bot = 0;
}

$groupNr = getValue("core", "playerNr=$playerNr", "groupNr");
$period = getValue("core", "playerNr=$playerNr", "period");
$subjectNr = getValue("core", "playerNr=$playerNr", "subjectNr");
$currentGroupSize = getValue("core", "playerNr=$playerNr", "currentGroupSize");
$role = getValue("core", "playerNr=$playerNr", "role");
$randomid = getValue("session", "playerNr=$playerNr", "randomid");


// was the session terminated for this player?
$HITTerminated = getValue("core", "playerNr=$playerNr", "experimentTerminated");
if ($HITTerminated == 1) {
    header("Location: " . PATH . "basis/participant/terminated.php?session_index=" . $_SESSION['sessionID'] . "&m=" . base64_encode(serialize(
            ['messageNr' => 4, 'playerNr' => $playerNr, 'projectID' => PROJECTID])));

    exit();
}

// did the participant already leave the session? (only when trying to come back)
$leftExp = getValue("core", "playerNr=$playerNr", "leftExperiment");
if ($leftExp == 1) {
    header("Location: " . PATH . "basis/participant/terminated.php?m=" . base64_encode(serialize(['messageNr' => 9, 'projectID' => PROJECTID])));
    exit();
}

// group aborted?
$groupAborted = getValue("core", "playerNr=$playerNr", "groupAborted");
if ($groupAborted == 1) {
    header("Location: " . PATH . "basis/participant/terminated.php?session_index=" . $_SESSION['sessionID'] . "&m=" . base64_encode(serialize(['messageNr' => 6, 'projectID' => PROJECTID, 'playerNr' => $playerNr])));
    exit();
}

// tell server on which page the client is looking
$prevPage = getValue("core", "playerNr=$playerNr", "onPage");
$thisPage = basename($_SERVER['PHP_SELF']);
setValue("core", "playerNr=$playerNr", "onPage", $thisPage);
// a refresh should not reset the time
$tStart = time();
$tStartShown = '';
if ($prevPage != $thisPage) {
    setValue("core", "playerNr=$playerNr", "tStart", $tStart);
    $tStartShown = $tStart;
} else $tStartShown = getValue("core", "playerNr=$playerNr", "tStart");

// check if we are on a waiting page
if (substr($thisPage, 0, 4) == 'wait') {

    $waitingPageNr = substr($thisPage, 4);
    $waitingPageNr = explode('.', $waitingPageNr);
    $controllerVarName = 'wait_' . $waitingPageNr[0] . 'ready';
    setValue("core", "playerNr=$playerNr", $controllerVarName, 1);
    if ($_GET['jump'] != null && $_GET['jump'] != 0) {
        $jumped = explode('_', $_GET['jump']);
        foreach ($jumped as $stage) {
            setValue("core", "playerNr=$playerNr", 'wait_' . $stage . 'ready', 1);

        }
    }


}


$conn = mysqli_connect(HOST, ADMIN, PASSW, DBNAME) or die(mysqli_error());
if (mysqli_connect_errno()) {
    echo "Failed to connect to MySQL: " . mysqli_connect_error();
};// Check connection

$sql = "SELECT * FROM " . PROJECTID . "globals";
$result = mysqli_query($conn, $sql);
$names = [];
$values = [];
while ($row = mysqli_fetch_array($result)) {
    if (substr($row['name'], 0, 7) != 'message') {
        $names[] = $row['name'];
        $values[] = $row['value'];
    }
}

?>

<meta charset="utf-8">
<link rel="shortcut icon" href="<?php echo PATH; ?>basis/pic/logo-head.png">
<link rel="stylesheet" type="text/css" href="<?php echo PATH; ?>basis/css/mystyle.css">
<script src="<?php echo PATH; ?>basis/js_plugins/jquery-3.2.1.min.js" type="text/javascript"></script>
<script src="<?php echo PATH; ?>basis/jsLibrary.js?v8.3" type="text/javascript"></script>

<script>
    /* $.xhrPool.abortAll(); */
    var period = <?php echo json_encode($period, JSON_NUMERIC_CHECK)?>;
    var playerNr = <?php echo json_encode($playerNr, JSON_NUMERIC_CHECK)?>;
    var decisionsTable = [];
    if (typeof (Worker) !== "undefined") {
        // use web workers to write the last action time
        var w;

        function startWorker() {
            if (typeof (Worker) !== "undefined") {
                if (typeof (w) == "undefined") {
                    w = new Worker("<?php echo PATH; ?>basis/participant/keepConnected.js");
                    w.postMessage(playerNr);
                }
                w.onmessage = function (event) {
                    document.getElementById("result").innerHTML = event.data;
                };
            } else {
                document.getElementById("result").innerHTML = "Sorry, your browser does not support Web Workers...";
            }
        }

        startWorker();
    } else {
        var connect = setInterval(function () {
            clientConnected(playerNr)
        }, 3000); // the old way
    }

    var subjectNr = <?php echo json_encode($subjectNr, JSON_NUMERIC_CHECK)?>;
    var groupNr = <?php echo json_encode($groupNr, JSON_NUMERIC_CHECK)?>;
    var currentGroupSize = <?php echo json_encode($currentGroupSize, JSON_NUMERIC_CHECK)?>;

    var role = <?php echo json_encode($role, JSON_NUMERIC_CHECK)?>;
    var bot = <?php echo json_encode($bot, JSON_NUMERIC_CHECK)?>;
    var randomid = <?php echo json_encode($randomid, JSON_NUMERIC_CHECK)?>;
    var tStart = <?php echo json_encode($tStartShown, JSON_NUMERIC_CHECK)?>;
    // read all parameters
    var names = <?php echo json_encode($names)?>;
    var values = <?php echo json_encode($values, JSON_NUMERIC_CHECK)?>;
    var path = <?php echo json_encode(PATH . "basis/")?>;
    for (var i = 0; i < names.length; i++) window[names[i]] = values[i];
    if (typeof participationFee !== 'undefined') {
        participationFee = parseFloat(participationFee);
    }
    console.log("loopStart:" + loopStart);
</script>



<script>


    var testMode = getParameter('testMode');
    if (testMode != 1 && (document.hidden || !document.hasFocus())) {
        alert('This experiment continues now.')
    }
    // store the connection in a variable to switch it off when needed

</script>
