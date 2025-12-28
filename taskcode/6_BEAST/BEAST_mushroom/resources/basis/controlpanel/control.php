<?php
$path = PATH . 'basis/';
include($path . 'classes/login.class.php');
include($path . 'sqlLibrary.php');
require(PATH . 'pagination/Pagination.class.php');

if (isset($_GET['logout'])) {
    LoginLioness::logout(null, '_beginControl.php');
}


$idRun = 0;
/** NEW FUNCTIONALITY NOT YET USED
$idRun = getCurrentRun(GAMEID, COURSEID);
if ($idRun === 0) {
    $noinclude = true;
    include($path . 'controlpanel_functions/createNewRun.php');
    $idRun = getCurrentRun(GAMEID, COURSEID);
}
$_SESSION['idRun'] = $idRun;


$select = "SELECT value FROM globals WHERE idRun=" . $idRun . " AND name LIKE BINARY 'compiled' LIMIT 1";
$compiled = liondb::getInstance()->query($select)->fetch(PDO::FETCH_ASSOC)['value'];
$data = file_get_contents('_globals.json');
if ($data === false) {
    echo helper::errormessage("_globals.json could not be read");
    $_SESSION['globals'] = [];
} else $_SESSION['globals'] = (Object)json_decode($data);
if ($_SESSION['globals']->compiled != $compiled) {
    liondb::getInstance()->insertOrUpdate('globals', $idRun, ['name'], 'value', (array) $_SESSION['globals']);
}
**/

/*
 * SQL MODE LEGACY
 */
$conn = mysqli_connect(HOST, ADMIN, PASSW, DBNAME) or die(mysqli_error($conn));
/* disable strict mode in mysql if enabled (for example google cloud computing)*/
$sql = 'SELECT @@GLOBAL.sql_mode;';
$result = @mysqli_query($conn, $sql) or die("Couldn't execute query " . $sql);
$originalResult = explode(",", mysqli_fetch_array($result)[0]);
$result = array_diff($originalResult, ["STRICT_TRANS_TABLES"]);
$result = array_diff($result, ["STRICT_ALL_TABLES"]);
$originalResult = implode(",", $originalResult);
$result = implode(",", $result);
if (strlen($originalResult) != strlen($result)) {
    $sql = 'set GLOBAL sql_mode = "' . $result . '"';
    if (!mysqli_query($conn, $sql)) {
        printf("Errormessage: %s\n", mysqli_error($conn));
    }
}


$page = new Pagination(PATH);

echo $page->getHead();

$pw = defined('PROJECTPW') ? PROJECTPW : -1;


