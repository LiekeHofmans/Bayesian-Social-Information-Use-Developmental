<?php
include('../common.php');
include("../sqlLibrary.php");

$conn = mysqli_connect(HOST, ADMIN, PASSW, DBNAME);
if (mysqli_connect_errno()) {
    echo "Failed to connect to MySQL: " . mysqli_connect_error();
};// Check connection
// list tables in database
$tables = [];
$result = mysqli_query($conn, 'SHOW TABLES LIKE "' . PROJECTID . '%"');
while ($row = mysqli_fetch_row($result)) {
    $tables[] = $row[0];
}
$idLength = strlen(PROJECTID);

foreach ($tables as $table) {
    // do not empty the parameter table
    if (substr($table, 0, $idLength) == PROJECTID && $idLength > 3) {

        if (substr($table, -7, 7) != 'globals' && substr($table, -7, 7) != 'globals') {
            echo $table;
            $sql = "TRUNCATE " . $table;
            $result = @mysqli_query($conn, $sql);
        }
    }
}