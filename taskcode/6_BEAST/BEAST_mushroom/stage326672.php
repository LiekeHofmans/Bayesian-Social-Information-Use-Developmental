<html>
        <head>
        
        <?php
    
        include("_projectID.php");
        include(PATH."basis/participant/header.php");
	    $_SESSION['projectID']=PROJECTID;
	    
	    ?>

        <link href="<?php echo PATH;?>basis/css/newlayout.css?v1" rel="stylesheet" type="text/css"  />
        <link href="<?php echo PATH;?>basis/css/newlayout_bootstrap.css" rel="stylesheet" type="text/css"  />
        <link href="<?php echo PATH;?>basis/css/grid.css" rel="stylesheet" type="text/css"  /><title>instructions R2</title>

        <script> var v={}; var wronganswers={}; var totalwronganswers={};var maxFalse = null;
        var firstStageExp = <?php echo json_encode(FIRSTPAGE . ".php"); ?>;
        var thisPage = <?php echo json_encode($thisPage); ?>;
        var sessionIndexJavascript = "<?php echo $_SESSION[sessionID];?>";
        pageRefreshed=0;
        var loopBegin = "stage" + loopStart + ".php";
        var afterLoopEnd = 326671;
        if (thisPage == firstStageExp || (thisPage==loopBegin && period > 1) || loopEnd==afterLoopEnd) firstStage();
        /* if (thisPage == firstStageExp || thisPage==loopBegin || loopEnd==afterLoopEnd) firstStage(); */
        TimeOut=null;
        function skipStage(proceedifpossible) {
         if (proceedifpossible === undefined) proceedifpossible = false;
         if (proceedifpossible) location.replace('stage326673.php?session_index=<?php echo $_SESSION[sessionID];?>');
         else location.replace('wait326672.php?session_index=<?php echo $_SESSION[sessionID];?>');
        }
        $(document).ready(function(){
        if (bot) { document.getElementsByClassName("buttonclick")[0].click(); }
        });
        
        </script>
        </head><body><div id="mainwrap" class="container" style="width: 100%; padding-left: 5%; padding-right: 5%; padding-top: 1%;"><form autocomplete="off"><div class="row"><!-- START Element 1 Type: 1-->
        
        <div class="col-sm-12" id="wrap1" style="display: none;"><div class="btnbox2 paddlr" style="text-align: center"><h3>Instructies 2 van 3</h3><p>Zodra de afbeelding is verdwenen vul jij je schatting van het aantal dieren in.&nbsp;<br>Dit is je schatting voor <b>deel A</b> van de ronde.<br></p><p>Nadat je je schatting hebt ingevuld begint <b>deel B</b> van de ronde.<br>Je zult de <i>deel A schatting van een eerdere deelnemer </i>zien.&nbsp;</p><p>Meer dan 450 studenten van de Universiteit van Amsterdam hebben dit spel al eerder gespeeld.<br>In elke ronde zie je de deel A schatting van een van deze eerdere deelnemers.</p><p><span style="background-color: initial;">De eerdere deelnemers zagen dezelfde afbeelding als jij. Zij zagen de afbeelding ook voor 6 seconden.&nbsp;<br></span><span style="background-color: initial;">Nadat de afbeelding verdween moesten zij ook schatten hoeveel dieren er op de afbeelding stonden.<br></span><span style="background-color: initial;">Zij konden ook een hogere bonus verdienen als hun schatting preciezer was.&nbsp;</span><br></p><p>Je vult dan <b>een tweede schatting</b> in.<br>Je kunt dezelfde schatting invullen als in deel A, of je kunt je schatting aanpassen.<br>Dit is je schatting voor <b>deel B</b> van een ronde.</p><p><br>Zodra je je deel B schatting hebt ingevuld is de ronde voorbij en begint er een nieuwe ronde.<br></p><p></p></div>
        </div><script>if((true)) { $('#wrap1').show(); } </script><!-- END Element 1 Type: 1-->
        
        <!-- START Element 2 Type: 18-->
        
        <div class="col-sm-12" id="wrap2" style="display: none;">
        <script>
       
        
        </script>
        
        <div  id="button2">
        <div id="buttonclick2" class="lionessbutton btn btn-default btn-lg btn-block " style=" white-space:normal !important; word-wrap: break-word;" onclick="
        $(this).hide(); $('#buttonload2').show();
        if (additionalCheck2()) {
            hideError2();
            if (checkEntries()) toNextPage2();
            else  { $(this).show(); 
            $('#buttonload2').hide(); }
        } else {
         $(this).show(); 
         $('#buttonload2').hide();
         }
        ">Ga  verder</div><div id="buttonload2" style="width: 100%; text-align: center; display: none;"><img src="<?php echo PATH;?>basis/pic/buttonload.gif"></div><div id="field2_error" class="alert alert-danger" style="display: none; text-align: center;"></div><div id="field2_attempts" class="alert alert-warning" style="display: none; text-align: center;"><span class="attempts_text">Attempts left to answer the control questions</span>:&nbsp;<span id="field2_attempts_num"></span></div></div><script>if(maxFalse!=null) {
            var numFails=quizFail(playerNr,1);  
            $('#field2_attempts').show();
            $('#field2_attempts_num').html(maxFalse-numFails);
           
        }
        function showError2(text) {
            var errorfield= $('#field2_error');
            errorfield.show();
            errorfield.html(text);
        
        }
        
        function hideError2() {
            $('#field2_error').hide();
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
        
        function additionalCheck2() {

           return true;
        }

       



        function checkFail() {} function toNextPage2() {
            if (loopEnd==326672) { showNext('wait326672.php?session_index=<?php echo $_SESSION[sessionID];?>',326673,326672);}
            else {showNext('stage326673.php?session_index=<?php echo $_SESSION[sessionID];?>',326673,326672);}

            };</script></div><script>if((true)) { $('#wrap2').show(); $('#buttonclick2').addClass('buttonclick');} </script><!-- END Element 2 Type: 18-->
        
        <!-- START Element 3 Type: 18-->
        
        <div class="col-sm-12" id="wrap3" style="display: none;">
        <script>
       
        
        </script>
        
        <div  id="button3">
        <div id="buttonclick3" class="lionessbutton btn btn-default btn-lg btn-block " style=" white-space:normal !important; word-wrap: break-word;" onclick="
        $(this).hide(); $('#buttonload3').show();
        if (additionalCheck3()) {
            hideError3();
            if (checkEntries()) toNextPage3();
            else  { $(this).show(); 
            $('#buttonload3').hide(); }
        } else {
         $(this).show(); 
         $('#buttonload3').hide();
         }
        ">Ga terug</div><div id="buttonload3" style="width: 100%; text-align: center; display: none;"><img src="<?php echo PATH;?>basis/pic/buttonload.gif"></div><div id="field3_error" class="alert alert-danger" style="display: none; text-align: center;"></div><div id="field3_attempts" class="alert alert-warning" style="display: none; text-align: center;"><span class="attempts_text">Attempts left to answer the control questions</span>:&nbsp;<span id="field3_attempts_num"></span></div></div><script>if(maxFalse!=null) {
            var numFails=quizFail(playerNr,1);  
            $('#field3_attempts').show();
            $('#field3_attempts_num').html(maxFalse-numFails);
           
        }
        function showError3(text) {
            var errorfield= $('#field3_error');
            errorfield.show();
            errorfield.html(text);
        
        }
        
        function hideError3() {
            $('#field3_error').hide();
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
        
        function additionalCheck3() {

           return true;
        }

       



        function checkFail() {} function toNextPage3() {
            if (loopEnd==326672) { showNext('wait326672.php?session_index=<?php echo $_SESSION[sessionID];?>',326671,326672);}
            else {showNext('stage326671.php?session_index=<?php echo $_SESSION[sessionID];?>',326671,326672);}

            };</script></div><script>if((true)) { $('#wrap3').show(); $('#buttonclick3').addClass('buttonclick');} </script><!-- END Element 3 Type: 18-->
        
        </div><script>setInterval(function(){ if (true) $('#wrap1').show();if (!(true)) $('#wrap1').hide();if (true) $('#wrap2').show();if (!(true)) $('#wrap2').hide();if (true) $('#wrap3').show();if (!(true)) $('#wrap3').hide(); }, 100);</script></form></div></div></body></html>