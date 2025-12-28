<?php
include('../common.php');
include('../sqlLibrary.php');
$tableName = $_POST['tableName'];
$condition = $_POST['condition'];
$varName = $_POST['varName'];
$sortBy = $_POST['sortBy'];
$values = getValues($tableName, $condition, $varName, $sortBy);
echo json_encode($values, JSON_NUMERIC_CHECK);