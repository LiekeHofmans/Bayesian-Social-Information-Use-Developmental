<?php
/**
 * Created by PhpStorm.
 * User: marcusgia
 * Date: 23.04.2019
 * Time: 09:24
 */
if (!(isset($noinclude) && $noinclude)) {
    include('../common.php');
    include('../sqlLibrary.php');
}

$idRun = getCurrentRun(GAMEID, COURSEID);

if ($idRun != 0) {
    /* end old run */
    $update = "UPDATE run SET stop = CURRENT_TIMESTAMP() WHERE idRun = " . $idRun;
    liondb::getInstance()->exec($update);

}

$insert = "INSERT INTO run (idGame, idCourse) VALUES (" . GAMEID . "," . COURSEID . ");";
$result = liondb::getInstance()->exec($insert);
$idRun = liondb::getInstance()->lastInsertID();
