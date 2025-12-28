<html>
        <head>
        
        <?php
    
        include("_projectID.php");
        include(PATH."basis/participant/header.php");
	    $_SESSION['projectID']=PROJECTID;
	    
	    ?>

        <link href="<?php echo PATH;?>basis/css/newlayout.css?v1" rel="stylesheet" type="text/css"  />
        <link href="<?php echo PATH;?>basis/css/newlayout_bootstrap.css" rel="stylesheet" type="text/css"  />
        <link href="<?php echo PATH;?>basis/css/grid.css" rel="stylesheet" type="text/css"  /><title>Questionnaire 1</title>

        <script> var v={}; var wronganswers={}; var totalwronganswers={};var maxFalse = null;
        var firstStageExp = <?php echo json_encode(FIRSTPAGE . ".php"); ?>;
        var thisPage = <?php echo json_encode($thisPage); ?>;
        var sessionIndexJavascript = "<?php echo $_SESSION[sessionID];?>";
        pageRefreshed=0;
        var loopBegin = "stage" + loopStart + ".php";
        var afterLoopEnd = 326680;
        if (thisPage == firstStageExp || (thisPage==loopBegin && period > 1) || loopEnd==afterLoopEnd) firstStage();
        /* if (thisPage == firstStageExp || thisPage==loopBegin || loopEnd==afterLoopEnd) firstStage(); */
        TimeOut=null;
        function skipStage(proceedifpossible) {
         if (proceedifpossible === undefined) proceedifpossible = false;
         if (proceedifpossible) location.replace('stage326688.php?session_index=<?php echo $_SESSION[sessionID];?>');
         else location.replace('wait326681.php?session_index=<?php echo $_SESSION[sessionID];?>');
        }
        $(document).ready(function(){
        if (bot) { document.getElementsByClassName("buttonclick")[0].click(); }
        });
        
        </script>
        </head><body><div id="mainwrap" class="container" style="width: 100%; padding-left: 5%; padding-right: 5%; padding-top: 1%;"><form autocomplete="off"><div class="row"><!-- START Element 1 Type: 19-->
        
        
        <script></script><!-- END Element 1 Type: 19-->
        
        <!-- START Element 2 Type: 1-->
        
        <div class="col-sm-12" id="wrap2" style="display: none;"><div class="btnbox2 paddlr" style="text-align: center"><h3>Vragenlijst</h3><p>Het spel dat je net gespeeld hebt bestond uit 5 rondes.<br>In elke ronde zag je een plaatje en schatte je het aantal dieren dat erop stond.<br>Na het invullen van je eerste schatting zag je de schatting van een eerdere deelnemer. <br>Daarna maakte je een <i>tweede&nbsp;</i>schatting.</p><p></p><p></p></div>
        </div><script>if((true)) { $('#wrap2').show(); } </script><!-- END Element 2 Type: 1-->
        
        <!-- START Element 3 Type: 23-->
        
        <div class="col-sm-12" id="wrap3" style="display: none;"><div class="btnbox2"><div class="form-group "><input type="hidden" id="field3"><script>var confidence1=null;</script><div style="text-align: center"><label for="field3">In het algemeen, hoe <i>zeker</i> voelde jij je over hoe goed je <u>eerste</u> schatting was (voor het zien van de schatting van de eerdere deelnemer)?</label></div><div
            id="button31"

            class="choicebuttons3 btn btn-default" onclick="$('.choicebuttons3').removeClass('btn-primary');
                            $('#button31').addClass('btn-primary');
                             confidence1=1;
                            $('#field3').val(1);">Helemaal niet zeker</div><div
            id="button32"

            class="choicebuttons3 btn btn-default" onclick="$('.choicebuttons3').removeClass('btn-primary');
                            $('#button32').addClass('btn-primary');
                             confidence1=2;
                            $('#field3').val(2);">Een beetje zeker</div><div
            id="button33"

            class="choicebuttons3 btn btn-default" onclick="$('.choicebuttons3').removeClass('btn-primary');
                            $('#button33').addClass('btn-primary');
                             confidence1=3;
                            $('#field3').val(3);">Best wel zeker</div><div
            id="button34"

            class="choicebuttons3 btn btn-default" onclick="$('.choicebuttons3').removeClass('btn-primary');
                            $('#button34').addClass('btn-primary');
                             confidence1=4;
                            $('#field3').val(4);">Heel zeker</div><script>var confidence1_options = [1,2,3,4];
        </script><div id="field3_noEntry" class="messagefield3 alert alert-danger" style="display: none;">Please indicate your response.</div><div id="field3_notcorrect" class="messagefield3 alert alert-danger" style="display: none;">The value you entered is not correct.</div></div></div><script>function checkValue_field3() {
           var label="confidence1";var required=0;var inline=0;var orderoptions=0;var graphical=1;var correct=null;var defaultvalue=null;var multiple=0;var options=null;var clicksave=0;
            if(!(true)) { checker=checker+1; } else {
                var value;
                if (bot) { 
                    if (correct != null) { value = correct; }
                    else if (typeof bot_confidence1 !== 'undefined') { value=bot_confidence1; }
                    else { 
                    var allvalues=["1","2","3","4"];
                    var index=Math.floor(Math.random()*allvalues.length); 
                    value=allvalues[index]; }
                }
                else {
                value=($('#field3').val()); 
                }
                                
                $('.messagefield3').hide();
                allcorrect=checker+1;
                if ((value === null || value == "") && required==1) {
                    $('#field3_noEntry').show();
                }
                else if (value!=correct && correct != null && required!=0) {
                            $('#field3_notcorrect').show();
                        }
                
                else {
                        

                       record("confidence1", value);

                            /* this variable is created in LionElementButton.class */
                           checker = checker+1;


                }
            
            if (allcorrect!=checker) {
                  wronganswers['confidence1']=1;
                       totalwronganswers['confidence1'] = isNaN(totalwronganswers['confidence1']) ? 1 : totalwronganswers['confidence1']+1; 
             
               } else wronganswers['confidence1']=0;
            
            
            }
            
            
            
         }



        </script></div><script>if((true)) { $('#wrap3').show(); } </script><!-- END Element 3 Type: 23-->
        
        <!-- START Element 4 Type: 23-->
        
        <div class="col-sm-12" id="wrap4" style="display: none;"><div class="btnbox2"><div class="form-group "><input type="hidden" id="field4"><script>var confidence2=null;</script><div style="text-align: center"><label for="field4"><br><br>In het algemeen, hoe <i>zeker</i> voelde jij je over hoe goed je <u>tweede</u> schatting was?</label></div><div
            id="button41"

            class="choicebuttons4 btn btn-default" onclick="$('.choicebuttons4').removeClass('btn-primary');
                            $('#button41').addClass('btn-primary');
                             confidence2=1;
                            $('#field4').val(1);">Helemaal niet zeker</div><div
            id="button42"

            class="choicebuttons4 btn btn-default" onclick="$('.choicebuttons4').removeClass('btn-primary');
                            $('#button42').addClass('btn-primary');
                             confidence2=2;
                            $('#field4').val(2);">Een beetje zeker</div><div
            id="button43"

            class="choicebuttons4 btn btn-default" onclick="$('.choicebuttons4').removeClass('btn-primary');
                            $('#button43').addClass('btn-primary');
                             confidence2=3;
                            $('#field4').val(3);">Best wel zeker</div><div
            id="button44"

            class="choicebuttons4 btn btn-default" onclick="$('.choicebuttons4').removeClass('btn-primary');
                            $('#button44').addClass('btn-primary');
                             confidence2=4;
                            $('#field4').val(4);">Heel zeker</div><script>var confidence2_options = [1,2,3,4];
        </script><div id="field4_noEntry" class="messagefield4 alert alert-danger" style="display: none;">Please indicate your response.</div><div id="field4_notcorrect" class="messagefield4 alert alert-danger" style="display: none;">The value you entered is not correct.</div></div></div><script>function checkValue_field4() {
           var label="confidence2";var required=0;var inline=0;var orderoptions=0;var graphical=1;var correct=null;var defaultvalue=null;var multiple=0;var options=null;var clicksave=0;
            if(!(true)) { checker=checker+1; } else {
                var value;
                if (bot) { 
                    if (correct != null) { value = correct; }
                    else if (typeof bot_confidence2 !== 'undefined') { value=bot_confidence2; }
                    else { 
                    var allvalues=["1","2","3","4"];
                    var index=Math.floor(Math.random()*allvalues.length); 
                    value=allvalues[index]; }
                }
                else {
                value=($('#field4').val()); 
                }
                                
                $('.messagefield4').hide();
                allcorrect=checker+1;
                if ((value === null || value == "") && required==1) {
                    $('#field4_noEntry').show();
                }
                else if (value!=correct && correct != null && required!=0) {
                            $('#field4_notcorrect').show();
                        }
                
                else {
                        

                       record("confidence2", value);

                            /* this variable is created in LionElementButton.class */
                           checker = checker+1;


                }
            
            if (allcorrect!=checker) {
                  wronganswers['confidence2']=1;
                       totalwronganswers['confidence2'] = isNaN(totalwronganswers['confidence2']) ? 1 : totalwronganswers['confidence2']+1; 
             
               } else wronganswers['confidence2']=0;
            
            
            }
            
            
            
         }



        </script></div><script>if((true)) { $('#wrap4').show(); } </script><!-- END Element 4 Type: 23-->
        
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
            if (loopEnd==326681) { showNext('wait326681.php?session_index=<?php echo $_SESSION[sessionID];?>',326688,326681);}
            else {showNext('stage326688.php?session_index=<?php echo $_SESSION[sessionID];?>',326688,326681);}

            };</script></div><script>if((true)) { $('#wrap5').show(); $('#buttonclick5').addClass('buttonclick');} </script><!-- END Element 5 Type: 18-->
        
        </div><script>setInterval(function(){ if (true) $('#wrap2').show();if (!(true)) $('#wrap2').hide();if (true) $('#wrap3').show();if (!(true)) $('#wrap3').hide();if (true) $('#wrap4').show();if (!(true)) $('#wrap4').hide();if (true) $('#wrap5').show();if (!(true)) $('#wrap5').hide(); }, 100);</script></form></div></div></body></html>