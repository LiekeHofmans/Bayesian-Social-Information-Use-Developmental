<html>
        <head>
        
        <?php
    
        include("_projectID.php");
        include(PATH."basis/participant/header.php");
	    $_SESSION['projectID']=PROJECTID;
	    
	    ?>

        <link href="<?php echo PATH;?>basis/css/newlayout.css?v1" rel="stylesheet" type="text/css"  />
        <link href="<?php echo PATH;?>basis/css/newlayout_bootstrap.css" rel="stylesheet" type="text/css"  />
        <link href="<?php echo PATH;?>basis/css/grid.css" rel="stylesheet" type="text/css"  /><title>finished task</title>

        <script> var v={}; var wronganswers={}; var totalwronganswers={};var maxFalse = null;
        var firstStageExp = <?php echo json_encode(FIRSTPAGE . ".php"); ?>;
        var thisPage = <?php echo json_encode($thisPage); ?>;
        var sessionIndexJavascript = "<?php echo $_SESSION[sessionID];?>";
        pageRefreshed=0;
        var loopBegin = "stage" + loopStart + ".php";
        var afterLoopEnd = 326679;
        if (thisPage == firstStageExp || (thisPage==loopBegin && period > 1) || loopEnd==afterLoopEnd) firstStage();
        /* if (thisPage == firstStageExp || thisPage==loopBegin || loopEnd==afterLoopEnd) firstStage(); */
        TimeOut=null;
        function skipStage(proceedifpossible) {
         if (proceedifpossible === undefined) proceedifpossible = false;
         if (proceedifpossible) location.replace('stage326681.php?session_index=<?php echo $_SESSION[sessionID];?>');
         else location.replace('wait326680.php?session_index=<?php echo $_SESSION[sessionID];?>');
        }
        $(document).ready(function(){
        if (bot) { document.getElementsByClassName("buttonclick")[0].click(); }
        });
        
        </script>
        </head><body><div id="mainwrap" class="container" style="width: 100%; padding-left: 5%; padding-right: 5%; padding-top: 1%;"><form autocomplete="off"><div class="row"><!-- START Element 1 Type: 19-->
        
        
        <script>//earnings
relevantDec = getValue('decisions', 'playerNr='+playerNr+' and period=1','relevantDecision');
relevantRound = Math.ceil(relevantDec);
relevantBlock = 1;
relevantRoundInBlock = 1 + (relevantRound-1)%5;
relevantAorB = getValue('decisions', 'playerNr='+playerNr+' and period=1','relevantAorB');

// get relevant decision and correct answer
var animal_names =['mieren', 'bijen', 'flamingo&#8217;s', 'kraanvogels', 'krekels'];
var corrAnsw = [93,78,59,74,69];
var thisCorr = corrAnsw[relevantRoundInBlock-1];

var relevantAnimal = animal_names[relevantRoundInBlock-1];
relevantVarName = 'estimate';
AorB = 'A';

if (relevantAorB==2) {
    relevantVarName = 'estimate_revised';
    AorB = 'B';
}

// calculate earnings
var est = getValue('decisions', 'playerNr='+playerNr+ ' and period='+relevantRound, relevantVarName);
var deviation = Math.abs(est - thisCorr);
var subtraction = Math.min(100, 5 * deviation);
//points = Math.max(100 - Math.pow(deviation,2), 0);
points = Math.max(100 - deviation * 5, 0).toFixed(0);

record('points', points)

record('bonusPaymentIfSelected', points)

var dollars = points * parseFloat(exchangeRate);
dollars = Math.min(dollars,1); // do not let payment go above 1
dollarsT = '€'+dollars.toFixed(2);
record('dollarsT', dollarsT);
setBonus(dollars);</script><!-- END Element 1 Type: 19-->
        
        <!-- START Element 2 Type: 1-->
        
        <div class="col-sm-12" id="wrap2" style="display: none;"><div class="btnbox2 paddlr" style="text-align: center"><h3><span style="color: inherit; font-family: inherit; background-color: rgba(223, 240, 216, 0);">Dit is het einde van het dierenspel!</span><br></h3><p>De computer heeft willekeurig ronde <script>document.write(relevantRoundInBlock)</script>, deel <script>document.write(AorB)</script> uitgekozen om jouw bonus te berekenen.<br></p><p>In die ronde had je geschat dat er <b><script>document.write(est)</script> <script>document.write(relevantAnimal)</script></b> op het plaatje stonden. <br>Het goede aantal <script>document.write(relevantAnimal)</script> was <b><script>document.write(thisCorr)</script></b>.&nbsp;</p><p>Dit betekent dat jouw schatting er <script>document.write(deviation)</script> naast zat.<br>Voor een schatting die precies goed was zou je €1,00 verdienen, en voor elk dier ernaast trekken we €0,05 af.</p><p>Dus, je bonus voor dit spel is: <b><script>document.write(dollarsT)</script></b></p><p><span style="background-color: initial;">
</span></p><hr>
<p></p><p><span style="background-color: initial;">We eindigen de taak met een korte vragenlijst over hoe jij je beslissingen in dit spel hebt genomen.<br></span></p><p></p><p></p></div>
        </div><script>if((true)) { $('#wrap2').show(); } </script><!-- END Element 2 Type: 1-->
        
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
        ">Ga verder naar de vragenlijst</div><div id="buttonload3" style="width: 100%; text-align: center; display: none;"><img src="<?php echo PATH;?>basis/pic/buttonload.gif"></div><div id="field3_error" class="alert alert-danger" style="display: none; text-align: center;"></div><div id="field3_attempts" class="alert alert-warning" style="display: none; text-align: center;"><span class="attempts_text">Attempts left to answer the control questions</span>:&nbsp;<span id="field3_attempts_num"></span></div></div><script>if(maxFalse!=null) {
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
            if (loopEnd==326680) { showNext('wait326680.php?session_index=<?php echo $_SESSION[sessionID];?>',326681,326680);}
            else {showNext('stage326681.php?session_index=<?php echo $_SESSION[sessionID];?>',326681,326680);}

            };</script></div><script>if((true)) { $('#wrap3').show(); $('#buttonclick3').addClass('buttonclick');} </script><!-- END Element 3 Type: 18-->
        
        </div><script>setInterval(function(){ if (true) $('#wrap2').show();if (!(true)) $('#wrap2').hide();if (true) $('#wrap3').show();if (!(true)) $('#wrap3').hide(); }, 100);</script></form></div></div></body></html>