<?php
include(PATH . "basis/sqlLibrary.php");

$bot = $_GET['bot'] == 1;
$timeNow = date('Y/m/d H:i:s');

// first check if the browser is Internet Explorer. This is not supported.
$isInternetExplorer = 0;
if (preg_match('/(?i)msie/', $_SERVER['HTTP_USER_AGENT'])) $isInternetExplorer = 1;
if (preg_match('/MSIE\s(?P<v>\d+)/i', @$_SERVER['HTTP_USER_AGENT'], $B) && $B['v'] <= 8) $isInternetExplorer = 1;
if (preg_match('~MSIE|Internet Explorer~i', $_SERVER['HTTP_USER_AGENT']) || (strpos($_SERVER['HTTP_USER_AGENT'], 'Trident/7.0; rv:11.0') !== false)) $isInternetExplorer = 1;
if ($isInternetExplorer == 1) {
    header("Location: " . PATH . "basis/participant/terminated.php?message=7&m=" . base64_encode(serialize(['messageNr' => 7, 'projectID' => PROJECTID])));
    exit();
}

// then check if the session is 'active'
$sessionLive = getParameter('active');
if ($sessionLive != 1) {
    header("Location: " . PATH . "basis/participant/terminated.php?m=" . base64_encode(serialize(['messageNr' => 0, 'projectID' => PROJECTID])));
    exit();
}

// retrieve the client's ipaddress
$ipaddress = getenv('HTTP_CLIENT_IP') ?:
    getenv('HTTP_X_FORWARDED_FOR') ?:
        getenv('HTTP_X_FORWARDED') ?:
            getenv('HTTP_FORWARDED_FOR') ?:
                getenv('HTTP_FORWARDED') ?:
                    getenv('REMOTE_ADDR');

// allowing multiple entries from same device (uncomment for test mode)
$totalPlayers = getParameter('totalPlayers');
$timestamp = getParameter('compiled');

if ($_SERVER['SERVER_ADDR'] == "132.231.59.8" && PROJECTID != 'e409g26604_' && PROJECTID != 'e409g26843_' && PROJECTID != 'e409g26878_' && PROJECTID != 'e1122g28396_') {
    if ($totalPlayers > 100) $totalPlayers = 100;
}

$testMode = getParameter('testMode');
$ipaddress_unencrypted = $ipaddress;
$ipaddress = md5($ipaddress);
if ($testMode == 1) $ipaddress .= rand(10000000, 99999999);

// check if this IP has already present logged in (preventing double log-ins)

$conn = mysqli_connect(HOST, ADMIN, PASSW, DBNAME) or die(mysqli_error());
$sql = "SELECT * FROM " . PROJECTID . "core";
$result = @mysqli_query($conn, $sql) or die("Couldn't execute query " . $sql);
$IParray = [];
while ($row = mysqli_fetch_array($result)) {
    $IParray[] = $row['ipaddress'];
}
// if IP is present, send client away (for testing, use 'sneakin.php' instead of 'begin.php'
$IPpresent = false;

/* participant from the same session comes back */
$reEnter = getParameter('reEnter');
if ($reEnter == 1 && isset($_COOKIE['clientcookie']) && $_COOKIE['clientcookie'] != 0 && $_COOKIE['clienttimestamp'] == $timestamp & $testMode != 1) {
    $sql = "SELECT onPage, leftExperiment, experimentTerminated, groupAborted FROM " . PROJECTID . "core WHERE playerNr=" . $_COOKIE['clientcookie'] . " LIMIT 1";
    $result = @mysqli_query($conn, $sql) or die("Couldn't execute query " . $sql);
    $row = mysqli_fetch_array($result);
    $location = $row['onPage'];
    if ($location != "" && $location != null && $row['leftExperiment'] != 1
        && $row['experimentTerminated'] != 1 && $row['groupAborted'] != 1) header("Location: " . $location);
}


if (in_array($ipaddress, $IParray)) {
    $IPpresent = true;
    $timeNow = date('Y/m/d H:i:s');
    $groupNr = 0;
    $message = 'Double entry attempt by ' . $ipaddress;
    insertRecord("logEvents", "groupNr, timeEvent, event", "'$groupNr', '$timeNow', '$message'");
    header("Location: " . PATH . "basis/participant/terminated.php?m=" . base64_encode(serialize(['messageNr' => 1, 'projectID' => PROJECTID])));
    exit();
}


$sessionFull = true;

// if the session is not full yet, write IP address to server
if (count($IParray) < $totalPlayers || $testMode == 1) {
    $sessionFull = false;
    // write a subject number for this client to the table 'core' (similar to 'Clients table' in zTree)
    if (!$IPpresent) {
        $ctx = stream_context_create(['http' => ['timeout' => 10]]);
        $location = unserialize(file_get_contents('http://www.geoplugin.net/php.gp?ip=' . $ipaddress_unencrypted, false, $ctx));
        $longitude = $location['geoplugin_longitude'];
        $latitude = $location['geoplugin_latitude'];
        $coordinates = $latitude . "#" . $longitude;
        $ipaddress_part = substr($ipaddress_unencrypted, 0, 10);
        if ($longitude === null || $latitude === null) {
            $sql = "INSERT INTO " . PROJECTID . "core (ipaddress, ipaddress_part) VALUES ('" . $ipaddress . "','" . $ipaddress_part . "')";
        } else {
            $sql = "INSERT INTO " . PROJECTID . "core (ipaddress, ipaddress_part, location) VALUES ('" . $ipaddress . "','" . $ipaddress_part . "','" . $coordinates . "')";
        }
        $result = @mysqli_query($conn, $sql) or die("Couldn't execute query " . $sql);

        $playerNr = @mysqli_insert_id($conn);

    } else $playerNr = 0;
} else $playerNr = 0;
?>

