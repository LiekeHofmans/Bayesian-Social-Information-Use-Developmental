<?php
include('../common.php');
include("../sqlLibrary.php");

// make connection to the server
$conn = mysqli_connect(HOST, ADMIN, PASSW, DBNAME) or die(mysqli_error());
mysqli_set_charset ($conn, "utf8");
// get the stage names for displaying the time_ variables correctly
$stageNamesArr = $_SESSION['stageNames'];
$stageNrs = array_keys($stageNamesArr);
$stageNames = [];
for ($i = 0; $i < count($stageNrs); $i++) $stageNames[] = $stageNamesArr[$stageNrs[$i]];


// get session time for file name
$sessionTime = date('Ymd') . '_' . date('Hi');
$gameTitle = $_SESSION['gameTitle'];
// read data from server
$idLength = strlen(PROJECTID);
$tables = [];
$result = mysqli_query($conn, 'SHOW TABLES');
while ($row = mysqli_fetch_row($result)) {
    if (substr($row[0], 0, $idLength) == PROJECTID) $tables[] = $row[0];
}

// store data in these containers
$tableNameContainer = [];
$headerContainer = [];
$dataContainer = [];

// loop through all tables
foreach ($tables as $table) {
    $table_name = $table;
    $table_type = explode("_", $table_name)[1]; // core decision globals session logEvents
    $tableNameContainer[] = $table_type;
    $sql = "SELECT * FROM $table_name";
    $result = @mysqli_query($conn, $sql) or die("Couldn't execute query " . $sql);
    $row = mysqli_fetch_assoc($result);

    // get the header names and store them in their container
    $headerNames = [];
    if ($row) {

        $columnTitles = array_keys($row);
        foreach ($columnTitles as $field) {
            // check if the name of the field is 'time_'
            if (substr($field, 0, 5) == 'time_') {
                $stageNr = substr($field, 5);
                if ($stageNamesArr[$stageNr] !== null && trim($stageNamesArr[$stageNr]) != '')
                    $field = 'time_' . $stageNamesArr[$stageNr];
                else  $field = 'time_' . $stageNr;
            }
            $numbers = array_count_values($headerNames);
            /* PROBLEM DOUBLE STAGE NAMES
            * to prevent this check if already in array
            * problem appears later when array_fill_keys makes values to keys and does not allow for duplicate keys.
            */
            if ($numbers[$field] > 0) array_push($headerNames, $field . '_' . $numbers[$field]);
            else array_push($headerNames, $field);
        }
    }
    $headerContainer[] = array_fill_keys($headerNames, 'string');

    // get the data for each of the variables and store them in their container
    $dat = [[]];
    while ($row) {
        $newRow = [];
        foreach ($row as $key => $field) {

            if ($key == 'onPage' && $table_type == 'core') {
                if ($field == 'lobby' || $field == 'lobby.php')
                    $field = 'lobby';
                else {
                    $stgNr = substr($field, 5, -4);

                    if ($stageNamesArr[$stgNr] !== null && trim($stageNamesArr[$stgNr]) != '')
                        $field = $stageNamesArr[$stgNr];
                }

            }
            array_push($newRow, $field);
        }
        array_push($dat, $newRow);
        $row = mysqli_fetch_assoc($result);
    }
    $dataContainer[] = $dat;
}


// read the data for the payment file (written to a separate sheet)
$paymentFileHeaders = [];
$paymentFileData = [[]];
$table_name = PROJECTID . "session";
$sql = "SELECT playerNr, relevantRandomid, participationAmount, bonusAmount, totalEarnings FROM $table_name ORDER BY totalEarnings DESC, relevantRandomid DESC";
$result = @mysqli_query($conn, $sql) or die("Couldn't execute query " . $sql);
$row = mysqli_fetch_assoc($result);

if ($row) {
    $columnTitles = array_keys($row);
    foreach ($columnTitles as $field) {
        array_push($paymentFileHeaders, $field);
    }
    array_push($paymentFileHeaders, "assignmentID", "workerID", "bonusMessage", "MTurkPaymentCode", "ProlificPaymentCode");
    $paymentFileHeaders = array_fill_keys($paymentFileHeaders, 'string');
    // get the data for each of the variables and store them in their container
    $dat = [[]];
    $cnt = 2;
    $bonusMessage = 'Thank you for participating in our study. Please note that your guaranteed participation fee is paid separately upon approval of your task.'; // this should be specified alongside the standard texts for 'external pages'
    while ($row) {
        $newRow = [];
        foreach ($row as $field) {
            array_push($newRow, $field);
        }

        // add the Excel commands for matching the MTurk worker IDs with the LIONESS random IDs to calculate bonuses
        array_push($newRow, '=INDEX(batchResults!$O:$O, MATCH($B' . $cnt . ', batchResults!$AB:$AB, 0))'); // assignment ID;
        array_push($newRow, '=INDEX(batchResults!$P:$P, MATCH($B' . $cnt . ', batchResults!$AB:$AB, 0))'); // worker ID
        array_push($newRow, $bonusMessage);
        array_push($newRow, '="aws mturk send-bonus --worker-id " & $G' . $cnt . '& " --bonus-amount " & $D' . $cnt . ' & " --assignment-id " & $F' . $cnt . ' & " --reason " & CHAR(34) & $H' . $cnt . ' & CHAR(34)'); // the DevTools code;
        array_push($newRow, '=VLOOKUP($A' . $cnt . ', session!$A:$E, 5, FALSE) & "," & D' . $cnt);

		array_push($dat, $newRow);
        $row = mysqli_fetch_assoc($result);
        $cnt++;
    }

    $paymentFileData = $dat;
}


// write to the Excel file
include_once("xlsxwriter.class.php");

$filename = "LIONESS Results - " . $gameTitle . " " . $sessionTime . ".xlsx";

header('Content-disposition: attachment; filename="' . XLSXWriter::sanitize_filename($filename) . '"');
header("Content-Type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet");
header('Content-Transfer-Encoding: binary');
header('Cache-Control: must-revalidate');
header('Pragma: public');

$writer = new XLSXWriter();
$writer->setAuthor('LIONESS Lab');

for ($i = 0; $i < count($headerContainer); $i++) {
    $writer->writeSheet($dataContainer[$i], $tableNameContainer[$i], $headerContainer[$i]);
}
// write payment tab
$writer->writeSheet($paymentFileData, 'payments', $paymentFileHeaders);

// write placeholder tab to paste MTurk Batch Results into
$emptyData = [[]];
$placeholder = [];
array_push($placeholder, "Paste your MTurk Batch Results here (cell A1). Then view the payment codes in the Excel tab 'paymentsMTurk', check them and paste column I ('MTurkPaymentToolsCode') into Amazon Command Line Tools to make your bonus payments");
array_push($emptyData, $placeholder);

$writer->writeSheet($emptyData, 'batchResults');
$writer->writeToStdOut();

