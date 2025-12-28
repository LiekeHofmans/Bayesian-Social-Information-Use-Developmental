<?php
include('../common.php');
include('../sqlLibrary.php');

$tableName = $_POST['tableName'];
$condition = $_POST['condition'];
$condition = str_replace("+", " ", $condition);
$varName = $_POST['varName'];
$value = $_POST['value'];
setValue($tableName, $condition, $varName, $value);
