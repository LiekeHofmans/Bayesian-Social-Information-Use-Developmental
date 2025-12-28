<html>
        <head>
        
        <?php
    
        include("_projectID.php");
        include(PATH."basis/participant/header.php");
	    $_SESSION['projectID']=PROJECTID;
	    
	    ?>

        <link href="<?php echo PATH;?>basis/css/newlayout.css?v1" rel="stylesheet" type="text/css"  />
        <link href="<?php echo PATH;?>basis/css/newlayout_bootstrap.css" rel="stylesheet" type="text/css"  />
        <link href="<?php echo PATH;?>basis/css/grid.css" rel="stylesheet" type="text/css"  /><title>quiz R</title>

        <script> var v={}; var wronganswers={}; var totalwronganswers={};var maxFalse = null;
        var firstStageExp = <?php echo json_encode(FIRSTPAGE . ".php"); ?>;
        var thisPage = <?php echo json_encode($thisPage); ?>;
        var sessionIndexJavascript = "<?php echo $_SESSION[sessionID];?>";
        pageRefreshed=0;
        var loopBegin = "stage" + loopStart + ".php";
        var afterLoopEnd = 326673;
        if (thisPage == firstStageExp || (thisPage==loopBegin && period > 1) || loopEnd==afterLoopEnd) firstStage();
        /* if (thisPage == firstStageExp || thisPage==loopBegin || loopEnd==afterLoopEnd) firstStage(); */
        TimeOut=null;
        function skipStage(proceedifpossible) {
         if (proceedifpossible === undefined) proceedifpossible = false;
         if (proceedifpossible) location.replace('stage326675.php?session_index=<?php echo $_SESSION[sessionID];?>');
         else location.replace('wait326674.php?session_index=<?php echo $_SESSION[sessionID];?>');
        }
        $(document).ready(function(){
        if (bot) { document.getElementsByClassName("buttonclick")[0].click(); }
        });
        
        </script>
        </head><body><div id="mainwrap" class="container" style="width: 100%; padding-left: 5%; padding-right: 5%; padding-top: 1%;"><form autocomplete="off"><div class="row"><!-- START Element 1 Type: 1-->
        
        <div class="col-sm-12" id="wrap1" style="display: none;"><div class="btnbox2 paddlr" style="text-align: center"><h3>Controle-vragen</h3><p>Om te controleren of je de taak begrijpt, vragen we je om hieronder aan te geven of de uitspraken kloppen of niet.</p></div>
        </div><script>if((true)) { $('#wrap1').show(); } </script><!-- END Element 1 Type: 1-->
        
        <!-- START Element 2 Type: 23-->
        
        <div class="col-sm-12" id="wrap2" style="display: none;"><div class="btnbox2"><div class="form-group "><input type="hidden" id="field2"><script>var qR1=null;</script><div style="text-align: center"><label for="field2"><b>In iedere ronde van deze taak krijg je een plaatje te zien. Je moet schatten hoeveel dieren er op het plaatje staan.</b></label></div><div
            id="button21"

            class="choicebuttons2 btn btn-default" onclick="$('.choicebuttons2').removeClass('btn-primary');
                            $('#button21').addClass('btn-primary');
                             qR1=1;
                            $('#field2').val(1);">klopt</div><div
            id="button22"

            class="choicebuttons2 btn btn-default" onclick="$('.choicebuttons2').removeClass('btn-primary');
                            $('#button22').addClass('btn-primary');
                             qR1=2;
                            $('#field2').val(2);">klopt niet</div><script>var qR1_options = [1,2];
        </script><div id="field2_noEntry" class="messagefield2 alert alert-danger" style="display: none;">Please indicate your response.</div><div id="field2_notcorrect" class="messagefield2 alert alert-danger" style="display: none;">The value you entered is not correct.</div></div></div><script>function checkValue_field2() {
           var label="qR1";var required=1;var inline=0;var orderoptions=0;var graphical=1;var correct=1;var defaultvalue=null;var multiple=0;var options=null;var clicksave=0;
            if(!(true)) { checker=checker+1; } else {
                var value;
                if (bot) { 
                    if (correct != null) { value = correct; }
                    else if (typeof bot_qR1 !== 'undefined') { value=bot_qR1; }
                    else { 
                    var allvalues=["1","2"];
                    var index=Math.floor(Math.random()*allvalues.length); 
                    value=allvalues[index]; }
                }
                else {
                value=($('#field2').val()); 
                }
                                
                $('.messagefield2').hide();
                allcorrect=checker+1;
                if ((value === null || value == "") && required==1) {
                    $('#field2_noEntry').show();
                }
                else if (value!=correct && correct != null && required!=0) {
                            $('#field2_notcorrect').show();
                        }
                
                else {
                        

                       record("qR1", value);

                            /* this variable is created in LionElementButton.class */
                           checker = checker+1;


                }
            
            if (allcorrect!=checker) {
                  wronganswers['qR1']=1;
                       totalwronganswers['qR1'] = isNaN(totalwronganswers['qR1']) ? 1 : totalwronganswers['qR1']+1; 
             
               } else wronganswers['qR1']=0;
            
            
            }
            
            
            
         }



        </script></div><script>if((true)) { $('#wrap2').show(); } </script><!-- END Element 2 Type: 23-->
        
        <!-- START Element 3 Type: 23-->
        
        <div class="col-sm-12" id="wrap3" style="display: none;"><div class="btnbox2"><div class="form-group "><input type="hidden" id="field3"><script>var qR2=null;</script><div style="text-align: center"><label for="field3"><br><b>Nadat je je schatting hebt ingevuld, zul je de schatting van een eerdere deelnemer zien. Je kunt dan een tweede schatting invullen.</b></label></div><div
            id="button31"

            class="choicebuttons3 btn btn-default" onclick="$('.choicebuttons3').removeClass('btn-primary');
                            $('#button31').addClass('btn-primary');
                             qR2=1;
                            $('#field3').val(1);">klopt</div><div
            id="button32"

            class="choicebuttons3 btn btn-default" onclick="$('.choicebuttons3').removeClass('btn-primary');
                            $('#button32').addClass('btn-primary');
                             qR2=2;
                            $('#field3').val(2);">klopt niet</div><script>var qR2_options = [1,2];
        </script><div id="field3_noEntry" class="messagefield3 alert alert-danger" style="display: none;">Please indicate your response.</div><div id="field3_notcorrect" class="messagefield3 alert alert-danger" style="display: none;">The value you entered is not correct.</div></div></div><script>function checkValue_field3() {
           var label="qR2";var required=1;var inline=0;var orderoptions=0;var graphical=1;var correct=1;var defaultvalue=null;var multiple=0;var options=null;var clicksave=0;
            if(!(true)) { checker=checker+1; } else {
                var value;
                if (bot) { 
                    if (correct != null) { value = correct; }
                    else if (typeof bot_qR2 !== 'undefined') { value=bot_qR2; }
                    else { 
                    var allvalues=["1","2"];
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
                        

                       record("qR2", value);

                            /* this variable is created in LionElementButton.class */
                           checker = checker+1;


                }
            
            if (allcorrect!=checker) {
                  wronganswers['qR2']=1;
                       totalwronganswers['qR2'] = isNaN(totalwronganswers['qR2']) ? 1 : totalwronganswers['qR2']+1; 
             
               } else wronganswers['qR2']=0;
            
            
            }
            
            
            
         }



        </script></div><script>if((true)) { $('#wrap3').show(); } </script><!-- END Element 3 Type: 23-->
        
        <!-- START Element 4 Type: 23-->
        
        <div class="col-sm-12" id="wrap4" style="display: none;"><div class="btnbox2"><div class="form-group "><input type="hidden" id="field4"><script>var qR3=null;</script><div style="text-align: center"><label for="field4"><br><b>Hoe preciezer je schattingen, hoe meer bonus je kunt verdienen.</b></label></div><div
            id="button41"

            class="choicebuttons4 btn btn-default" onclick="$('.choicebuttons4').removeClass('btn-primary');
                            $('#button41').addClass('btn-primary');
                             qR3=1;
                            $('#field4').val(1);">klopt</div><div
            id="button42"

            class="choicebuttons4 btn btn-default" onclick="$('.choicebuttons4').removeClass('btn-primary');
                            $('#button42').addClass('btn-primary');
                             qR3=2;
                            $('#field4').val(2);">klopt niet</div><script>var qR3_options = [1,2];
        </script><div id="field4_noEntry" class="messagefield4 alert alert-danger" style="display: none;">Please indicate your response.</div><div id="field4_notcorrect" class="messagefield4 alert alert-danger" style="display: none;">The value you entered is not correct.</div></div></div><script>function checkValue_field4() {
           var label="qR3";var required=1;var inline=0;var orderoptions=0;var graphical=1;var correct=1;var defaultvalue=null;var multiple=0;var options=null;var clicksave=0;
            if(!(true)) { checker=checker+1; } else {
                var value;
                if (bot) { 
                    if (correct != null) { value = correct; }
                    else if (typeof bot_qR3 !== 'undefined') { value=bot_qR3; }
                    else { 
                    var allvalues=["1","2"];
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
                        

                       record("qR3", value);

                            /* this variable is created in LionElementButton.class */
                           checker = checker+1;


                }
            
            if (allcorrect!=checker) {
                  wronganswers['qR3']=1;
                       totalwronganswers['qR3'] = isNaN(totalwronganswers['qR3']) ? 1 : totalwronganswers['qR3']+1; 
             
               } else wronganswers['qR3']=0;
            
            
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

       



        function checkFail() {var numFails=quizFail(playerNr,0,wronganswers);
            console.log(numFails);
            if (numFails>=maxFalse && maxFalse!=null) location.replace(path+'participant/terminated.php?m=<?php echo base64_encode(serialize(array('messageNr'=>8,'playerNr'=>$playerNr,'projectID'=>PROJECTID))); ?>');
            if (maxFalse!=null && numFails<=maxFalse) $('#field5_attempts_num').html(maxFalse-numFails);
            } function toNextPage5() {
            if (loopEnd==326674) { showNext('wait326674.php?session_index=<?php echo $_SESSION[sessionID];?>',326675,326674);}
            else {showNext('stage326675.php?session_index=<?php echo $_SESSION[sessionID];?>',326675,326674);}

            };</script></div><script>if((true)) { $('#wrap5').show(); $('#buttonclick5').addClass('buttonclick');} </script><!-- END Element 5 Type: 18-->
        
        <!-- START Element 6 Type: 25-->
        
        <div class="col-sm-12" id="wrap6" style="display: none;"><div  id="button6">
        <div id="buttonclick6" class="lionessbutton btn btn-default btn-lg btn-block" onclick="toNextPage6();">Terug naar de instructies</div></div><script>



      


         function toNextPage6() {
            showNext('stage326673.php?session_index=<?php echo $_SESSION[sessionID];?>',326673,326674);

            };</script></div><script>if((true)) { $('#wrap6').show(); } </script><!-- END Element 6 Type: 25-->
        
        </div><script>setInterval(function(){ if (true) $('#wrap1').show();if (!(true)) $('#wrap1').hide();if (true) $('#wrap2').show();if (!(true)) $('#wrap2').hide();if (true) $('#wrap3').show();if (!(true)) $('#wrap3').hide();if (true) $('#wrap4').show();if (!(true)) $('#wrap4').hide();if (true) $('#wrap5').show();if (!(true)) $('#wrap5').hide();if (true) $('#wrap6').show();if (!(true)) $('#wrap6').hide(); }, 100);</script></form></div></div></body></html>