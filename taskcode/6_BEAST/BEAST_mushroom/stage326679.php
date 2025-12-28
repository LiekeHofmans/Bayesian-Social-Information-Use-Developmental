<html>
        <head>
        
        <?php
    
        include("_projectID.php");
        include(PATH."basis/participant/header.php");
	    $_SESSION['projectID']=PROJECTID;
	    
	    ?>

        <link href="<?php echo PATH;?>basis/css/newlayout.css?v1" rel="stylesheet" type="text/css"  />
        <link href="<?php echo PATH;?>basis/css/newlayout_bootstrap.css" rel="stylesheet" type="text/css"  />
        <link href="<?php echo PATH;?>basis/css/grid.css" rel="stylesheet" type="text/css"  /><title>end of round</title>

        <script> var v={}; var wronganswers={}; var totalwronganswers={};var maxFalse = null;
        var firstStageExp = <?php echo json_encode(FIRSTPAGE . ".php"); ?>;
        var thisPage = <?php echo json_encode($thisPage); ?>;
        var sessionIndexJavascript = "<?php echo $_SESSION[sessionID];?>";
        pageRefreshed=0;
        var loopBegin = "stage" + loopStart + ".php";
        var afterLoopEnd = 326678;
        if (thisPage == firstStageExp || (thisPage==loopBegin && period > 1) || loopEnd==afterLoopEnd) firstStage();
        /* if (thisPage == firstStageExp || thisPage==loopBegin || loopEnd==afterLoopEnd) firstStage(); */
        TimeOut=null;
        function skipStage(proceedifpossible) {
         if (proceedifpossible === undefined) proceedifpossible = false;
         if (proceedifpossible) location.replace('stage326680.php?session_index=<?php echo $_SESSION[sessionID];?>');
         else location.replace('wait326679.php?session_index=<?php echo $_SESSION[sessionID];?>');
        }
        $(document).ready(function(){
        if (bot) { document.getElementsByClassName("buttonclick")[0].click(); }
        });
        
        </script>
        </head><body><div id="mainwrap" class="container" style="width: 100%; padding-left: 5%; padding-right: 5%; padding-top: 1%;"><form autocomplete="off"><div class="row"><!-- START Element 1 Type: 19-->
        
        
        <script>showPer = 1 + (period-1)%5;</script><!-- END Element 1 Type: 19-->
        
        <!-- START Element 2 Type: 1-->
        
        <div class="col-sm-12" id="wrap2" style="display: none;"><div class="btnbox2 paddlr" style="text-align: center"><h3>Ronde afgelopen</h3>Dit is het einde van ronde <script>document.write(showPer)</script>.<br>Klik hieronder om verder te gaan.</div>
        </div><script>if((period != 5 & period <10)) { $('#wrap2').show(); } </script><!-- END Element 2 Type: 1-->
        
        <!-- START Element 3 Type: 1-->
        
        <div class="col-sm-12" id="wrap3" style="display: none;"><div class="btnbox2 paddlr" style="text-align: center"><h3>Einde van het spel</h3><p>Je bent nu klaar met het dierenspel! Klik hieronder om jouw bonus te bekijken.</p></div>
        </div><script>if((period >= 5)) { $('#wrap3').show(); } </script><!-- END Element 3 Type: 1-->
        
        <!-- START Element 4 Type: 18-->
        
        <div class="col-sm-12" id="wrap4" style="display: none;">
        <script>
       
        
        </script>
        
        <div  id="button4">
        <div id="buttonclick4" class="lionessbutton btn btn-default btn-lg btn-block " style=" white-space:normal !important; word-wrap: break-word;" onclick="
        $(this).hide(); $('#buttonload4').show();
        if (additionalCheck4()) {
            hideError4();
            if (checkEntries()) toNextPage4();
            else  { $(this).show(); 
            $('#buttonload4').hide(); }
        } else {
         $(this).show(); 
         $('#buttonload4').hide();
         }
        ">Ga verder</div><div id="buttonload4" style="width: 100%; text-align: center; display: none;"><img src="<?php echo PATH;?>basis/pic/buttonload.gif"></div><div id="field4_error" class="alert alert-danger" style="display: none; text-align: center;"></div><div id="field4_attempts" class="alert alert-warning" style="display: none; text-align: center;"><span class="attempts_text">Attempts left to answer the control questions</span>:&nbsp;<span id="field4_attempts_num"></span></div></div><script>if(maxFalse!=null) {
            var numFails=quizFail(playerNr,1);  
            $('#field4_attempts').show();
            $('#field4_attempts_num').html(maxFalse-numFails);
           
        }
        function showError4(text) {
            var errorfield= $('#field4_error');
            errorfield.show();
            errorfield.html(text);
        
        }
        
        function hideError4() {
            $('#field4_error').hide();
        }
       
        
        

        if (typeof window.showNext === 'undefined') {
            window.showNext = function(url, nextstage, stageNr) {
                var timeRecName = "time_" + stageNr;
                var timeOnThisPage = getServerTime() - tStart;
                setValue(timeRecName, timeOnThisPage);
                location.replace(url); 
            }
        }


        

        var checker;
        
        function checkEntries() {
           checker=0;

            var numEntries = document.forms[0].length;
            var numValuesExpected=0;

            for (var i=0; i<numEntries; i++)
            {
                var name = "checkValue_" + document.forms[0][i].id;
                if (document.forms[0][i].id!="")
                {                   
                    fn = window[name]; /* this is a generic function calling the checker for the variable "name"  */
                    fnExists = typeof fn === "function";
                    if (fnExists) {
                        fn();
                        ++numValuesExpected;
                    }
                 };

            }
           if (checker==numValuesExpected) return true;
           else {
                checkFail();
                return false;
            }
        }
        
        function additionalCheck4() {newPeriod = period + 1;
setValue('core', 'playerNr='+playerNr, 'period', newPeriod);
insertRecord('decisions', 'playerNr, period', [playerNr, newPeriod]);

           return true;
        }

       



        function checkFail() {} function toNextPage4() {
            if (loopEnd==326679) { showNext('wait326679.php?session_index=<?php echo $_SESSION[sessionID];?>',326675,326679);}
            else {showNext('stage326675.php?session_index=<?php echo $_SESSION[sessionID];?>',326675,326679);}

            };</script></div><script>if((period<5)) { $('#wrap4').show(); $('#buttonclick4').addClass('buttonclick');} </script><!-- END Element 4 Type: 18-->
        
        <!-- START Element 5 Type: 18-->
        
        <div class="col-sm-12" id="wrap5" style="display: none;">
        <script>
       
        
        </script>
        
        <div  id="button5">
        <div id="buttonclick5" class="lionessbutton btn btn-default btn-lg btn-block " style=" white-space:normal !important; word-wrap: break-word;" onclick="
        $(this).hide(); $('#buttonload5').show();
        if (additionalCheck5()) {
            hideError5();
            if (checkEntries()) toNextPage5();
            else  { $(this).show(); 
            $('#buttonload5').hide(); }
        } else {
         $(this).show(); 
         $('#buttonload5').hide();
         }
        ">Ga verder</div><div id="buttonload5" style="width: 100%; text-align: center; display: none;"><img src="<?php echo PATH;?>basis/pic/buttonload.gif"></div><div id="field5_error" class="alert alert-danger" style="display: none; text-align: center;"></div><div id="field5_attempts" class="alert alert-warning" style="display: none; text-align: center;"><span class="attempts_text">Attempts left to answer the control questions</span>:&nbsp;<span id="field5_attempts_num"></span></div></div><script>if(maxFalse!=null) {
            var numFails=quizFail(playerNr,1);  
            $('#field5_attempts').show();
            $('#field5_attempts_num').html(maxFalse-numFails);
           
        }
        function showError5(text) {
            var errorfield= $('#field5_error');
            errorfield.show();
            errorfield.html(text);
        
        }
        
        function hideError5() {
            $('#field5_error').hide();
        }
       
        
        

        if (typeof window.showNext === 'undefined') {
            window.showNext = function(url, nextstage, stageNr) {
                var timeRecName = "time_" + stageNr;
                var timeOnThisPage = getServerTime() - tStart;
                setValue(timeRecName, timeOnThisPage);
                location.replace(url); 
            }
        }


        

        var checker;
        
        function checkEntries() {
           checker=0;

            var numEntries = document.forms[0].length;
            var numValuesExpected=0;

            for (var i=0; i<numEntries; i++)
            {
                var name = "checkValue_" + document.forms[0][i].id;
                if (document.forms[0][i].id!="")
                {                   
                    fn = window[name]; /* this is a generic function calling the checker for the variable "name"  */
                    fnExists = typeof fn === "function";
                    if (fnExists) {
                        fn();
                        ++numValuesExpected;
                    }
                 };

            }
           if (checker==numValuesExpected) return true;
           else {
                checkFail();
                return false;
            }
        }
        
        function additionalCheck5() {

           return true;
        }

       



        function checkFail() {} function toNextPage5() {
            if (loopEnd==326679) { showNext('wait326679.php?session_index=<?php echo $_SESSION[sessionID];?>',326680,326679);}
            else {showNext('stage326680.php?session_index=<?php echo $_SESSION[sessionID];?>',326680,326679);}

            };</script></div><script>if((period >=5)) { $('#wrap5').show(); $('#buttonclick5').addClass('buttonclick');} </script><!-- END Element 5 Type: 18-->
        
        </div><script>setInterval(function(){ if (period != 5 & period <10) $('#wrap2').show();if (!(period != 5 & period <10)) $('#wrap2').hide();if (period >= 5) $('#wrap3').show();if (!(period >= 5)) $('#wrap3').hide();if (period<5) $('#wrap4').show();if (!(period<5)) $('#wrap4').hide();if (period >=5) $('#wrap5').show();if (!(period >=5)) $('#wrap5').hide(); }, 100);</script></form></div></div></body></html>