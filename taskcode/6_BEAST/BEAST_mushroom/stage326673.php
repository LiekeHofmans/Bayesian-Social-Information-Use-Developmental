<html>
        <head>
        
        <?php
    
        include("_projectID.php");
        include(PATH."basis/participant/header.php");
	    $_SESSION['projectID']=PROJECTID;
	    
	    ?>

        <link href="<?php echo PATH;?>basis/css/newlayout.css?v1" rel="stylesheet" type="text/css"  />
        <link href="<?php echo PATH;?>basis/css/newlayout_bootstrap.css" rel="stylesheet" type="text/css"  />
        <link href="<?php echo PATH;?>basis/css/grid.css" rel="stylesheet" type="text/css"  /><title>instructions R3</title>

        <script> var v={}; var wronganswers={}; var totalwronganswers={};var maxFalse = null;
        var firstStageExp = <?php echo json_encode(FIRSTPAGE . ".php"); ?>;
        var thisPage = <?php echo json_encode($thisPage); ?>;
        var sessionIndexJavascript = "<?php echo $_SESSION[sessionID];?>";
        pageRefreshed=0;
        var loopBegin = "stage" + loopStart + ".php";
        var afterLoopEnd = 326672;
        if (thisPage == firstStageExp || (thisPage==loopBegin && period > 1) || loopEnd==afterLoopEnd) firstStage();
        /* if (thisPage == firstStageExp || thisPage==loopBegin || loopEnd==afterLoopEnd) firstStage(); */
        TimeOut=null;
        function skipStage(proceedifpossible) {
         if (proceedifpossible === undefined) proceedifpossible = false;
         if (proceedifpossible) location.replace('stage326674.php?session_index=<?php echo $_SESSION[sessionID];?>');
         else location.replace('wait326673.php?session_index=<?php echo $_SESSION[sessionID];?>');
        }
        $(document).ready(function(){
        if (bot) { document.getElementsByClassName("buttonclick")[0].click(); }
        });
        
        </script>
        </head><body><div id="mainwrap" class="container" style="width: 100%; padding-left: 5%; padding-right: 5%; padding-top: 1%;"><form autocomplete="off"><div class="row"><!-- START Element 1 Type: 1-->
        
        <div class="col-sm-12" id="wrap1" style="display: none;"><div class="btnbox2 paddlr" style="text-align: center"><h3>Instructies 3 van 3</h3><p><b>Hoe preciezer jouw schattingen, hoe meer bonus je kunt verdienen.</b><br>Je bonus wordt als volgt berekend:</p>
<p>Als je klaar bent met de taak, zal de computer willekeurig 1 van de 5 rondes selecteren, en zal dan deel A of deel B van die ronde selecteren.<br>Als je het aantal dieren in die ronde en voor dat deel <i style="font-weight: bold;">precies goed</i><b>&nbsp;had, dan verdien je €1,00.</b><br><b>Voor ieder dier dat je ernaast zat, wordt 5 cent afgetrokken.</b><br>Je bonus kan niet onder de nul eindigen.</p><p>Bijvoorbeeld, als het echte aantal dieren in het plaatje 60 was, en jouw schatting was 53, dan zat je er 7 naast.<br>Dit betekent dat er 7 x €0,05 = €0,35 wordt afgetrokken. <br>Jouw verdiensten voor die schatting zouden dan zijn: €1,00 - €0,35 = €0,65 punten.</p><p>Klik &#039;Ga verder&#039; als je de taak begrijpt.<br>Er volgen dan een paar korte controle-vragen om te checken of je het snapt.</p></div>
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
        ">Ga verder</div><div id="buttonload2" style="width: 100%; text-align: center; display: none;"><img src="<?php echo PATH;?>basis/pic/buttonload.gif"></div><div id="field2_error" class="alert alert-danger" style="display: none; text-align: center;"></div><div id="field2_attempts" class="alert alert-warning" style="display: none; text-align: center;"><span class="attempts_text">Attempts left to answer the control questions</span>:&nbsp;<span id="field2_attempts_num"></span></div></div><script>if(maxFalse!=null) {
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
            if (loopEnd==326673) { showNext('wait326673.php?session_index=<?php echo $_SESSION[sessionID];?>',326674,326673);}
            else {showNext('stage326674.php?session_index=<?php echo $_SESSION[sessionID];?>',326674,326673);}

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
            if (loopEnd==326673) { showNext('wait326673.php?session_index=<?php echo $_SESSION[sessionID];?>',326672,326673);}
            else {showNext('stage326672.php?session_index=<?php echo $_SESSION[sessionID];?>',326672,326673);}

            };</script></div><script>if((true)) { $('#wrap3').show(); $('#buttonclick3').addClass('buttonclick');} </script><!-- END Element 3 Type: 18-->
        
        </div><script>setInterval(function(){ if (true) $('#wrap1').show();if (!(true)) $('#wrap1').hide();if (true) $('#wrap2').show();if (!(true)) $('#wrap2').hide();if (true) $('#wrap3').show();if (!(true)) $('#wrap3').hide(); }, 100);</script></form></div></div></body></html>