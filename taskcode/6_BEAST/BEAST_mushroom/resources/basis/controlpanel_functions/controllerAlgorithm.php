<?php
// this script is the engine of the whole program
// it is called in 'control.php', so this code is executed every second again.
// the code checks whether clients are ready to start the experiment,
// ready to go to a new round, and if they are still connected to the server
include('../common.php');
include('../sqlLibrary.php');

$PHPready = 0;
$time0 = microtime(true);

// read global parameters
$numberPeriods = getParameter('numberPeriods');
$totalPlayers = getParameter('totalPlayers');
$groupSize = getParameter('groupSize');
$numberOfGroups = $totalPlayers / $groupSize;
$matchingProcedure = getParameter('sortableMatching');


// set the timeouts (in seconds) to remove players when they are not active anymore
$timeoutDisconnect = 30;
$timeoutDisconnectLobby = 15;
// declare variable to count how many clients are done with the quiz (and ready to enter the HIT)
$sumDoneQuiz = 0;
// store the number of ready participants (to go to the next period) in an array that keeps track of that for each group
$subjReady = array_fill(1, ($numberOfGroups + 1), '0');
// count how many clients each group holds at this moment
$subjInGroup = array_fill(1, $groupSize, '0');
// count how many participants each group contains at this moment
$subjCnt = 0;

// ===(0) Read all data needed for the control script
$conn = mysqli_connect(HOST, ADMIN, PASSW, DBNAME) or die(mysqli_error());
$result = mysqli_query($conn, "SELECT playerNr, groupNr, groupNrStart, ipaddress, currentGroupSize, period, lastActionTime, connected, onPage FROM " . PROJECTID . "core ORDER BY playerNr ASC");
$playerNr = [];
$ipaddress = [];
$groupNr = [];
$groupNrStart = [];
$period = [];
$onPage = [];
$connected = [];
while ($row = mysqli_fetch_assoc($result)) {
    $playerNr[] = $row['playerNr'];
    $groupNr[] = $row['groupNr'];
    $groupNrStart[] = $row['groupNrStart'];
    $lastActionTime[] = $row['lastActionTime'];
    $ipaddress[] = $row['ipaddress'];
    $currentGroupSize[] = $row['currentGroupSize'];
    $period[] = $row['period'];
    $connected[] = $row['connected'];
    $onPage[] = basename($row['onPage']);
}

