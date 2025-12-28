<?php

include('_projectID.php');
error_reporting(E_ERROR | E_PARSE);
#reset opcache so credentials.php is read if just created
if (function_exists("opcache_reset")) {
    opcache_reset();
}
$phpversion = explode('.', phpversion());
if ($phpversion[0] < 7 && $phpversion[1] < 1) echo '<div class="alert alert-warning">You are using a PHP version lower than 7.1, which may cause errors. Please use an up-to-date PHP version. At least 7.1.</div>';

function showHeader()
{

    echo ' <html>
        <head>
            <link href="resources/basis/css/newlayout.css" rel="stylesheet" type="text/css"/>
            <link href="resources/basis/css/newlayout_bootstrap.css" rel="stylesheet" type="text/css"/>
            <link href="resources/basis/css/grid.css" rel="stylesheet" type="text/css"/>
        </head>
        <body><div class="main" style="left: 25%; width: 663px"><div class="btnbox2" style="text-align: left;"><img src="resources/pagination/pic/lionlogo.svg" width="100px"></div>';
}

function showFooter()
{

    echo '</div></body>
        </html>';

}

function alertMessage($text, $headershow = true)
{

    if ($headershow) showHeader();

    echo '<div class="alert alert-warning">' . $text . '</div>';

    if ($headershow) showFooter();

}


function showConfirmer($text, $confirmerid)
{


    showHeader();
    alertMessage($text, false);
    echo '<div><form method="POST" action="controlpanel.php"><div class="form-group"> <button type="submit" class="btn btn-large btn-primary">CONFIRM</button>
                <input name="' . $confirmerid . '" type="hidden"
                       value="1"></div></form>';
    showFooter();


}

if (!file_exists('ENABLESETUP.php')) header('Location: _beginControl.php');

