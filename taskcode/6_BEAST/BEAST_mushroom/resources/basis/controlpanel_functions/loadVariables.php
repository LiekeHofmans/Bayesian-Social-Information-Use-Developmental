<?php
include('../common.php');
include('../sqlLibrary.php');

$table_name = $_REQUEST['tableName'];
$conn = mysqli_connect(HOST, ADMIN, PASSW, DBNAME) or die(mysqli_error($conn));

$sql = "SELECT * FROM $table_name";// ORDER BY playerNr ASC";
$result = mysqli_query($conn, $sql) or die("Couldn't execute query " . $sql);
$numberOfVariables = mysqli_num_fields($result);
$varNames = [];
for ($i = 0; $i < $numberOfVariables; ++$i) {
    $varNames[] = mysqli_fetch_field_direct($result, $i)->name;
}
//	$colData = [];
//	while($r = mysqli_fetch_assoc($result)) {$colData[] = array_values($r);}

$shortCol = [];
for ($i = 0; $i < count($varNames); $i++) {
    if (substr($varNames[$i], 0, 5) != 'wait_' && substr($varNames[$i], -5, 5) != 'Ready') $shortCol[] = $varNames[$i];
}
echo json_encode($shortCol);