<html lang="en">
<head>
    <title>Connecting to server</title>
    <script src="<?php echo PATH; ?>basis/js_plugins/jquery-3.2.1.min.js" type="text/javascript"></script>
    <script src="<?php echo PATH; ?>basis/jsLibrary.js?v5" type="text/javascript"></script>
    <link rel="shortcut icon" href="<?php echo PATH; ?>basis/pic/logo-head.png">
</head>
<body>
<NOSCRIPT>
    <div class="alert alert-danger">Javascript is disabled. Please enable JavaScript and refresh this page to
        continue.
    </div>
</NOSCRIPT>
<div class="" style="text-align: center;"><br><br><br><img src="<?php echo PATH; ?>basis/pic/working.gif">&nbsp;&nbsp;&nbsp;Connecting
    to server
</div>
</body>
</html>

<script>
    var projectID =<?php echo json_encode(PROJECTID);?>;
    var path = <?php echo json_encode(PATH . "basis/");?>;
    var serverTime = <?php echo json_encode($timeNow);?>;
    var testMode = <?php echo json_encode($testMode, JSON_NUMERIC_CHECK);?>;
    var IPpresent = <?php echo json_encode($IPpresent);?>;
    var IPaddress = <?php echo json_encode($ipaddress);?>;
    var sessionFull = <?php echo json_encode($sessionFull);?>;
    var externalID = <?php if (isset($_GET['tic'])) echo json_encode($_GET['tic']); else echo 'null'; ?>;
    var timestamp = <?php echo $timestamp; ?>;

    var playerNr = <?php echo json_encode($playerNr, JSON_NUMERIC_CHECK);?>;

    // double entry --> kick player out
    if (IPpresent) {
        insertRecord('logEvents', 'playerNr', 0);
        var messg = 'Double entry by ' + IPaddress;
        setValue('logEvents', 'playerNr=' + playerNr, 'event', messg);
        setValue('logEvents', 'playerNr=' + playerNr, 'timeEvent', serverTime);
        location.replace(path + 'participant/terminated.php?m=<?php echo base64_encode(serialize(['messageNr' => 1, 'projectID' => PROJECTID])); ?>');
    }

    var totalPlayers =<?php echo $totalPlayers; ?>;


    totalPlayers = parseInt(totalPlayers);

    if ((playerNr > totalPlayers || sessionFull) && testMode == 0) {
        insertRecord('logEvents', 'playerNr', playerNr);
        const messg_full = 'Player ' + playerNr + ' did not enter as the session is full';
        setValue('logEvents', 'playerNr=' + playerNr, 'event', messg_full);
        location.replace(path + 'participant/terminated.php?m=<?php echo base64_encode(serialize(['messageNr' => 2, 'projectID' => PROJECTID])); ?>');
    } else {
        document.cookie = "clientcookie=" + playerNr + "; max-age=8640000; path=/; samesite=lax";
        document.cookie = "clienttimestamp=" + timestamp + "; max-age=8640000; path=/; samesite=lax";
        document.cookie = "testcookie<?php echo $_SESSION['sessionID'];?>=" + playerNr + "; path=/; samesite=lax";
        document.cookie = "botcookie<?php echo $_SESSION['sessionID'];?>=<?php echo $bot;?>; path=/; samesite=lax";

        var rnd1 = Math.floor(Math.random() * 10) + 2000000 + playerNr * 100;
        var rnd2 = Math.floor(Math.random() * 10) + 1000000 + playerNr * 100;

        if (getValue('session', 'playerNr=' + playerNr, 'randomid')) {
        } else {
            insertRecord('session', 'playerNr', playerNr);
            insertRecord('logEvents', 'playerNr', playerNr);
            var messg = 'Player ' + playerNr + ' entered the session';
            setValue('logEvents', 'playerNr=' + playerNr, 'event', messg);
            setValue('logEvents', 'playerNr=' + playerNr, 'timeEvent', serverTime);

            /* set session cookie [not used now] */
            var xmlhttp;
            if (window.XMLHttpRequest) {
                xmlhttp = new XMLHttpRequest();
            } else {
                xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
            }
            xmlhttp.open("POST", path + "ajax/setSessionCookie.php?playerNr=" + playerNr, false);
            xmlhttp.send();
        }
        var participationFee = getParameter('participationFee');
        setValue('session', 'playerNr=' + playerNr, 'randomid', rnd2);
        setValue('session', 'playerNr=' + playerNr, 'randomidNotPlayed', rnd1);
        setValue('session', 'playerNr=' + playerNr, 'relevantRandomid', rnd2);
        setValue('session', 'playerNr=' + playerNr, 'externalID', externalID);
        setValue('session', 'playerNr=' + playerNr, 'participationAmount', participationFee);
        setValue('session', 'playerNr=' + playerNr, 'totalEarnings', participationFee);
        setValue('core', 'playerNr=' + playerNr, 'period', 1);
        setValue('core', 'playerNr=' + playerNr, 'role', 1);

        location.replace('<?php echo FIRSTPAGE . ".php?session_index=" . $_SESSION['sessionID'];?>');
    }


</script>






