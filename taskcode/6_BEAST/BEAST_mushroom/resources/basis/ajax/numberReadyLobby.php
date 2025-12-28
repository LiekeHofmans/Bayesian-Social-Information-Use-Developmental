<?php
include('../common.php');
include('../sqlLibrary.php');

$matchingProcedure = getParameter('sortableMatching');
$groupSize = getParameter('groupSize');

$role = $_POST['role'];

if ($matchingProcedure == 1) {
    $conn = mysqli_connect(HOST, ADMIN, PASSW, DBNAME) or die(mysqli_error());
    $table_name = PROJECTID . 'core';
    $sql = "SELECT playerNr FROM $table_name WHERE (lobbyReady=1 and connected=1 and LEFT(onPage,5)='lobby')";

    $result = @mysqli_query($conn, $sql) or die("Couldn't execute query " . $sql);

    echo json_encode(mysqli_num_rows($result), JSON_NUMERIC_CHECK);
}
if ($matchingProcedure == 2) {
    $conn = mysqli_connect(HOST, ADMIN, PASSW, DBNAME) or die(mysqli_error());
    $table_name = PROJECTID . 'core';
    $sql = "SELECT role FROM $table_name WHERE (lobbyReady=1 and connected=1 and LEFT(onPage,5)='lobby')";
    $result = @mysqli_query($conn, $sql) or die("Couldn't execute query " . $sql);
    $roleList = [];
    while ($row = mysqli_fetch_assoc($result)) {
        $roleList[] = $row['role'];
    }
    $effectivelyReady = 0;
    for ($i = 1; $i <= $groupSize; $i++) {
        if (in_array($i, $roleList)) $effectivelyReady++;
    }
    echo json_encode($effectivelyReady, JSON_NUMERIC_CHECK);
}
if ($matchingProcedure == 3) {
    $conn = mysqli_connect(HOST, ADMIN, PASSW, DBNAME) or die(mysqli_error());
    $table_name = PROJECTID . 'core';
    $sql = "SELECT playerNr FROM $table_name WHERE (lobbyReady=1 and connected=1 and LEFT(onPage,5)='lobby' and role=$role)";

    $result = @mysqli_query($conn, $sql) or die("Couldn't execute query " . $sql);
    echo json_encode(mysqli_num_rows($result), JSON_NUMERIC_CHECK);
}

