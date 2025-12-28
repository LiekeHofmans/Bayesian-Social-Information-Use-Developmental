<?php
include('../common.php');
include("../sqlLibrary.php");

$conn = mysqli_connect(HOST, ADMIN, PASSW, DBNAME) or die(mysqli_error());
mysqli_set_charset ($conn, "utf8");
$result = mysqli_query($conn, "SHOW TABLES");
$tableList = [];
$defaultOrder = ['core' => 'playerNr', 'decisions' => 'playerNr', 'globals' => 'name', 'logEvents' => 'eventNr', 'logEvents' => 'eventNr', 'session' => 'playerNr'];
$timestamps = ['lastActionTime','tStart'];
while ($tables = mysqli_fetch_array($result)) $tableList[] = $tables[0];

//	print_r($_SESSION['stageNames']);

//	$table_name="core";	
$sql = "SELECT ";
$txt = '';
$table_name = $_GET['tableName'];
$numColsRequested = $_GET['n'];
$orderBy = $_GET['orderBy'];
$ascOrDesc = $_GET['ascOrDesc'];
$table_name_wo_prefix = explode('_', $table_name)[1];

if ($numColsRequested > 0) {
    for ($i = 0; $i < $numColsRequested; $i++) {
        $varName = '`'.$_GET['q' . $i].'`';
        if (in_array($varName, $timestamps)) $sql .= 'FROM_UNIXTIME('.$varName.')';
        else $sql .= $varName;
        if ($i < ($numColsRequested - 1)) $sql .= ', ';
    }
    $sql .= " FROM $table_name";
    if ($orderBy != 'undefined') {
        $sql .= " ORDER BY " . $orderBy;
        if ($ascOrDesc == '0') $sql .= " ASC";
        else $sql .= " DESC";
        $sql .= ", " . $defaultOrder[$table_name_wo_prefix] . " ASC ";
    } else {
        $sql .= " ORDER BY " . $defaultOrder[$table_name_wo_prefix];
    }

    $result = mysqli_query($conn, $sql) or die("Couldn't execute query " . $sql);
    $colData = [];
    while ($r = mysqli_fetch_assoc($result)) {
        $colData[] = array_values($r);
    }

    // set up the headers
    $txt .= '<table cellpadding="1" cellspacing="1" class="sortable"><thead><tr>';
    $columns = count($colData);
    for ($i = 0; $i < $numColsRequested; $i++) {
        $txt .= '<th align=center>';
        $varName = $_GET['q' . $i];
        if (substr($varName, 0, 5) == 'time_') {
            $stageNr = substr($varName, 5);
            $val = $_SESSION['stageNames'][$stageNr];
            $varName = 'time_' . $val;
        }
        $txt .= $varName;
        $txt .= '</th>';
    }
    $txt .= '</tr></thead><tbody>';

    for ($i = 0; $i < $columns; $i++) {
        $txt .= "<tr>";
        $rows = count($colData[$i]);
        for ($j = 0; $j < $rows; $j++) {
            $val = $colData[$i][$j];


            if (substr($val, 0, 5) == 'stage') {
                $idStage = substr($val, 0, -4);
                $idStage = substr($idStage, 5);
                $val = "*** " . $_SESSION['stageNames'][$idStage] . " *** ";

                //		$val = $idStage;
            } elseif ($val == 'lobby' || $val == 'lobby.php') $val = '*** lobby ***';
            elseif (substr($val, 0, 4) == 'wait') {
                $idStage = substr($val, 0, -4);
                $idStage = substr($idStage, 4);
                $val = "- " . $_SESSION['stageNames'][$idStage] . " - ";
                //		$val = $idStage;
            }

            $txt .= "<td align=center>" . $val . "</td>";
        }
        $txt .= "</tr>";
    }
    $txt .= "</tbody></table>";
}
echo $txt;
