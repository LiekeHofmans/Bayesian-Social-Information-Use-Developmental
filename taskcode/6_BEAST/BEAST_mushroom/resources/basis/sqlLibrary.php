<?php

/**
 * @deprecated: replaced by getValue
 **/
function getParameter($name)
{
    return getValue("globals", "name='" . $name . "'", "value");
}


/**
 * Retrieves a variable from a specific record
 * example: $previousDecision=getValue("decisions","playerNr='$playerNr' and period='$period-1'","decision");
 **/
function getValue($table_name, $condition, $name)
{
    $table_name = sanitizeTableNames($table_name);
    $table_name_server = PROJECTID . $table_name;
    $sql = "SELECT $name FROM $table_name_server WHERE ($condition)";
    $result = liondb_leg::getInstance()->query($sql);
    if ($row = $result->fetch(PDO::FETCH_ASSOC)) {
        $value = $row[$name];
    } else $value = "";
    return $value;
}


//Retrieves an array of variables from a specific record
function getValues($table_name, $condition, $name, $sortBy)
{//example: $previousDecision=getValues("decisions","groupNr='$groupNr' and period='$period-1'","decision");
    $table_name = sanitizeTableNames($table_name);
    $table_name_server = PROJECTID . $table_name;

    $sql = "SELECT $name FROM $table_name_server WHERE ($condition) ORDER BY ($sortBy) ASC";
    $result = liondb_leg::getInstance()->query($sql);
    $values = [];
    while ($row = $result->fetch(PDO::FETCH_ASSOC)) {
        $values[] = $row[$name];
    }
    return $values;
}


//inserts new record in table
//example: insertRecord("decisions","playerNr, period, decision","\"$playerNr\", \"$period\", \"$decision\" ");
function insertRecord($table_name, $names, $values)
{
    $table_name = sanitizeTableNames($table_name);
    $table_name_server = PROJECTID . $table_name;

    $sql = "INSERT INTO $table_name_server (" . $names . ") VALUES (" . $values . ")";
    if (preg_match('/"/', $names) > 0) $mod_names = str_getcsv($names, ",", "\"");
    else $mod_names = str_getcsv($names, ",", "'");
    if (preg_match('/"/', $names) > 0) $mod_values = str_getcsv($values, ",", "\"");
    else $mod_values = str_getcsv($values, ",", "'");
    $update_values = [];
    foreach ($mod_names as $key => $val)
        array_push($update_values, $val . "='" . $mod_values[$key], "'");
    $sql .= " ON DUPLICATE KEY UPDATE " . implode(',', $update_values);

    return liondb_leg::getInstance()->exec($sql);
}

//Updates a variable in a record
function setValue($table_name, $condition, $name, $value)
{
    $table_name = sanitizeTableNames($table_name);
    $table_name_server = PROJECTID . $table_name;

    $sql = "UPDATE $table_name_server SET `$name`=\"$value\" WHERE ($condition)";
    return liondb_leg::getInstance()->exec($sql);

}

/**
 *
 * THIS FUNCTION IS ONLY USED BY THE CONTROLLER ALGORITH
 * @deprecated
 * the escape sequence \" needs to be added when you want to pass a string to this function
 **/
function setValues($table_name, $condition, $updatestring)
{
    $table_name = sanitizeTableNames($table_name);
    $sql = "UPDATE " . PROJECTID . $table_name . " SET " . $updatestring . " WHERE ($condition)";
    return liondb_leg::getInstance()->exec($sql);

}

function resetWaitingValues($playerNr)
{

    $sql = "SHOW COLUMNS FROM " . PROJECTID . "core";
    $result = liondb_leg::getInstance()->query($sql);
    $allVars = [];

    while ($row = $result->fetch(PDO::FETCH_ASSOC)) {
        $allVars [] = $row['Field'];
    }
    $clause = "playerNr=" . $playerNr;
    for ($i = 0; $i < count($allVars); $i++) {
        if (substr($allVars[$i], 0, 5) == 'wait_') {
            setValue("core", $clause, $allVars[$i], 0);
        }
    }
}


function readcookie($variable)
{
    $cookie_val = $_COOKIE[$variable];
    return explode("-", $cookie_val);
}

function updateLastActionTime($playerNr)
{
    return liondb_leg::getInstance()->prepareAndExecute("UPDATE " . PROJECTID . "core SET lastActionTime = " . time() . " WHERE playerNr= ?", [$playerNr]);
}


function getCurrentRun(int $idGame, int $idCourse)
{
    $select = "SELECT idRun FROM run WHERE idGame=" . $idGame . " AND idCourse=" . $idCourse . " AND stop IS NULL ORDER BY idRun LIMIT 1";
    $result = liondb::getInstance()->query($select);
    if ($result->rowCount() > 0) return $result->fetch(PDO::FETCH_ASSOC)['idRun'];
    else return 0;

}

function sanitizeTableNames($tableName)
{

    $allowedTableNames = ['core', 'decisions', 'globals', 'session', 'logEvents'];
    if (in_array($tableName, $allowedTableNames)) return $tableName;
    else return '';

}