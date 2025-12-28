<?php
include('../common.php');
include('../sqlLibrary.php');
$tableName = $_POST['tableName'];
$condition = $_POST['condition'];
$varName = $_POST['varName'];
$value = getValue($tableName, $condition, $varName);
echo json_encode($value, JSON_NUMERIC_CHECK);
