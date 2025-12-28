<?php
// record time on server (if client is still active)
include('../common.php');
include('../sqlLibrary.php');
$playerNr = $_POST['playerNr'];
echo updateLastActionTime($playerNr);