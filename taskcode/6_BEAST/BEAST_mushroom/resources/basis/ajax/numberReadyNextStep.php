<?php
include('../common.php');
include('../sqlLibrary.php');
$table_name = PROJECTID . 'core';


$playerNr = $_POST['playerNr'];

$groupNr = getValue("core", "playerNr=$playerNr", "groupNr");
$thisPage = getValue("core", "playerNr=$playerNr", "onPage");
$waitingPageNr = substr($thisPage, 4);
$waitingPageNr = explode('.', $waitingPageNr);
$controllerVarName = 'wait_' . $waitingPageNr[0] . 'ready';

$sql = "SELECT playerNr FROM $table_name WHERE groupNr = ? and $controllerVarName=1";
$result = liondb_leg::getInstance()->prepareAndCount($sql, [$groupNr]);
echo json_encode($result, JSON_NUMERIC_CHECK);
