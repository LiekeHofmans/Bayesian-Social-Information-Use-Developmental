DROP TABLE IF EXISTS  `e3765g29044_globals`;SELECT 1;CREATE TABLE `e3765g29044_globals` (
                  `name` varchar(36) NOT NULL,
                  `value` TEXT NOT NULL
                ) CHARACTER SET utf8;SELECT 1;INSERT INTO `e3765g29044_globals` (`name`, `value`) VALUES ('compiled', '1646053871'),('active', '1'),('testMode', '0'),('totalPlayers', '10000'),('groupSize', '1'),('numberPeriods', '1'),('loopStart', ''),('loopEnd', ''),('participationFee', '0'),('exchangeRate', '0.01'),('reEnter', '0'),('dropoutHandling', '3'),('sortableMatching', '1'),('message0', 'This HIT is currently offline. You cannot participate at this time.'),('message1', 'According to our records, your device has already been connected to the server during this session. &lt;br&gt;                Participants are only allowed to enter a session once. Thank you for your understanding.'),('message2', 'We have sufficient participants for this HIT. &lt;br&gt;Unfortunately, you cannot participate at this time. &lt;br&gt;&lt;br&gt;                Thank you for your understanding.'),('message3', 'You are currently not logged in. You cannot participate in the HIT.'),('message4', 'Unfortunately, this HIT was terminated for a technical reason! &lt;br&gt;&lt;br&gt;&lt;br&gt;                You cannot continue. &lt;br&gt;&lt;br&gt;&lt;br&gt;                You will receive your guaranteed participation fee of $ $participationFee$.                To collect your earnings, please fill out this random code on MTurk.                &lt;br&gt;&lt;br&gt;&lt;b&gt;$randomid$&lt;/b&gt;.                &lt;br&gt;                Once you have filled out this code, you can close this window.                Thank you for your participation.'),('message5', 'You did not make a decision before the time was up. &lt;br&gt;&lt;br&gt; You have been removed from the HIT. &lt;br&gt;&lt;br&gt;                        You can close down this window.'),('message6', 'Unfortunately, one of the players in your group dropped out of the HIT! &lt;br&gt;&lt;br&gt;&lt;br&gt;                 You cannot continue. &lt;br&gt;&lt;br&gt;&lt;br&gt;You will receive your guaranteed participation fee of                  $ $participationFee$.                 To collect your earnings, please fill out this random code on MTurk.                 &lt;br&gt;&lt;br&gt;&lt;b&gt;$randomid$&lt;/b&gt;.                 &lt;br&gt;                 Once you have filled out this code, you can close this window.                 Thank you for your participation.'),('message7', 'As indicated in our HIT text on MTurk, our HIT does &lt;b&gt;not&lt;/b&gt; support Microsoft Internet Explorer. &lt;br&gt;                         Please return this HIT.                         &lt;br&gt;                         We apologise for any inconvenience caused.'),('message8', 'You did not answer the quiz correctly and were excluded from further participation                                               '),('antsNumber', '93'),('beesNumber', '78'),('flamingosNumber', '59'),('cranesNumber', '74'),('cricketsNumber', '69'),('img_size', '50'),('overlap_ratio', '0.5'),('border', '50');SELECT 1;ALTER TABLE e3765g29044_globals ADD PRIMARY KEY(`name`);SELECT 1;DROP TABLE IF EXISTS `e3765g29044_decisions`;SELECT 1;CREATE TABLE IF NOT EXISTS `e3765g29044_decisions` (
                  `playerNr` int(11),
                  `groupNr` int(11),
                  `subjectNr` int(11),
                  `period` int(11)
                  ,`iteration`   TEXT,`relevantDecision`   TEXT,`relevantAorB`   TEXT,`subjectID`   TEXT,`qR1`   TEXT,`qR2`   TEXT,`qR3`   TEXT,`nAnimals`   TEXT,`estimate`   TEXT,`socialInfo`   TEXT,`estimate_revised`   TEXT,`points`   TEXT,`bonusPaymentIfSelected`   TEXT,`dollarsT`   TEXT,`confidence1`   TEXT,`confidence2`   TEXT,`time_326669` float ,`time_326705` float ,`time_326671` float ,`time_326672` float ,`time_326673` float ,`time_326674` float ,`time_326675` float ,`time_326676` float ,`time_326677` float ,`time_326678` float ,`time_326679` float ,`time_326680` float ,`time_326681` float ,`time_326688` float ) CHARACTER SET utf8;SELECT 1;ALTER TABLE e3765g29044_decisions ADD PRIMARY KEY( `playerNr`, `period`);SELECT 1;DROP TABLE IF EXISTS `e3765g29044_logEvents`;SELECT 1;CREATE TABLE IF NOT EXISTS `e3765g29044_logEvents` (
                  `eventNr` int(11) NOT NULL AUTO_INCREMENT,
                  `groupNr` int(11) NOT NULL,
                  `playerNr` int(11) NOT NULL,
                  `timeEvent` varchar(256) NOT NULL,
                  `event` varchar(256) NOT NULL,
                  PRIMARY KEY(eventNr)
                ) CHARACTER SET utf8;SELECT 1;DROP TABLE IF EXISTS `e3765g29044_core`;SELECT 1;CREATE TABLE IF NOT EXISTS `e3765g29044_core` (
                      `playerNr` int(11) NOT NULL AUTO_INCREMENT,                   
                      `groupNr` int(11) NOT NULL,
                      `subjectNr` int(11) NOT NULL,
                      `groupNrStart` int(11) NOT NULL,
                      `currentGroupSize` int(11) NOT NULL,
                      `period` int(11) NOT NULL,
                      `onPage` varchar(30) NOT NULL,
                      `connected` boolean,
                      `tStart` int(11) NOT NULL,
                      `lastActionTime` int(11) NOT NULL,
                      `ipaddress` varchar(99) NOT NULL,
                      `ipaddress_part` varchar(15) NOT NULL,
                      `location` varchar(40) NULL,
                      `waitMore` int(11) NOT NULL,
                      `lobbyReady` boolean,
                      `enterLobby` INT(11),
                      `role` INT(11),`wait_326669ready` boolean,`wait_326705ready` boolean,`wait_326671ready` boolean,`wait_326672ready` boolean,`wait_326673ready` boolean,`wait_326674ready` boolean,`wait_326675ready` boolean,`wait_326676ready` boolean,`wait_326677ready` boolean,`wait_326678ready` boolean,`wait_326679ready` boolean,`wait_326680ready` boolean,`wait_326681ready` boolean,`wait_326688ready` boolean,`wait_lastInPeriod` boolean,
                      `periodReady` boolean,
                      `leftExperiment` boolean,
                      `experimentTerminated` boolean,
                      `groupAborted` boolean,
                      PRIMARY KEY (playerNr)
                    ) CHARACTER SET utf8;SELECT 1;DROP TABLE IF EXISTS `e3765g29044_session`;SELECT 1;CREATE TABLE IF NOT EXISTS `e3765g29044_session` (
                  `playerNr` int(11) NOT NULL,
                  `randomid` VARCHAR(256) NOT NULL,
                  `randomidNotPlayed` VARCHAR(256)   NOT NULL,
                  `relevantRandomid` varchar(256) NOT NULL,
                  `externalID` varchar(256) NULL,
                  `participationAmount` decimal(11,2) NOT NULL,
                  `bonusAmount` decimal(11,2) NOT NULL,
                  `totalEarnings` decimal(11,2) NOT NULL,`qR1_fail`   int(11) DEFAULT 0,`qR2_fail`   int(11) DEFAULT 0,`qR3_fail`   int(11) DEFAULT 0,`quizFail` int(11) DEFAULT 0,
                    PRIMARY KEY (playerNr)
                  ) CHARACTER SET utf8;SELECT 1;TRUNCATE `e3765g29044_session`;SELECT 1;