// === (5) Regulate connections to the server and inform peers of dropouts
$timeNow = time(); // take the time once before entering the loop
for ($i = 0; $i < count($playerNr); $i++) {
    // if client i was still connected last time that we checked, see if it is still connected
    $timesincelastaction = $timeNow - $lastActionTime[$i];
    // retrieve group number and the page a client is watching
    // === (5a) Before the interaction phase has started
    if ($groupNr[$i] == 0) {
        // before the HIT has started, we have to check more often if the client is still there
        // we do not want inactive clients to be allocated to a group!!
        // after some time of inactivity, set the flag 'connected' to zero, so that the client cannot be allocated to a group
        $timeout = $timeoutDisconnect;
        if ($onPage[$i] == 'lobby' || $onPage[$i] == 'lobby.php') $timeout = $timeoutDisconnectLobby;

        if ($timesincelastaction > $timeout) {
            if ($connected[$i] == 1) {
                $message = 'Connection lost pre-lobby';
                $timeEvent = date('Y/m/d H:i:s');
                insertRecord("logEvents", "groupNr, playerNr, timeEvent, event", "'$groupNr[$i]', '$playerNr[$i]', '$timeEvent', '$message'");

                setValue("core", "playerNr=$playerNr[$i]", "connected", 0);
                //			setValue("core","playerNr=$playerNr[$i]","onPage",'disconnected');
            }
        } else {
            if ($connected[$i] == 0) {
                $message = 'Connection made pre-lobby';
                $timeEvent = date('Y/m/d H:i:s');
                insertRecord("logEvents", "groupNr, playerNr, timeEvent, event", "'$groupNr[$i]', '$playerNr[$i]', '$timeEvent', '$message'");

                setValue("core", "playerNr=$playerNr[$i]", "connected", 1);
            }
        }
    } // === (5b) Interaction phase; accommodate dropouts etc, etc
    elseif ($period[$i] <= $numberPeriods) {
        // in later phases of the game, we check less often. We do not want needless experimental terminations due to hanging browsers or so...
        if ($timesincelastaction > $timeoutDisconnect) {
            // APPARENTLY, CLIENT i HAS TIMED OUT. fill out a random decision as soon as all other group members have done the same.
            if ($connected[$i] == 1) {
                // flag the disconnection
                setValue("core", "playerNr=$playerNr[$i]", "connected", 0);

                if ($period[$i] >= $numberPeriods) {
                    $message = 'Player finished the task';
                    $timeNow = date('Y/m/d H:i:s');
                    insertRecord("logEvents", "groupNr, playerNr, timeEvent, event", "'$groupNr[$i]', '$playerNr[$i]', '$timeNow', '$message'");
                    //setValue("core", "playerNr=$playerNr[$i]", "onPage", "finished");
                } else {
                    $message = 'Player dropped out';
                    $timeNow = date('Y/m/d H:i:s');
                    insertRecord("logEvents", "groupNr, playerNr, timeEvent, event", "'$groupNr[$i]', '$playerNr[$i]', '$timeNow', '$message'");
                    //setValue("core", "playerNr=$playerNr[$i]", "onPage", "disconnected");
                }

                $dropoutHandler = getParameter('dropoutHandling');

                if ($dropoutHandler != 3) { // 3 means 'disable exclusion'
                    //
                    $newGroupSize = $currentGroupSize[$i] - 1;
                    // tell the other players in this group, that one player dropped out
                    for ($j = 0; $j < count($playerNr); $j++) {
                        if ($groupNrStart[$j] == $groupNrStart[$i] && $playerNr[$i] != $playerNr[$j]) {
                            if ($newGroupSize >= 0) setValue("core", "playerNr=$playerNr[$j]", "currentGroupSize", $newGroupSize);
                        }
                    }
                    setValue("core", "playerNr=$playerNr[$i]", "groupNr", -1);
                    setValue("core", "playerNr=$playerNr[$i]", "leftExperiment", 1);
                }
                // now determine which action to take upon dropout

                if ($dropoutHandler == 1) { // abort group
                    $message = 'Group aborted due to dropout of this participant';
                    $timeNow = date('Y/m/d H:i:s');
                    insertRecord("logEvents", "groupNr, playerNr, timeEvent, event", "'$groupNr[$i]', '$playerNr[$i]', '$timeNow', '$message'");
                    // set flags (to prevent re-entering or affecting other players)
                    setValue("core", "playerNr=$playerNr[$i]", "groupAborted", 1);

                    // record the dropout for group members (who will be booted out when they go to the next page
                    $message = 'Group aborted due to dropout of fellow-group member';
                    $timeNow = date('Y/m/d H:i:s');

                    // remove all group members from the session
                    for ($j = 0; $j < count($playerNr); $j++) {
                        if ($groupNr[$j] == $groupNr[$i] && $playerNr[$i] != $playerNr[$j]) {
                            setValue("core", "playerNr=$playerNr[$j]", "groupAborted", 1);
                            insertRecord("logEvents", "groupNr, playerNr, timeEvent, event", "'$groupNr[$j]', '$playerNr[$j]', '$timeNow', '$message'");
                        }
                    }
                }
                if ($dropoutHandler == 2) {
                    // proceed with decreased group
                    // log that the participant was removed
                    $message = 'Timed out, removed from experiment. The group proceeds.';
                    $timeNow = date('Y/m/d H:i:s');
                    insertRecord("logEvents", "groupNr, playerNr, timeEvent, event", "'$groupNr[$i]', '$playerNr[$i]', '$timeNow', '$message'");
                }
            }
        } // otherwise, the client is still connected. record that
        else {
            if ($connected[$i] == 0 && $groupNr[$i] >= 0) setValue("core", "playerNr=$playerNr[$i]", "connected", 1);
        }
    }
    //=== (5c) after interaction phase, close connection to the server
    if ($period[$i] > $numberPeriods && $connected[$i] == 1) setValue("core", "playerNr=$playerNr[$i]", "connected", 0);
}

