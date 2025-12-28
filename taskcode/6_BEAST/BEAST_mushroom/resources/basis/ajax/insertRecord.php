<?php
include('../common.php');
include('../sqlLibrary.php');
$tableName = $_POST['tableName'];
$varNames = json_decode(stripslashes($_POST['varNames']));
$values = json_decode(stripslashes($_POST['values']));
insertRecord($tableName, $varNames, $values);
