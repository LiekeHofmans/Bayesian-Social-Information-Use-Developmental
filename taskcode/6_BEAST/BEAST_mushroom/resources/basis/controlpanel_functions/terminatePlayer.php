<?php
// this script can terminate a participant.
// the participant will be sent to '_experimentTerminated.php' once a new page loads
include("../common.php");
include("../sqlLibrary.php");

$playerNr = $_POST['playerNr'];
$rows = setValue("core", "playerNr='$playerNr'", "experimentTerminated", 1);
$timeNow = date('Y/m/d H:i:s');
$message = 'player ' . $playerNr . ' terminated BY EXPERIMENTER.';
insertRecord("logEvents", "groupNr, playerNr, timeEvent, event", "'0', '$playerNr', '$timeNow', '$message'");

echo json_encode($rows, JSON_NUMERIC_CHECK);