if ($matchingProcedure == 1) {
    // ===(2) Count players in the lobby, and are who is ready to proceed to the next round
    for ($i = 0; $i < count($playerNr); $i++) {    // === (2a) Count how many players in the lobby are ready to form a group
        // wait until a group has filled up and the players are ready to go, then assign group numbers
        // check if client has been assigned a group, and if he is waiting to enter the HIT
        if ($connected[$i] == 1) {
            $groupAssigned = 0;
            if ($groupNr[$i] > 0) $groupAssigned = 1;
            $inLobby = 0;
            if ($onPage[$i] == 'lobby' || $onPage[$i] == 'lobby.php') $inLobby = 1;
            if ($groupAssigned == 0 && $inLobby == 1 && $subjCnt < $groupSize) {
                // if client is connected and the group is not full yet, and no group has been assigned yet
                // NB: each time this code runs (once every second), only one group can be started
                // because he counter '$subjCnt' cannot exceed the group size '$groupSize', so we can allocate max 1 group per second
                $subjInGroup[$subjCnt] = $playerNr[$i];
                $subjCnt++;
            }
        }
    }
    // ===(3) Allocate players in the lobby to groups
    if ($subjCnt == $groupSize) {
        // determine which is the lowest group that is not full yet
        $sql = "SELECT * FROM " . PROJECTID . "core ORDER BY groupNrStart DESC";
        $result = @mysqli_query($conn, $sql) or die("Couldn't execute query " . $sql);
        if ($row = mysqli_fetch_array($result)) {
            $groupNr1 = $row['groupNrStart'] + 1;
        } else {
            $groupNr1 = 1;
        }
        //add this number to the table 'groupComposition'

        for ($j = 0; $j < $groupSize; $j++) {
            $focalPlayer = $subjInGroup[$j];
            setValues("core", "playerNr=$focalPlayer", "groupNr=$groupNr1, groupNrStart=$groupNr1, currentGroupSize=$groupSize, period=1");
            setValue("core", "playerNr=$focalPlayer", "wait_lastInPeriod", 0);
            setValue("core", "playerNr=$focalPlayer", "subjectNr", $j + 1);
            setValue("decisions", "playerNr=$focalPlayer", "subjectNr", $j + 1);
            setValue("decisions", "playerNr=$focalPlayer", "groupNr", $groupNr1);
            $randID = getValue("session", "playerNr=$focalPlayer", "randomid");
            setValue("session", "playerNr=$focalPlayer", "relevantRandomid", $randID);
        }
    }
}
if ($matchingProcedure == 2) {
    // we will assign groups according to roles; each role should be present EXACTLY ONCE
    $playerNrMatching = [];
    $roleList = [];
    $conn = mysqli_connect(HOST, ADMIN, PASSW, DBNAME) or die(mysqli_error());
    // retrieve those entries from the database who are waiting in the lobby and sort according to timestamp
    $result = mysqli_query($conn, "SELECT playerNr, role FROM " . PROJECTID . "core 
        WHERE ((onPage='lobby' OR onPage='lobby.php') AND groupNr=0 AND connected=1) ORDER BY enterLobby ASC");
    while ($row = mysqli_fetch_assoc($result)) {
        $playerNrMatching[] = $row['playerNr'];
        $roleList[] = $row['role'];
    }
    $subjCnt = 0;
    for ($roleIndex = 1; $roleIndex <= $groupSize; $roleIndex++) {
        $position = array_search($roleIndex, $roleList);
        if (in_array($roleIndex, $roleList)) {
            $player = $playerNrMatching[$position];
            $subjInGroup[$subjCnt] = $player;
            $subjCnt++;
        }
    }

    if ($subjCnt == $groupSize) { // we have a group ready. Now assign group numbers and release them from the lobby (through groupNr > 0)
        // determine which is the lowest group that is not full yet
        $sql = "SELECT * FROM " . PROJECTID . "core ORDER BY groupNrStart DESC";
        $result = @mysqli_query($conn, $sql) or die("Couldn't execute query " . $sql);
        if ($row = mysqli_fetch_array($result)) {
            $groupNr1 = $row['groupNrStart'] + 1;
        } else {
            $groupNr1 = 1;
        }
        for ($j = 0; $j < $groupSize; $j++) {
            $focalPlayer = $subjInGroup[$j];
            setValues("core", "playerNr=$focalPlayer", "groupNr=$groupNr1, groupNrStart=$groupNr1, currentGroupSize=$groupSize, period=1");
            setValue("core", "playerNr=$focalPlayer", "wait_lastInPeriod", 0);
            setValue("core", "playerNr=$focalPlayer", "subjectNr", $j + 1);
            setValue("decisions", "playerNr=$focalPlayer", "subjectNr", $j + 1);
            setValue("decisions", "playerNr=$focalPlayer", "groupNr", $groupNr1);
            $randID = getValue("session", "playerNr=$focalPlayer", "randomid");
            setValue("session", "playerNr=$focalPlayer", "relevantRandomid", $randID);
        }
    }
}
if ($matchingProcedure == 3) {
    // we will assign groups according to roles; all group members MUST HAVE THE SAME ROLE (for treatment variation)
    $playerNrMatching = [];
    $roleList = [];
    $conn = mysqli_connect(HOST, ADMIN, PASSW, DBNAME) or die(mysqli_error());
    // retrieve those entries from the database who are waiting in the lobby and sort according to timestamp
    $result = mysqli_query($conn, "SELECT playerNr, role FROM " . PROJECTID . "core WHERE ((onPage='lobby' OR onPage='lobby.php') AND groupNr=0 AND connected=1) ORDER BY enterLobby ASC");
    while ($row = mysqli_fetch_assoc($result)) {
        $playerNrMatching[] = $row['playerNr'];
        $roleList[] = $row['role'];
    }

// which unique roles are present in the lobby?
    $rolesInLobby = array_unique($roleList);
    // loop over the present roles
    for ($roleIndex = 0; $roleIndex < count($rolesInLobby); $roleIndex++) {
        $subjInGroupSameRole = array_fill(1, $groupSize, '0');
        $subjCnt = 0;
        $roleNr = $rolesInLobby[$roleIndex]; // roleNr now contains one role

        for ($ind = 0; $ind < count($roleList); $ind++) {
            if ($roleList[$ind] == $roleNr && $subjCnt < $groupSize) {
                $player = $playerNrMatching[$ind];
                $subjInGroupSameRole[$subjCnt] = $player;
                $subjCnt++;
            }
        }
        if ($subjCnt == $groupSize) { // we have a group ready. Now assign group numbers and release them from the lobby (through groupNr > 0)
            // determine which is the lowest group that is not full yet

            $sql = "SELECT * FROM " . PROJECTID . "core ORDER BY groupNrStart DESC";
            $result = @mysqli_query($conn, $sql) or die("Couldn't execute query " . $sql);
            if ($row = mysqli_fetch_array($result)) {
                $groupNr1 = $row['groupNrStart'] + 1;
            } else {
                $groupNr1 = 1;
            }
            for ($j = 0; $j < $groupSize; $j++) {
                $focalPlayer = $subjInGroupSameRole[$j];
                setValues("core", "playerNr=$focalPlayer", "groupNr=$groupNr1, groupNrStart=$groupNr1, currentGroupSize=$groupSize, period=1");
                setValue("core", "playerNr=$focalPlayer", "wait_lastInPeriod", 0);
                setValue("core", "playerNr=$focalPlayer", "subjectNr", $j + 1);

                setValue("decisions", "playerNr=$focalPlayer", "subjectNr", $j + 1);
                setValue("decisions", "playerNr=$focalPlayer", "groupNr", $groupNr1);

                $randID = getValue("session", "playerNr=$focalPlayer", "randomid");
                setValue("session", "playerNr=$focalPlayer", "relevantRandomid", $randID);
            }
        }
    }
}

// === (4) Allow players who are ready for the next period to move on
for ($i = 0; $i < count($playerNr); $i++) {
    // === (2b) Count players in each group ready for the next period
    // do not check players that were excluded (with groupNr=-1)


    $readyForNextPeriod = getValue("core", "playerNr=$playerNr[$i]", "wait_lastInPeriod");
    // count for each group how many core are ready
    if ($readyForNextPeriod == '1') {
        if ($groupNr[$i] > 0) $subjReady[$groupNr[$i]]++;
        elseif ($groupNr[$i] == 0) $singleReady[$i] = 1;
    } else $singleReady[$i] = 0;

}

for ($i = 0; $i < count($playerNr); $i++) {
    if ($groupNr[$i] >= 0) {
        // if everyone's ready, go to the next round, taking into account potential dropouts
        if ($subjReady[$groupNr[$i]] == $currentGroupSize[$i] || $singleReady[$i] == 1) {
            $newPeriod = $period[$i] + 1;
            if ($period[$i] <= $numberPeriods) {
                // update the period number
                setValue("core", "playerNr=$playerNr[$i]", "period", $newPeriod);
                setValue("core", "playerNr=$playerNr[$i]", "periodReady", 1);
                // set all regulating counters to zero
                for ($l = 1; $l <= 10; $l++) {
                    $varName = 'wait_' . $l . 'ready';
                    //setValue("core","playerNr=$playerNr[$i]",$varName, 0);
                }
                setValue("core", "playerNr=$playerNr[$i]", "wait_lastInPeriod", 0);
                resetWaitingValues($playerNr[$i]);

            }
        }
    }
}


// if the script has been executed, record the time the server took to run the script
$phpTime = microtime(true) - $time0;
echo round($phpTime, 3);
/*
}
*/