if (LoginLioness::checkValidity($pw)) {
    ?>

    <script>

        var controllerAlgWorker;

        function registerControllerAlgWorker() {
            if (typeof (Worker) !== "undefined") {
                if (typeof (controllerAlgWorker) == "undefined") {
                    controllerAlgWorker = new Worker("controlpanel_js/callController.js");
                    controllerAlgWorker.onmessage = function (event) {
                        document.getElementById("controllerDone").innerHTML = '<font size="1">t<sub>PHP</sub>=' + event.data;
                        document.getElementById("heart").style.opacity = "0.5";
                        setTimeout(function () {
                            document.getElementById("heart").style.opacity = "1";
                        }, 500)
                    };
                    controllerAlgWorker.onerror = function (event) {
                        console.log(event.data);
                    };
                    controllerAlgWorker.postMessage("<?php echo PROJECTID;?>");
                } else {
                    console.log("Web Worker is already defined");
                }

            } else {
                alert("Sorry, your browser does not support Web Workers...");
            }
        };
        registerControllerAlgWorker();
    </script>
    </head>

    <?php

    $idExperimenter = COURSEID;
    if ($idExperimenter > 10000) $isDemo = true;
    else $isDemo = false;

    echo $page->getTopNavigation(PROJECTID, $isDemo);
    echo $page->getNavBar();
    echo $page->beginContainer();

    if ($isDemo) echo '<div class="alert alert-warning">Welcome to this LIONESS demo experiment. Please start test players (or bots) using the top horizontal bar. You can monitor the progress of the experiment below, and select the variables you wish to track by clicking \'Display options.\'</div>';

    $cookie = array_key_exists('controlbanner', $_COOKIE) ? $_COOKIE['controlbanner'] : null;
    if ($cookie != 1) {
        echo '<div id="controlbanner"><div class="alert alert-info" style="margin-bottom: 2px; margin-top: 5px;">This page controls the experimental flow. Keep this page open for the entire duration of your interactive experiment. For non-interactive experiments this page does not need to be open.</div>';
        echo '<div class="row-fluid">';
        if (!$isDemo && ($_SERVER['HTTP_HOST'] == 'lioness.uni-passau.de' || $_SERVER['HTTP_HOST'] == 'classex.uni-passau.de')) echo '<div style="padding-left: 5px; font-size: x-small; color: gray" class="span10">You are running your experiment on lioness.uni-passau.de. This server is mainly for development and testing. To prevent overload, we cap the maximum number of participants on this server to 100 per experiment. When you are finished developing and testing, and ready to run your experiment, please <a href="https://lioness-doc.readthedocs.io/en/latest/0303_set_up.html" target="_blank">download your experiment and put it on an own server</a>.</div>';
        else echo '<div class="span10"></div>';

        echo '<div class="span2" onclick="var d=new Date(); 
                    d.setTime(d.getTime() + (365*24*60*60*1000)); 
                    document.cookie=\'controlbanner=1; expires=\' + d.toUTCString(); 
                    $(\'#controlbanner\').hide();" style="cursor: pointer;  padding-right: 5px; text-align: right; color: grey; font-size: x-small">Do not show this hint again</div>';


        echo '</div></div>';
    }
    ?>


    <div class="row-fluid">


        <div id="monitor" class="span12">

            <?php
            // load the library to regulate reading from and writing to the database

            $result = mysqli_query($conn, "SHOW TABLES LIKE '" . PROJECTID . "%'");
            $tableList = [];
            while ($tables = mysqli_fetch_array($result)) $tableList[] = $tables[0];

            $stageNamesArr = $_SESSION['stageNames'];
            $stageNrs = array_keys($stageNamesArr);
            $stageNames = [];
            for ($i = 0; $i < count($stageNrs); $i++) $stageNames[] = $stageNamesArr[$stageNrs[$i]];

            //	print_r($_SESSION['stageNum']);

            ?>
            <script>
                // jQuery for browsing tables
                var tables = <?php echo json_encode($tableList); ?>;
                var stageNames = <?php echo json_encode($stageNames); ?>;
                var stageNrs = <?php echo json_encode($stageNrs); ?>;
                var projectID = <?php echo json_encode(PROJECTID); ?>;

                // upon new page entry, show first tables and its variables by default
                // also pre-select useful variables from other tables to guide new useres
                var activeTable = localStorage['activeTable'];
                if (!activeTable) {
                    activeTable = 0; // start with core table if no localStorage is found
                    localStorage['activeTable'] = 0;
                    var preselectedVars = [0, 1, 2, 6];
                    for (let i = 0; i < preselectedVars.length; i++) localStorage[projectID + 'core_tcol' + preselectedVars[i]] = 1;
                    preselectedVars = [0, 1, 3];
                    for (let i = 0; i < preselectedVars.length; i++) localStorage[projectID + 'decisions_tcol' + preselectedVars[i]] = 1;
                    preselectedVars = [0, 1, 2, 3];
                    for (let i = 0; i < preselectedVars.length; i++) localStorage[projectID + 'globals_tcol' + preselectedVars[i]] = 1;

                }
                // show the variable selection menu by default
                localStorage['varMenu'] = 1;

                // once the page is loaded, start the functions that refresh the data tables regularly so that monitoring progress is live
                $(document).ready(function () {
                    $(".tabs-menu").click(function (event) {
                        clearInterval(refreshTable);
                        event.preventDefault();

                        // if a new table is selected, update the localstorage
                        localStorage['activeTable'] = ($(this).attr("href").substr(-1));

                        // show that table
                        $(this).parent().addClass("current");
                        $(this).parent().siblings().removeClass("current");
                        var tab = $(this).attr("href");
                        //$(".tab-content").not(tab).css("display", "none");
                        $(tab).fadeIn();

                        // show the contents of that table
                        var tableName = tables[localStorage['activeTable']];
                        var tabNames = loadVariables(tableName);
                        loadVariables2(tableName);
                        loadTable();

                        // start the refreshing procedure
                        refreshTable = setInterval(function () {
                            loadTable();
                        }, 2000);
                    });
                    // make the selected variables blue in the menu (so that they look selected)
                    loadVariables2(tableName);
                    $('#li' + tableName).addClass('active');
                });


            </script>

            <div id="Monitor">
                <h3><?php echo $_SESSION['gameTitle']; ?> - Control panel</h3>
                <h6 style="color: grey;">address for
                    participants: <?php echo $_SERVER['SERVER_NAME'] . str_replace('Control', 'Participant', $_SERVER['PHP_SELF']); ?> </h6>

                <script>
                    // first display the tabs to browse through the tables
                    var l = <?php echo strlen(PROJECTID); ?>;
                    var tables = <?php echo json_encode($tableList); ?>;
                    var txt = '';
                    txt += ' <ul class="nav nav-tabs">';
                    for (var i = 0; i < tables.length; i++) txt += '<li id="li' + tables[i] + '"><a class="tabs-menu" data-toggle="tab" href="#tab-' + i + '">' + tables[i].split("_").pop() + '</a></li>';
                    txt += '</ul>';

                    txt += '<button type="button" onclick="toggleVarMenu()"><div id="button_sign" style="padding:0"> > </div></button> Display options';
                    txt += '<br clear=both>';

                    document.write(txt);
                </script>
                <!-- the variable selection box -->
                <div id="varMenu" class="alert alert-info"></div>
                <div>
                    <table id="showTableMonitor" class="table table-striped"></table>
                </div>


                <script>
                    // load the variable names from PHP
                    var tableName = tables[activeTable];
                    var tabNames = loadVariables(tableName);
                    var tableNameActive = tables[localStorage['activeTable']];

                    // function for table display
                    var showMode = 'table-cell';
                    if (document.all) showMode = 'block';

                    // initialise visible columns from cache
                    for (var i = 0; i < tabNames.length; i++) {
                        cells = document.getElementsByName(tableNameActive + '_tcol' + i);
                        var varName = localStorage.getItem(tableNameActive + '_tcol' + i);
                    }


                    document.getElementById("button_sign").innerHTML = ">";
                    document.getElementById("varMenu").style.display = "none";
                    if (localStorage['varMenu']) {
                        document.getElementById("varMenu").style.display = "block";
                        document.getElementById("button_sign").innerHTML = "v";
                    }


                    var refreshTable = setInterval(function () {
                        loadTable();
                    }, 3000);
                </script>
            </div>


        </div>
    </div>

    </div>


    <?php

    echo $page->endContainer();

} else {

    LoginLioness::displayLoginField();
}
echo $page->getBodyEnd();