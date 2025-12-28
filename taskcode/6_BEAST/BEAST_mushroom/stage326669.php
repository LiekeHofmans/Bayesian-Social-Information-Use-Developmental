<html>
        <head>
        
        <?php
    
        include("_projectID.php");
        include(PATH."basis/participant/header.php");
	    $_SESSION['projectID']=PROJECTID;
	    
	    ?>

        <link href="<?php echo PATH;?>basis/css/newlayout.css?v1" rel="stylesheet" type="text/css"  />
        <link href="<?php echo PATH;?>basis/css/newlayout_bootstrap.css" rel="stylesheet" type="text/css"  />
        <link href="<?php echo PATH;?>basis/css/grid.css" rel="stylesheet" type="text/css"  /><title>welcome</title>

        <script> var v={}; var wronganswers={}; var totalwronganswers={};var maxFalse = null;
        var firstStageExp = <?php echo json_encode(FIRSTPAGE . ".php"); ?>;
        var thisPage = <?php echo json_encode($thisPage); ?>;
        var sessionIndexJavascript = "<?php echo $_SESSION[sessionID];?>";
        pageRefreshed=0;
        var loopBegin = "stage" + loopStart + ".php";
        var afterLoopEnd = null;
        if (thisPage == firstStageExp || (thisPage==loopBegin && period > 1) || loopEnd==afterLoopEnd) firstStage();
        /* if (thisPage == firstStageExp || thisPage==loopBegin || loopEnd==afterLoopEnd) firstStage(); */
        TimeOut=null;
        function skipStage(proceedifpossible) {
         if (proceedifpossible === undefined) proceedifpossible = false;
         if (proceedifpossible) location.replace('stage326705.php?session_index=<?php echo $_SESSION[sessionID];?>');
         else location.replace('wait326669.php?session_index=<?php echo $_SESSION[sessionID];?>');
        }
        $(document).ready(function(){
        if (bot) { document.getElementsByClassName("buttonclick")[0].click(); }
        });
        
        </script>
        </head><body><div id="mainwrap" class="container" style="width: 100%; padding-left: 5%; padding-right: 5%; padding-top: 1%;"><form autocomplete="off"><div class="row"><!-- START Element 1 Type: 19-->
        
        
        <script>record('iteration',1)

var animal_names = ['ants', 'bees','flamingos', 'cranes', 'crickets'];

pics=[];
for (var i=0; i<animal_names.length; i++){
    pics[i] = new Image();
    pics[i].src =  'pics/'+animal_names[i]+'_small.png';
}

feeT = '$'+parseFloat(participationFee).toFixed(2);

relDec = Math.ceil(Math.random() * 5);
record('relevantDecision', relDec);
relAorB= 1+ Math.ceil(Math.random());
record('relevantAorB', relAorB);</script><!-- END Element 1 Type: 19-->
        
        <!-- START Element 2 Type: 24-->
        
        <div class="col-sm-12" id="wrap2" style="display: none;"><div class="form-group btnbox2" ><label for="field2"><hr>Vul het Subject ID in om te taak te starten.</label><textarea  id="field2" style="text-align: center; width: 100%" rows="2" name="bid2" onkeyup="subjectID = this.form.bid2.value; " class="btntextfield form-control"></textarea><div id="field2_minmax" class="alert alert-danger" style="display: none;">Please enter a text with between 1 and 50 
        characters.</div><div id="field2_noNumber" class="alert alert-danger" style="display: none;">Please enter a text.</div><script>
            var subjectID=null;
            
            
            function checkValue_field2() {
        

        var label="subjectID";var min=1;var max=50;var rows=2;var required=1;var hideremain=1;

        
            if(!(true)) { checker=checker+1; } else {
            
                if (bot) { 
                    if (typeof bot_subjectID !== 'undefined') { value=bot_subjectID; }
                    else { stringlength=Math.floor(Math.random()*max)+min; 
                        var basestring='i am a bot. ';
                        if (max<3) { value='-'; }
                        else if (max<basestring.length) { value='bot'; }
                        else { value=''; 
                            for (var j=0; j<=(stringlength); j=j+basestring.length) {
                            
                                value=value+basestring;
                            }
                        }
                    }
                value_unencoded=value;
                } else {
                value_unencoded = $('#field2').val(); 
                value=encodeURI(value_unencoded);
                 
                }
            
            
               
                /* check if any entry has been made */
                if ((value == "") && required==1 && min>0) {
                    $('#field2_noNumber').show();
                }
                else {
                    $('#field2_noNumber').hide();
                    


                    
                   
                        if (value_unencoded.length>max || value_unencoded.length < min) {
                            $('#field2_minmax').show();
                        }
                        else { $('#field2_minmax').hide();

                       


                            record("subjectID",decodeURI(value));

                            /* this variable is created in LionElementButton.class */
                           checker = checker+1;
                       
                   }
               }
            }

}

        </script></div></div><script>if((true)) { $('#wrap2').show(); } </script><!-- END Element 2 Type: 24-->
        
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
        ">Ga verder</div><div id="buttonload3" style="width: 100%; text-align: center; display: none;"><img src="<?php echo PATH;?>basis/pic/buttonload.gif"></div><div id="field3_error" class="alert alert-danger" style="display: none; text-align: center;"></div><div id="field3_attempts" class="alert alert-warning" style="display: none; text-align: center;"><span class="attempts_text">Attempts left to answer the control questions</span>:&nbsp;<span id="field3_attempts_num"></span></div></div><script>if(maxFalse!=null) {
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
        
        function additionalCheck3() {setValue('session', 'playerNr='+playerNr, 'externalID', subjectID);

           return true;
        }

       



        function checkFail() {} function toNextPage3() {
            if (loopEnd==326669) { showNext('wait326669.php?session_index=<?php echo $_SESSION[sessionID];?>',326705,326669);}
            else {showNext('stage326705.php?session_index=<?php echo $_SESSION[sessionID];?>',326705,326669);}

            };</script></div><script>if((true)) { $('#wrap3').show(); $('#buttonclick3').addClass('buttonclick');} </script><!-- END Element 3 Type: 18-->
        
        </div><script>setInterval(function(){ if (true) $('#wrap2').show();if (!(true)) $('#wrap2').hide();if (true) $('#wrap3').show();if (!(true)) $('#wrap3').hide(); }, 100);</script></form></div></div></body></html>