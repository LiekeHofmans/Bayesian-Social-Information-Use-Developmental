<html>
        <head>
        
        <?php
    
        include("_projectID.php");
        include(PATH."basis/participant/header.php");
	    $_SESSION['projectID']=PROJECTID;
	    
	    ?>

        <link href="<?php echo PATH;?>basis/css/newlayout.css?v1" rel="stylesheet" type="text/css"  />
        <link href="<?php echo PATH;?>basis/css/newlayout_bootstrap.css" rel="stylesheet" type="text/css"  />
        <link href="<?php echo PATH;?>basis/css/grid.css" rel="stylesheet" type="text/css"  /><title>announce_Q2</title>

        <script> var v={}; var wronganswers={}; var totalwronganswers={};var maxFalse = null;
        var firstStageExp = <?php echo json_encode(FIRSTPAGE . ".php"); ?>;
        var thisPage = <?php echo json_encode($thisPage); ?>;
        var sessionIndexJavascript = "<?php echo $_SESSION[sessionID];?>";
        pageRefreshed=0;
        var loopBegin = "stage" + loopStart + ".php";
        var afterLoopEnd = 326681;
        if (thisPage == firstStageExp || (thisPage==loopBegin && period > 1) || loopEnd==afterLoopEnd) firstStage();
        /* if (thisPage == firstStageExp || thisPage==loopBegin || loopEnd==afterLoopEnd) firstStage(); */
        TimeOut=null;
        function skipStage(proceedifpossible) {
         if (proceedifpossible === undefined) proceedifpossible = false;
         if (proceedifpossible) location.replace('stage326683.php?session_index=<?php echo $_SESSION[sessionID];?>');
         else location.replace('wait326682.php?session_index=<?php echo $_SESSION[sessionID];?>');
        }
        $(document).ready(function(){
        if (bot) { document.getElementsByClassName("buttonclick")[0].click(); }
        });
        
        </script>
        </head><body><div id="mainwrap" class="container" style="width: 100%; padding-left: 5%; padding-right: 5%; padding-top: 1%;"><form autocomplete="off"><div class="row"><!-- START Element 1 Type: 1-->
        
        <div class="col-sm-12" id="wrap1" style="display: none;"><div class="btnbox2 paddlr" style="text-align: center"><h3>Questionnaire part 2 of 4</h3><p>The second part of this questionnaire is about yourself.&nbsp;</p><p>Before any analysis of your responses takes place, the data will be <u>anonymized</u>. We&nbsp;will only use this data for analysis at the group level. <br>This procedure implies that we will <u>not be able to link your responses to your identity</u>. <br><b>Note: you can leave any item open if you prefer not to answer it.</b></p></div>
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
        ">Continue</div><div id="buttonload2" style="width: 100%; text-align: center; display: none;"><img src="<?php echo PATH;?>basis/pic/buttonload.gif"></div><div id="field2_error" class="alert alert-danger" style="display: none; text-align: center;"></div><div id="field2_attempts" class="alert alert-warning" style="display: none; text-align: center;"><span class="attempts_text">Attempts left to answer the control questions</span>:&nbsp;<span id="field2_attempts_num"></span></div></div><script>if(maxFalse!=null) {
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
            if (loopEnd==326682) { showNext('wait326682.php?session_index=<?php echo $_SESSION[sessionID];?>',326683,326682);}
            else {showNext('stage326683.php?session_index=<?php echo $_SESSION[sessionID];?>',326683,326682);}

            };</script></div><script>if((true)) { $('#wrap2').show(); $('#buttonclick2').addClass('buttonclick');} </script><!-- END Element 2 Type: 18-->
        
        </div><script>setInterval(function(){ if (true) $('#wrap1').show();if (!(true)) $('#wrap1').hide();if (true) $('#wrap2').show();if (!(true)) $('#wrap2').hide(); }, 100);</script></form></div></div></body></html>