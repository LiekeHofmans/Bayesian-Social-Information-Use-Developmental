<?php
include("../common.php");
include("../sqlLibrary.php");
$playerNr = $_POST['playerNr'];

if ($_POST['readonly'] != 1) {
    $failures = getValue("session", "playerNr=$playerNr", "quizFail");
    setValue("session", "playerNr=$playerNr", "quizFail", ($failures + 1));

    if ($_POST['wronganswers'] != null) {

        foreach ($_POST['wronganswers'] as $label => $wasfalse) {
            if ($wasfalse == 1) {
                $failures_this = getValue("session", "playerNr=$playerNr", $label . "_fail");
                setValue("session", "playerNr=$playerNr", $label . "_fail", ($failures_this + 1));
            }
        }


    }


}


echo getValue("session", "playerNr=$playerNr", "quizFail");
