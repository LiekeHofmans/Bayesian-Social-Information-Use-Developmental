<?php
if (isset($_GET['m'])) {
    $message = base64_decode($_GET['m']);
    $paramarray = unserialize($message);

    $messageNr = $paramarray['messageNr'];
    $playerNr = $paramarray['playerNr'];
    $projectID = $paramarray['projectID'];


} else $messageNr = -1;

define("PROJECTID", $projectID);
include("../common.php");
include("../sqlLibrary.php");

// message 0 = HIT is offline ('sessionOffline.php')
// message 1 = duplicate participant ('devicePresent.php')
// message 2 = HIT is full    ('HITfull.php')
// message 3 = no player cookie found ('notLoggedIn.php')
// message 4 = HIT terminated ('HITterminated.php')
// message 5 = time out decision
// message 6 = Group was aborted ('HITendedTimeout.php')
// message 7 = browser (IE) not supported ('browserNotSupported.php')
// message 8 = quiz fails
// message 9 = leftExperiment
$parName = 'message' . $messageNr;
/*
 * TODO messagetext should go to parameters as well
 */
if ($messageNr == -1 || $messageNr > 9) $messageText = "An error occurred. You cannot access this page.";
elseif ($messageNr == 9) $messageText = "You already have left the experiment.<br><br> 
		You can close this window.";
else $messageText = getParameter($parName);
?>
<html lang="en">
<head>
    <title>Experiment stopped</title>
    <link rel="shortcut icon" href="../pic/logo-head.png">
    <link rel="stylesheet" type="text/css" href="../css/mystyle.css">
    <link href="../css/newlayout.css" rel="stylesheet" type="text/css"/>
    <link href="../css/newlayout_bootstrap.css" rel="stylesheet" type="text/css"/>
    <script src="../js_plugins/jquery-3.2.1.min.js"></script>
    <script src="../jsLibrary.js?v5" type="text/javascript"></script>
</head>
<body>
<script>
    //    clearInterval(connect); // stop telling the server that this participant is still active
    var messageText = <?php echo json_encode($messageText); ?>;
    var messageNr = <?php echo json_encode($messageNr, JSON_NUMERIC_CHECK); ?>;
    var playerNr = <?php echo json_encode($playerNr, JSON_NUMERIC_CHECK); ?>;
    var path = "../";

    if (messageNr == 4 || messageNr == 6) {
        var participationFee = getParameter('participationFee');
        var period = getValue('core','playerNr=' + playerNr, 'period');
        var randomid = getValue('session', 'playerNr=' + playerNr, 'randomidNotPlayed');
//        alert(randomid);
        if (messageNr == 4) setValue('core', 'playerNr=' + playerNr, 'onPage', 'TERMINATED');
        if (messageNr == 6) setValue('core', 'playerNr=' + playerNr, 'onPage', 'GROUP ABORTED');

        setValue('core', 'playerNr=' + playerNr, 'connected', 0);

        setValue('session', 'playerNr=' + playerNr, 'relevantRandomid', randomid);
        if (messageNr == 4) setValue('session', 'playerNr=' + playerNr, 'bonusAmount', 0);
        if (messageNr == 6) {
            var bonus = 0;
            for (var i = 1; i <= period; i++) {
                bonus = bonus + getInt('decisions', 'playerNr=' + playerNr + ' and period=' + i, 'payoffThisPeriod');
            }
            setValue('session', 'playerNr=' + playerNr, 'bonusAmount', bonus);
        }

        setValue('session', 'playerNr=' + playerNr, 'participationAmount', participationFee);

        setValue('session', 'playerNr=' + playerNr, 'totalEarnings', participationFee);
    }

    if (messageNr == 5) {

        /* log that this player is excluded */
        var logMessage = 'Player ' + playerNr + ' was excluded due to timeout.';
        var time1 = getServerTime();

        insertRecord('logEvents', "playerNr, timeEvent", [playerNr, time1]);
        setValue('logEvents', 'playerNr=' + playerNr + ' and timeEvent=' + time1, 'event', logMessage);
        setValue('core', 'playerNr=' + playerNr, 'leftExperiment', 1);

    }

    if (messageNr == 8) {

        /* log that this player is excluded */
        var logMessage = 'Player ' + playerNr + ' was excluded due to quiz fail.';
        var time1 = getServerTime();

        insertRecord('logEvents', "playerNr, timeEvent", [playerNr, time1]);
        setValue('logEvents', 'playerNr=' + playerNr + ' and timeEvent=' + time1, 'event', logMessage);
        setValue('core', 'playerNr=' + playerNr, 'leftExperiment', 1);

    }

</script>
<?php
$suchmuster = '/(\$)([.a-zA-Z0-9_]*)(\$)/';

$output = preg_replace_callback(
    $suchmuster,
    function ($treffer) {

        return '<script>document.write(' . $treffer[2] . ')</script>';

    },
    $messageText);
echo '<div class="alert alert-warning" style="text-align: center; margin-top: 50px;">';

echo html_entity_decode($output);

echo '</div>'

?>

</body>

</html>