if (array_key_exists('send', $_POST) && $_POST['send'] == 1) {
    $content = '<?php
	// first define the host, the database name, the username (admin), and the password
	define ("HOST","' . $_POST['host'] . '");
	define ("ADMIN","' . $_POST['admin'] . '");
	define ("DBNAME","' . $_POST['dbname'] . '");
	define ("PASSW","' . $_POST['passw'] . '");
	define("DNS", "mysql:dbname=".DBNAME.";host=".HOST);
    define("DNS_LEGACY", "mysql:dbname=".DBNAME.";host=".HOST);
	    ';

    if (!file_put_contents('credentials.php', $content)) {
        alertMessage(' <b>Credentials could not be written.</b> Permission to edit/write credentials.php is missing.<br>
            If you are using Bitnami give all users the right to read and write credentials.php.
            In Filezilla, find the file <i>credentials.php</i> in the folder of your experiment.
            Right-click on this file, and select <i>File permissions...</i>.
            A dialog box will open. Make sure that the <i>Read</i> and <i>Write</i> boxes are checked for <i>Public
                permissions</i>.<br>
            Once you have given these writing permissions to credentials.php, please refresh this screen and try
            again!<br>
            For more information please refer to the
            <a href="https://lioness-doc.readthedocs.io/en/latest/0303_set_up.html#set-up-your-database-and-lioness-tables"
               target="_blank">documentation!</a>
            If you require further help, please refer to the <a
                    href="https://groups.google.com/forum/#!forum/lioness-lab" target="_blank"> forum.</a>.
        ');
        die();
    }

}
if (!file_exists('credentials.php')) {
    $writer = fopen('credentials.php', 'w');
    if (!$writer) {
        alertMessage('   <b>Credentials could not be written.</b> Permission to create credentials.php in the game folder is missing.<br>
            If you are using Bitnami give all users the right to read and write into the game folder recursively.
            In Filezilla, find the folder of your experiment.
            Right-click on this folder, and select <i>File attributes...</i>.
            A dialog box will open. Make sure that the <i>Read</i> and <i>Write</i> boxes are checked for <i>Public
                permissions</i>.
            Also make sure that <i>Recurse into subdirectories</i> is checked.<br>
            Once you have given these writing permissions to credentials.php, please refresh this screen and try
            again!<br>
            For more information please refer to the
            <a href="https://lioness-doc.readthedocs.io/en/latest/0303_set_up.html#set-up-your-database-and-lioness-tables"
               target="_blank">documentation!</a>
            If you require further help, please refer to the <a
                    href="https://groups.google.com/forum/#!forum/lioness-lab" target="_blank"> forum.</a>.
        ');
        die();
    } else {
        //write empty credentials file here
        fwrite($writer, '<?php 
    define ("HOST","localhost");
	define ("ADMIN","root");
	define ("DBNAME","lionessdb");
	define ("PASSW","");
	define("DNS", "mysql:dbname=".DBNAME.";host=".HOST);
    define("DNS_LEGACY", "mysql:dbname=".DBNAME.";host=".HOST);');
        fclose($writer);
    }
}

include('credentials.php');

$conn = mysqli_connect(HOST, ADMIN, PASSW, DBNAME);

if (!$conn) {
    $error = mysqli_connect_errno();
    if ($error == 1049 && DBNAME != '') {

        if ($_POST['createDBconfirm'] != 1) {

            showConfirmer("There is no database with the name " . DBNAME . " yet. 
                LIONESS Lab wants to create one. Please confirm.", "createDBconfirm");
            die();

        } else {
            $conn2 = mysqli_connect(HOST, ADMIN, PASSW);
            $sql = "CREATE DATABASE " . DBNAME;
            $result = mysqli_query($conn2, $sql);
            $conn_new = true;
        }

    }

}


if ($conn_new) $conn = mysqli_connect(HOST, ADMIN, PASSW, DBNAME);


if (!$conn || HOST == '' || DBNAME == '' || ADMIN == '') {

    if (DBNAME == '') $dbname = 'lionessdb';
    else $dbname = DBNAME;
    if (HOST == '') $host = 'localhost';
    else $host = HOST;
    if (ADMIN == '') $admin = 'root';
    else $admin = ADMIN;


    showHeader();


    echo '<div class="row-fluid" style="margin-left:50px;margin-right:50px;">
        <div class="span1"></div>
        <div class="span4">
            <h3>Login Data for DB</h3>
            <div class="alert alert-danger">
                LIONESS cannot connect to the database, as it has not been created yet. <br>Please check whether your
                credentials are filled out correctly and press submit to generate the database.<br>
                If you are using the Bitnami Launchpad, you can find your password in the <i>Application Info</i> of
                your LAMP stack, in the field <i>Credentials</i>.<br>
                For the other fields LIONESS tried to add sensible default values.
                For more information please refer to the
                <a href="https://lioness-doc.readthedocs.io/en/latest/0303_set_up.html#set-up-your-database-and-lioness-tables"
                   target="_blank">documentation!</a><br>
                </div>
            <form method="post">
                <div class="form-group">
                    <label for="field1">Hostname</label>
                    <input name="host" id="field1"
                           type="text"
                           value="' . $host . '"
                           class="form-control input-lg" style="text-align: center;">
                </div>
                <div class="form-group">
                    <label for="field2">Username</label>
                    <input name="admin" id="field2"
                           type="text"
                           value="' . $admin . '"
                           class="form-control input-lg" style="text-align: center;">
                </div>
                <div class="form-group"><label for="field3">Password</label>
                    <input name="passw" id="field3"
                           type="text"
                           value="' . PASSW . '"
                           class="form-control input-lg" style="text-align: center;">
                </div>
                <div class="form-group">
                    <label for="field4">Database</label>
                    <input name="dbname" id="field4"
                           type="text"
                           value="' . $dbname . '"
                           class="form-control input-lg" style="text-align: center;">
                </div>
                <button type="submit" class="btn btn-primary">Submit</button>
                <input name="send" type="hidden"
                       value="1">
            </form>
        </div>
    </div>';


    showFooter();

} else {
    $compiled = false;
    $sql2 = "SHOW TABLES ";
    $result = mysqli_query($conn, $sql2);
    $correctab = 0;
    while ($row = mysqli_fetch_array($result, MYSQLI_NUM)) {

        if ($row[0] == PROJECTID . 'core') $correctab++;
        if ($row[0] == PROJECTID . 'globals') $correctab++;
        if ($row[0] == PROJECTID . 'decisions') $correctab++;
        if ($row[0] == PROJECTID . 'session') $correctab++;
        if ($row[0] == PROJECTID . 'logEvents' || $row[0] == PROJECTID . 'logevents') $correctab++;
    }
    if ($correctab >= 5) $compiled = true;
    if ($compiled) {
        header('Location: _beginControl.php');
    } else {

        if ($_POST['confirmSetupTables'] != 1) {

            showConfirmer("The tables for this experiment have not been set up yet 
            (or not been set up completely). Clicking confirm will destroy all old tables of this experiment.", "confirmSetupTables");

        } else {


            $sql = file_get_contents('setup_tables.sql');
            $lines = explode(';SELECT 1;', $sql);
            foreach ($lines as $line) {
                $result = mysqli_query($conn, $line);
            }
            header('Location: _beginControl.php');

        }
    }


}
