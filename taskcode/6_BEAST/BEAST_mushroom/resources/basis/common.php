<?php
/**
 * Created by PhpStorm.
 * User: GIAMAT01
 * Date: 10.05.2016
 * Time: 11:04
 */

/*
 * SESSION WRITING BEGIN
 */
$session_prefix = 'mysid';
$session_index = isset($_REQUEST['session_index']) ? $_REQUEST['session_index'] : 0;
$active_sessions = [];

foreach ($_COOKIE as $name => $sid) {
    $zerlegtes = explode('_', $name);
    if (2 === count($zerlegtes)) {
        list($prefix, $index) = $zerlegtes;
        if ($session_prefix == $prefix)
            $active_sessions[$index] = $sid;
    }
}

if (!empty($_REQUEST['newsession'])) {

    do {
        $index = mt_rand();
    } while (isset($active_sessions[$index]));
    $session_index = md5($index);
}


session_name($session_prefix . '_' . $session_index);
ini_set('session.gc_probability', '0');
ini_set("session.gc_maxlifetime",60 * 60 * 24 * 365);
session_start();
output_add_rewrite_var('session_index', $session_index);
$_SESSION['sessionID'] = $session_index;
/*
 * SESSION WRITING END
 */
define('IPTEST', '');

if (!defined("PROJECTID")) {
    if (isset($_GET['projectID'])) define("PROJECTID", $_GET['projectID']);
    elseif (isset($_SESSION['projectID'])) define("PROJECTID", $_SESSION['projectID']);
    else echo "PROJECTID NOT DEFINED!";
}
ini_set('display_errors', 1);
error_reporting(E_ERROR | E_PARSE);

if (file_exists('../../credentials.php')) include('../../credentials.php');
elseif (file_exists('../../../credentials.php')) include('../../../credentials.php');
else include('credentials.php');

include_once('classes/liondb.class.php');
include_once('classes/liondb_legacy.class.php');
include_once('classes/helper.class.php');


