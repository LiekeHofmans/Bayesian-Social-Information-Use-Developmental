<html>
        <head>
        
        <?php
    
        include("_projectID.php");
        include(PATH."basis/participant/header.php");
	    $_SESSION['projectID']=PROJECTID;
	    
	    ?>

        <link href="<?php echo PATH;?>basis/css/newlayout.css?v1" rel="stylesheet" type="text/css"  />
        <link href="<?php echo PATH;?>basis/css/newlayout_bootstrap.css" rel="stylesheet" type="text/css"  />
        <link href="<?php echo PATH;?>basis/css/grid.css" rel="stylesheet" type="text/css"  /><title>Questionnaire 5</title>

        <script> var v={}; var wronganswers={}; var totalwronganswers={};var maxFalse = null;
        var firstStageExp = <?php echo json_encode(FIRSTPAGE . ".php"); ?>;
        var thisPage = <?php echo json_encode($thisPage); ?>;
        var sessionIndexJavascript = "<?php echo $_SESSION[sessionID];?>";
        pageRefreshed=0;
        var loopBegin = "stage" + loopStart + ".php";
        var afterLoopEnd = 326686;
        if (thisPage == firstStageExp || (thisPage==loopBegin && period > 1) || loopEnd==afterLoopEnd) firstStage();
        /* if (thisPage == firstStageExp || thisPage==loopBegin || loopEnd==afterLoopEnd) firstStage(); */
        TimeOut=null;
        function skipStage(proceedifpossible) {
         if (proceedifpossible === undefined) proceedifpossible = false;
         if (proceedifpossible) location.replace('stage326688.php?session_index=<?php echo $_SESSION[sessionID];?>');
         else location.replace('wait326687.php?session_index=<?php echo $_SESSION[sessionID];?>');
        }
        $(document).ready(function(){
        if (bot) { document.getElementsByClassName("buttonclick")[0].click(); }
        });
        
        </script>
        </head><body><div id="mainwrap" class="container" style="width: 100%; padding-left: 5%; padding-right: 5%; padding-top: 1%;"><form autocomplete="off"><div class="row"><!-- START Element 1 Type: 19-->
        
        
        <script></script><!-- END Element 1 Type: 19-->
        
        <!-- START Element 2 Type: 1-->
        
        <div class="col-sm-12" id="wrap2" style="display: none;"><div class="btnbox2 paddlr" style="text-align: center"><h3>Questionnaire 3/5
</h3><p></p><p>Please use the following scale to indicate the degree of your agreement or disagreement with each of the 11 statements below.<br>Record your answer by clicking on the buttons.<br>Try to describe yourself accurately and generally <br>(that is, the way you are actually in most situations - not the way you would hope to be).</p></div>
        </div><script>if((true)) { $('#wrap2').show(); } </script><!-- END Element 2 Type: 1-->
        
        <!-- START Element 3 Type: 23-->
        
        <div class="col-sm-12" id="wrap3" style="display: none;"><div class="btnbox2"><div class="form-group "><input type="hidden" id="field3"><script>var conf1=null;</script><div style="text-align: center"><label for="field3"><b>1. I often rely on, and act upon, the advice of others.</b></label></div><div
            id="button31"

            class="choicebuttons3 btn btn-default" onclick="$('.choicebuttons3').removeClass('btn-primary');
                            $('#button31').addClass('btn-primary');
                             conf1=1;
                            $('#field3').val(1);">very strong disagreement</div><div
            id="button32"

            class="choicebuttons3 btn btn-default" onclick="$('.choicebuttons3').removeClass('btn-primary');
                            $('#button32').addClass('btn-primary');
                             conf1=2;
                            $('#field3').val(2);">strong disagreement</div><div
            id="button33"

            class="choicebuttons3 btn btn-default" onclick="$('.choicebuttons3').removeClass('btn-primary');
                            $('#button33').addClass('btn-primary');
                             conf1=3;
                            $('#field3').val(3);">moderate disagreement</div><div
            id="button34"

            class="choicebuttons3 btn btn-default" onclick="$('.choicebuttons3').removeClass('btn-primary');
                            $('#button34').addClass('btn-primary');
                             conf1=4;
                            $('#field3').val(4);">slight disagreement</div><div
            id="button35"

            class="choicebuttons3 btn btn-default" onclick="$('.choicebuttons3').removeClass('btn-primary');
                            $('#button35').addClass('btn-primary');
                             conf1=5;
                            $('#field3').val(5);">neither agreement nor disagreement</div><div
            id="button36"

            class="choicebuttons3 btn btn-default" onclick="$('.choicebuttons3').removeClass('btn-primary');
                            $('#button36').addClass('btn-primary');
                             conf1=6;
                            $('#field3').val(6);">slight agreement</div><div
            id="button37"

            class="choicebuttons3 btn btn-default" onclick="$('.choicebuttons3').removeClass('btn-primary');
                            $('#button37').addClass('btn-primary');
                             conf1=7;
                            $('#field3').val(7);">moderate agreement</div><div
            id="button38"

            class="choicebuttons3 btn btn-default" onclick="$('.choicebuttons3').removeClass('btn-primary');
                            $('#button38').addClass('btn-primary');
                             conf1=8;
                            $('#field3').val(8);">strong agreement</div><div
            id="button39"

            class="choicebuttons3 btn btn-default" onclick="$('.choicebuttons3').removeClass('btn-primary');
                            $('#button39').addClass('btn-primary');
                             conf1=9;
                            $('#field3').val(9);">very strong agreement</div><script>var conf1_options = [1,2,3,4,5,6,7,8,9];
        </script><div id="field3_noEntry" class="messagefield3 alert alert-danger" style="display: none;">Please indicate your response.</div><div id="field3_notcorrect" class="messagefield3 alert alert-danger" style="display: none;">The value you entered is not correct.</div></div></div><script>function checkValue_field3() {
           var label="conf1";var required=1;var inline=0;var orderoptions=0;var graphical=1;var correct=null;var defaultvalue=null;var multiple=null;var options=null;var clicksave=null;
            if(!(true)) { checker=checker+1; } else {
                var value;
                if (bot) { 
                    if (correct != null) { value = correct; }
                    else if (typeof bot_conf1 !== 'undefined') { value=bot_conf1; }
                    else { 
                    var allvalues=["1","2","3","4","5","6","7","8","9"];
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
                        

                       record("conf1", value);

                            /* this variable is created in LionElementButton.class */
                           checker = checker+1;


                }
            
            if (allcorrect!=checker) {
                  wronganswers['conf1']=1;
                       totalwronganswers['conf1'] = isNaN(totalwronganswers['conf1']) ? 1 : totalwronganswers['conf1']+1; 
             
               } else wronganswers['conf1']=0;
            
            
            }
            
            
            
         }



        </script></div><script>if((true)) { $('#wrap3').show(); } </script><!-- END Element 3 Type: 23-->
        
        <!-- START Element 4 Type: 23-->
        
        <div class="col-sm-12" id="wrap4" style="display: none;"><div class="btnbox2"><div class="form-group "><input type="hidden" id="field4"><script>var conf2=null;</script><div style="text-align: center"><label for="field4"><br><b>2. I would be the last one to change my opinion in a heated argument on a controversial topic.</b></label></div><div
            id="button41"

            class="choicebuttons4 btn btn-default" onclick="$('.choicebuttons4').removeClass('btn-primary');
                            $('#button41').addClass('btn-primary');
                             conf2=1;
                            $('#field4').val(1);">very strong disagreement</div><div
            id="button42"

            class="choicebuttons4 btn btn-default" onclick="$('.choicebuttons4').removeClass('btn-primary');
                            $('#button42').addClass('btn-primary');
                             conf2=2;
                            $('#field4').val(2);">strong disagreement</div><div
            id="button43"

            class="choicebuttons4 btn btn-default" onclick="$('.choicebuttons4').removeClass('btn-primary');
                            $('#button43').addClass('btn-primary');
                             conf2=3;
                            $('#field4').val(3);">moderate disagreement</div><div
            id="button44"

            class="choicebuttons4 btn btn-default" onclick="$('.choicebuttons4').removeClass('btn-primary');
                            $('#button44').addClass('btn-primary');
                             conf2=4;
                            $('#field4').val(4);">slight disagreement</div><div
            id="button45"

            class="choicebuttons4 btn btn-default" onclick="$('.choicebuttons4').removeClass('btn-primary');
                            $('#button45').addClass('btn-primary');
                             conf2=5;
                            $('#field4').val(5);">neither agreement nor disagreement</div><div
            id="button46"

            class="choicebuttons4 btn btn-default" onclick="$('.choicebuttons4').removeClass('btn-primary');
                            $('#button46').addClass('btn-primary');
                             conf2=6;
                            $('#field4').val(6);">slight agreement</div><div
            id="button47"

            class="choicebuttons4 btn btn-default" onclick="$('.choicebuttons4').removeClass('btn-primary');
                            $('#button47').addClass('btn-primary');
                             conf2=7;
                            $('#field4').val(7);">moderate agreement</div><div
            id="button48"

            class="choicebuttons4 btn btn-default" onclick="$('.choicebuttons4').removeClass('btn-primary');
                            $('#button48').addClass('btn-primary');
                             conf2=8;
                            $('#field4').val(8);">strong agreement</div><div
            id="button49"

            class="choicebuttons4 btn btn-default" onclick="$('.choicebuttons4').removeClass('btn-primary');
                            $('#button49').addClass('btn-primary');
                             conf2=9;
                            $('#field4').val(9);">very strong agreement</div><script>var conf2_options = [1,2,3,4,5,6,7,8,9];
        </script><div id="field4_noEntry" class="messagefield4 alert alert-danger" style="display: none;">Please indicate your response.</div><div id="field4_notcorrect" class="messagefield4 alert alert-danger" style="display: none;">The value you entered is not correct.</div></div></div><script>function checkValue_field4() {
           var label="conf2";var required=1;var inline=0;var orderoptions=0;var graphical=1;var correct=null;var defaultvalue=null;var multiple=null;var options=null;var clicksave=null;
            if(!(true)) { checker=checker+1; } else {
                var value;
                if (bot) { 
                    if (correct != null) { value = correct; }
                    else if (typeof bot_conf2 !== 'undefined') { value=bot_conf2; }
                    else { 
                    var allvalues=["1","2","3","4","5","6","7","8","9"];
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
                        

                       record("conf2", value);

                            /* this variable is created in LionElementButton.class */
                           checker = checker+1;


                }
            
            if (allcorrect!=checker) {
                  wronganswers['conf2']=1;
                       totalwronganswers['conf2'] = isNaN(totalwronganswers['conf2']) ? 1 : totalwronganswers['conf2']+1; 
             
               } else wronganswers['conf2']=0;
            
            
            }
            
            
            
         }



        </script></div><script>if((true)) { $('#wrap4').show(); } </script><!-- END Element 4 Type: 23-->
        
        <!-- START Element 5 Type: 23-->
        
        <div class="col-sm-12" id="wrap5" style="display: none;"><div class="btnbox2"><div class="form-group "><input type="hidden" id="field5"><script>var conf3=null;</script><div style="text-align: center"><label for="field5"><br><b>3. Generally, I&#039;d rather give in and go along for the sake of peace than struggle to have my way.</b></label></div><div
            id="button51"

            class="choicebuttons5 btn btn-default" onclick="$('.choicebuttons5').removeClass('btn-primary');
                            $('#button51').addClass('btn-primary');
                             conf3=1;
                            $('#field5').val(1);">very strong disagreement</div><div
            id="button52"

            class="choicebuttons5 btn btn-default" onclick="$('.choicebuttons5').removeClass('btn-primary');
                            $('#button52').addClass('btn-primary');
                             conf3=2;
                            $('#field5').val(2);">strong disagreement</div><div
            id="button53"

            class="choicebuttons5 btn btn-default" onclick="$('.choicebuttons5').removeClass('btn-primary');
                            $('#button53').addClass('btn-primary');
                             conf3=3;
                            $('#field5').val(3);">moderate disagreement</div><div
            id="button54"

            class="choicebuttons5 btn btn-default" onclick="$('.choicebuttons5').removeClass('btn-primary');
                            $('#button54').addClass('btn-primary');
                             conf3=4;
                            $('#field5').val(4);">slight disagreement</div><div
            id="button55"

            class="choicebuttons5 btn btn-default" onclick="$('.choicebuttons5').removeClass('btn-primary');
                            $('#button55').addClass('btn-primary');
                             conf3=5;
                            $('#field5').val(5);">neither agreement nor disagreement</div><div
            id="button56"

            class="choicebuttons5 btn btn-default" onclick="$('.choicebuttons5').removeClass('btn-primary');
                            $('#button56').addClass('btn-primary');
                             conf3=6;
                            $('#field5').val(6);">slight agreement</div><div
            id="button57"

            class="choicebuttons5 btn btn-default" onclick="$('.choicebuttons5').removeClass('btn-primary');
                            $('#button57').addClass('btn-primary');
                             conf3=7;
                            $('#field5').val(7);">moderate agreement</div><div
            id="button58"

            class="choicebuttons5 btn btn-default" onclick="$('.choicebuttons5').removeClass('btn-primary');
                            $('#button58').addClass('btn-primary');
                             conf3=8;
                            $('#field5').val(8);">strong agreement</div><div
            id="button59"

            class="choicebuttons5 btn btn-default" onclick="$('.choicebuttons5').removeClass('btn-primary');
                            $('#button59').addClass('btn-primary');
                             conf3=9;
                            $('#field5').val(9);">very strong agreement</div><script>var conf3_options = [1,2,3,4,5,6,7,8,9];
        </script><div id="field5_noEntry" class="messagefield5 alert alert-danger" style="display: none;">Please indicate your response.</div><div id="field5_notcorrect" class="messagefield5 alert alert-danger" style="display: none;">The value you entered is not correct.</div></div></div><script>function checkValue_field5() {
           var label="conf3";var required=1;var inline=0;var orderoptions=0;var graphical=1;var correct=null;var defaultvalue=null;var multiple=null;var options=null;var clicksave=null;
            if(!(true)) { checker=checker+1; } else {
                var value;
                if (bot) { 
                    if (correct != null) { value = correct; }
                    else if (typeof bot_conf3 !== 'undefined') { value=bot_conf3; }
                    else { 
                    var allvalues=["1","2","3","4","5","6","7","8","9"];
                    var index=Math.floor(Math.random()*allvalues.length); 
                    value=allvalues[index]; }
                }
                else {
                value=($('#field5').val()); 
                }
                                
                $('.messagefield5').hide();
                allcorrect=checker+1;
                if ((value === null || value == "") && required==1) {
                    $('#field5_noEntry').show();
                }
                else if (value!=correct && correct != null && required!=0) {
                            $('#field5_notcorrect').show();
                        }
                
                else {
                        

                       record("conf3", value);

                            /* this variable is created in LionElementButton.class */
                           checker = checker+1;


                }
            
            if (allcorrect!=checker) {
                  wronganswers['conf3']=1;
                       totalwronganswers['conf3'] = isNaN(totalwronganswers['conf3']) ? 1 : totalwronganswers['conf3']+1; 
             
               } else wronganswers['conf3']=0;
            
            
            }
            
            
            
         }



        </script></div><script>if((true)) { $('#wrap5').show(); } </script><!-- END Element 5 Type: 23-->
        
        <!-- START Element 6 Type: 23-->
        
        <div class="col-sm-12" id="wrap6" style="display: none;"><div class="btnbox2"><div class="form-group "><input type="hidden" id="field6"><script>var conf4=null;</script><div style="text-align: center"><label for="field6"><br><b>4. I tend to follow family tradition in making political decisions.</b></label></div><div
            id="button61"

            class="choicebuttons6 btn btn-default" onclick="$('.choicebuttons6').removeClass('btn-primary');
                            $('#button61').addClass('btn-primary');
                             conf4=1;
                            $('#field6').val(1);">very strong disagreement</div><div
            id="button62"

            class="choicebuttons6 btn btn-default" onclick="$('.choicebuttons6').removeClass('btn-primary');
                            $('#button62').addClass('btn-primary');
                             conf4=2;
                            $('#field6').val(2);">strong disagreement</div><div
            id="button63"

            class="choicebuttons6 btn btn-default" onclick="$('.choicebuttons6').removeClass('btn-primary');
                            $('#button63').addClass('btn-primary');
                             conf4=3;
                            $('#field6').val(3);">moderate disagreement</div><div
            id="button64"

            class="choicebuttons6 btn btn-default" onclick="$('.choicebuttons6').removeClass('btn-primary');
                            $('#button64').addClass('btn-primary');
                             conf4=4;
                            $('#field6').val(4);">slight disagreement</div><div
            id="button65"

            class="choicebuttons6 btn btn-default" onclick="$('.choicebuttons6').removeClass('btn-primary');
                            $('#button65').addClass('btn-primary');
                             conf4=5;
                            $('#field6').val(5);">neither agreement nor disagreement</div><div
            id="button66"

            class="choicebuttons6 btn btn-default" onclick="$('.choicebuttons6').removeClass('btn-primary');
                            $('#button66').addClass('btn-primary');
                             conf4=6;
                            $('#field6').val(6);">slight agreement</div><div
            id="button67"

            class="choicebuttons6 btn btn-default" onclick="$('.choicebuttons6').removeClass('btn-primary');
                            $('#button67').addClass('btn-primary');
                             conf4=7;
                            $('#field6').val(7);">moderate agreement</div><div
            id="button68"

            class="choicebuttons6 btn btn-default" onclick="$('.choicebuttons6').removeClass('btn-primary');
                            $('#button68').addClass('btn-primary');
                             conf4=8;
                            $('#field6').val(8);">strong agreement</div><div
            id="button69"

            class="choicebuttons6 btn btn-default" onclick="$('.choicebuttons6').removeClass('btn-primary');
                            $('#button69').addClass('btn-primary');
                             conf4=9;
                            $('#field6').val(9);">very strong agreement</div><script>var conf4_options = [1,2,3,4,5,6,7,8,9];
        </script><div id="field6_noEntry" class="messagefield6 alert alert-danger" style="display: none;">Please indicate your response.</div><div id="field6_notcorrect" class="messagefield6 alert alert-danger" style="display: none;">The value you entered is not correct.</div></div></div><script>function checkValue_field6() {
           var label="conf4";var required=1;var inline=0;var orderoptions=0;var graphical=1;var correct=null;var defaultvalue=null;var multiple=null;var options=null;var clicksave=null;
            if(!(true)) { checker=checker+1; } else {
                var value;
                if (bot) { 
                    if (correct != null) { value = correct; }
                    else if (typeof bot_conf4 !== 'undefined') { value=bot_conf4; }
                    else { 
                    var allvalues=["1","2","3","4","5","6","7","8","9"];
                    var index=Math.floor(Math.random()*allvalues.length); 
                    value=allvalues[index]; }
                }
                else {
                value=($('#field6').val()); 
                }
                                
                $('.messagefield6').hide();
                allcorrect=checker+1;
                if ((value === null || value == "") && required==1) {
                    $('#field6_noEntry').show();
                }
                else if (value!=correct && correct != null && required!=0) {
                            $('#field6_notcorrect').show();
                        }
                
                else {
                        

                       record("conf4", value);

                            /* this variable is created in LionElementButton.class */
                           checker = checker+1;


                }
            
            if (allcorrect!=checker) {
                  wronganswers['conf4']=1;
                       totalwronganswers['conf4'] = isNaN(totalwronganswers['conf4']) ? 1 : totalwronganswers['conf4']+1; 
             
               } else wronganswers['conf4']=0;
            
            
            }
            
            
            
         }



        </script></div><script>if((true)) { $('#wrap6').show(); } </script><!-- END Element 6 Type: 23-->
        
        <!-- START Element 7 Type: 23-->
        
        <div class="col-sm-12" id="wrap7" style="display: none;"><div class="btnbox2"><div class="form-group "><input type="hidden" id="field7"><script>var conf5=null;</script><div style="text-align: center"><label for="field7"><br><b>5. Basically, my friends are the ones who decide what we do together.</b></label></div><div
            id="button71"

            class="choicebuttons7 btn btn-default" onclick="$('.choicebuttons7').removeClass('btn-primary');
                            $('#button71').addClass('btn-primary');
                             conf5=1;
                            $('#field7').val(1);">very strong disagreement</div><div
            id="button72"

            class="choicebuttons7 btn btn-default" onclick="$('.choicebuttons7').removeClass('btn-primary');
                            $('#button72').addClass('btn-primary');
                             conf5=2;
                            $('#field7').val(2);">strong disagreement</div><div
            id="button73"

            class="choicebuttons7 btn btn-default" onclick="$('.choicebuttons7').removeClass('btn-primary');
                            $('#button73').addClass('btn-primary');
                             conf5=3;
                            $('#field7').val(3);">moderate disagreement</div><div
            id="button74"

            class="choicebuttons7 btn btn-default" onclick="$('.choicebuttons7').removeClass('btn-primary');
                            $('#button74').addClass('btn-primary');
                             conf5=4;
                            $('#field7').val(4);">slight disagreement</div><div
            id="button75"

            class="choicebuttons7 btn btn-default" onclick="$('.choicebuttons7').removeClass('btn-primary');
                            $('#button75').addClass('btn-primary');
                             conf5=5;
                            $('#field7').val(5);">neither agreement nor disagreement</div><div
            id="button76"

            class="choicebuttons7 btn btn-default" onclick="$('.choicebuttons7').removeClass('btn-primary');
                            $('#button76').addClass('btn-primary');
                             conf5=6;
                            $('#field7').val(6);">slight agreement</div><div
            id="button77"

            class="choicebuttons7 btn btn-default" onclick="$('.choicebuttons7').removeClass('btn-primary');
                            $('#button77').addClass('btn-primary');
                             conf5=7;
                            $('#field7').val(7);">moderate agreement</div><div
            id="button78"

            class="choicebuttons7 btn btn-default" onclick="$('.choicebuttons7').removeClass('btn-primary');
                            $('#button78').addClass('btn-primary');
                             conf5=8;
                            $('#field7').val(8);">strong agreement</div><div
            id="button79"

            class="choicebuttons7 btn btn-default" onclick="$('.choicebuttons7').removeClass('btn-primary');
                            $('#button79').addClass('btn-primary');
                             conf5=9;
                            $('#field7').val(9);">very strong agreement</div><script>var conf5_options = [1,2,3,4,5,6,7,8,9];
        </script><div id="field7_noEntry" class="messagefield7 alert alert-danger" style="display: none;">Please indicate your response.</div><div id="field7_notcorrect" class="messagefield7 alert alert-danger" style="display: none;">The value you entered is not correct.</div></div></div><script>function checkValue_field7() {
           var label="conf5";var required=1;var inline=0;var orderoptions=0;var graphical=1;var correct=null;var defaultvalue=null;var multiple=null;var options=null;var clicksave=null;
            if(!(true)) { checker=checker+1; } else {
                var value;
                if (bot) { 
                    if (correct != null) { value = correct; }
                    else if (typeof bot_conf5 !== 'undefined') { value=bot_conf5; }
                    else { 
                    var allvalues=["1","2","3","4","5","6","7","8","9"];
                    var index=Math.floor(Math.random()*allvalues.length); 
                    value=allvalues[index]; }
                }
                else {
                value=($('#field7').val()); 
                }
                                
                $('.messagefield7').hide();
                allcorrect=checker+1;
                if ((value === null || value == "") && required==1) {
                    $('#field7_noEntry').show();
                }
                else if (value!=correct && correct != null && required!=0) {
                            $('#field7_notcorrect').show();
                        }
                
                else {
                        

                       record("conf5", value);

                            /* this variable is created in LionElementButton.class */
                           checker = checker+1;


                }
            
            if (allcorrect!=checker) {
                  wronganswers['conf5']=1;
                       totalwronganswers['conf5'] = isNaN(totalwronganswers['conf5']) ? 1 : totalwronganswers['conf5']+1; 
             
               } else wronganswers['conf5']=0;
            
            
            }
            
            
            
         }



        </script></div><script>if((true)) { $('#wrap7').show(); } </script><!-- END Element 7 Type: 23-->
        
        <!-- START Element 8 Type: 23-->
        
        <div class="col-sm-12" id="wrap8" style="display: none;"><div class="btnbox2"><div class="form-group "><input type="hidden" id="field8"><script>var conf6=null;</script><div style="text-align: center"><label for="field8"><br><b>6. A charismatic and eloquent speaker can easily influence and change my ideas.</b></label></div><div
            id="button81"

            class="choicebuttons8 btn btn-default" onclick="$('.choicebuttons8').removeClass('btn-primary');
                            $('#button81').addClass('btn-primary');
                             conf6=1;
                            $('#field8').val(1);">very strong disagreement</div><div
            id="button82"

            class="choicebuttons8 btn btn-default" onclick="$('.choicebuttons8').removeClass('btn-primary');
                            $('#button82').addClass('btn-primary');
                             conf6=2;
                            $('#field8').val(2);">strong disagreement</div><div
            id="button83"

            class="choicebuttons8 btn btn-default" onclick="$('.choicebuttons8').removeClass('btn-primary');
                            $('#button83').addClass('btn-primary');
                             conf6=3;
                            $('#field8').val(3);">moderate disagreement</div><div
            id="button84"

            class="choicebuttons8 btn btn-default" onclick="$('.choicebuttons8').removeClass('btn-primary');
                            $('#button84').addClass('btn-primary');
                             conf6=4;
                            $('#field8').val(4);">slight disagreement</div><div
            id="button85"

            class="choicebuttons8 btn btn-default" onclick="$('.choicebuttons8').removeClass('btn-primary');
                            $('#button85').addClass('btn-primary');
                             conf6=5;
                            $('#field8').val(5);">neither agreement nor disagreement</div><div
            id="button86"

            class="choicebuttons8 btn btn-default" onclick="$('.choicebuttons8').removeClass('btn-primary');
                            $('#button86').addClass('btn-primary');
                             conf6=6;
                            $('#field8').val(6);">slight agreement</div><div
            id="button87"

            class="choicebuttons8 btn btn-default" onclick="$('.choicebuttons8').removeClass('btn-primary');
                            $('#button87').addClass('btn-primary');
                             conf6=7;
                            $('#field8').val(7);">moderate agreement</div><div
            id="button88"

            class="choicebuttons8 btn btn-default" onclick="$('.choicebuttons8').removeClass('btn-primary');
                            $('#button88').addClass('btn-primary');
                             conf6=8;
                            $('#field8').val(8);">strong agreement</div><div
            id="button89"

            class="choicebuttons8 btn btn-default" onclick="$('.choicebuttons8').removeClass('btn-primary');
                            $('#button89').addClass('btn-primary');
                             conf6=9;
                            $('#field8').val(9);">very strong agreement</div><script>var conf6_options = [1,2,3,4,5,6,7,8,9];
        </script><div id="field8_noEntry" class="messagefield8 alert alert-danger" style="display: none;">Please indicate your response.</div><div id="field8_notcorrect" class="messagefield8 alert alert-danger" style="display: none;">The value you entered is not correct.</div></div></div><script>function checkValue_field8() {
           var label="conf6";var required=1;var inline=0;var orderoptions=0;var graphical=1;var correct=null;var defaultvalue=null;var multiple=null;var options=null;var clicksave=null;
            if(!(true)) { checker=checker+1; } else {
                var value;
                if (bot) { 
                    if (correct != null) { value = correct; }
                    else if (typeof bot_conf6 !== 'undefined') { value=bot_conf6; }
                    else { 
                    var allvalues=["1","2","3","4","5","6","7","8","9"];
                    var index=Math.floor(Math.random()*allvalues.length); 
                    value=allvalues[index]; }
                }
                else {
                value=($('#field8').val()); 
                }
                                
                $('.messagefield8').hide();
                allcorrect=checker+1;
                if ((value === null || value == "") && required==1) {
                    $('#field8_noEntry').show();
                }
                else if (value!=correct && correct != null && required!=0) {
                            $('#field8_notcorrect').show();
                        }
                
                else {
                        

                       record("conf6", value);

                            /* this variable is created in LionElementButton.class */
                           checker = checker+1;


                }
            
            if (allcorrect!=checker) {
                  wronganswers['conf6']=1;
                       totalwronganswers['conf6'] = isNaN(totalwronganswers['conf6']) ? 1 : totalwronganswers['conf6']+1; 
             
               } else wronganswers['conf6']=0;
            
            
            }
            
            
            
         }



        </script></div><script>if((true)) { $('#wrap8').show(); } </script><!-- END Element 8 Type: 23-->
        
        <!-- START Element 9 Type: 23-->
        
        <div class="col-sm-12" id="wrap9" style="display: none;"><div class="btnbox2"><div class="form-group "><input type="hidden" id="field9"><script>var conf7=null;</script><div style="text-align: center"><label for="field9"><br><b>7. I am more independent than conforming in my ways.</b></label></div><div
            id="button91"

            class="choicebuttons9 btn btn-default" onclick="$('.choicebuttons9').removeClass('btn-primary');
                            $('#button91').addClass('btn-primary');
                             conf7=1;
                            $('#field9').val(1);">very strong disagreement</div><div
            id="button92"

            class="choicebuttons9 btn btn-default" onclick="$('.choicebuttons9').removeClass('btn-primary');
                            $('#button92').addClass('btn-primary');
                             conf7=2;
                            $('#field9').val(2);">strong disagreement</div><div
            id="button93"

            class="choicebuttons9 btn btn-default" onclick="$('.choicebuttons9').removeClass('btn-primary');
                            $('#button93').addClass('btn-primary');
                             conf7=3;
                            $('#field9').val(3);">moderate disagreement</div><div
            id="button94"

            class="choicebuttons9 btn btn-default" onclick="$('.choicebuttons9').removeClass('btn-primary');
                            $('#button94').addClass('btn-primary');
                             conf7=4;
                            $('#field9').val(4);">slight disagreement</div><div
            id="button95"

            class="choicebuttons9 btn btn-default" onclick="$('.choicebuttons9').removeClass('btn-primary');
                            $('#button95').addClass('btn-primary');
                             conf7=5;
                            $('#field9').val(5);">neither agreement nor disagreement</div><div
            id="button96"

            class="choicebuttons9 btn btn-default" onclick="$('.choicebuttons9').removeClass('btn-primary');
                            $('#button96').addClass('btn-primary');
                             conf7=6;
                            $('#field9').val(6);">slight agreement</div><div
            id="button97"

            class="choicebuttons9 btn btn-default" onclick="$('.choicebuttons9').removeClass('btn-primary');
                            $('#button97').addClass('btn-primary');
                             conf7=7;
                            $('#field9').val(7);">moderate agreement</div><div
            id="button98"

            class="choicebuttons9 btn btn-default" onclick="$('.choicebuttons9').removeClass('btn-primary');
                            $('#button98').addClass('btn-primary');
                             conf7=8;
                            $('#field9').val(8);">strong agreement</div><div
            id="button99"

            class="choicebuttons9 btn btn-default" onclick="$('.choicebuttons9').removeClass('btn-primary');
                            $('#button99').addClass('btn-primary');
                             conf7=9;
                            $('#field9').val(9);">very strong agreement</div><script>var conf7_options = [1,2,3,4,5,6,7,8,9];
        </script><div id="field9_noEntry" class="messagefield9 alert alert-danger" style="display: none;">Please indicate your response.</div><div id="field9_notcorrect" class="messagefield9 alert alert-danger" style="display: none;">The value you entered is not correct.</div></div></div><script>function checkValue_field9() {
           var label="conf7";var required=1;var inline=0;var orderoptions=0;var graphical=1;var correct=null;var defaultvalue=null;var multiple=null;var options=null;var clicksave=null;
            if(!(true)) { checker=checker+1; } else {
                var value;
                if (bot) { 
                    if (correct != null) { value = correct; }
                    else if (typeof bot_conf7 !== 'undefined') { value=bot_conf7; }
                    else { 
                    var allvalues=["1","2","3","4","5","6","7","8","9"];
                    var index=Math.floor(Math.random()*allvalues.length); 
                    value=allvalues[index]; }
                }
                else {
                value=($('#field9').val()); 
                }
                                
                $('.messagefield9').hide();
                allcorrect=checker+1;
                if ((value === null || value == "") && required==1) {
                    $('#field9_noEntry').show();
                }
                else if (value!=correct && correct != null && required!=0) {
                            $('#field9_notcorrect').show();
                        }
                
                else {
                        

                       record("conf7", value);

                            /* this variable is created in LionElementButton.class */
                           checker = checker+1;


                }
            
            if (allcorrect!=checker) {
                  wronganswers['conf7']=1;
                       totalwronganswers['conf7'] = isNaN(totalwronganswers['conf7']) ? 1 : totalwronganswers['conf7']+1; 
             
               } else wronganswers['conf7']=0;
            
            
            }
            
            
            
         }



        </script></div><script>if((true)) { $('#wrap9').show(); } </script><!-- END Element 9 Type: 23-->
        
        <!-- START Element 10 Type: 23-->
        
        <div class="col-sm-12" id="wrap10" style="display: none;"><div class="btnbox2"><div class="form-group "><input type="hidden" id="field10"><script>var conf8=null;</script><div style="text-align: center"><label for="field10"><br><b>8. If someone is very persuasive, I tend to change my opinion and go along with them.</b></label></div><div
            id="button101"

            class="choicebuttons10 btn btn-default" onclick="$('.choicebuttons10').removeClass('btn-primary');
                            $('#button101').addClass('btn-primary');
                             conf8=1;
                            $('#field10').val(1);">very strong disagreement</div><div
            id="button102"

            class="choicebuttons10 btn btn-default" onclick="$('.choicebuttons10').removeClass('btn-primary');
                            $('#button102').addClass('btn-primary');
                             conf8=2;
                            $('#field10').val(2);">strong disagreement</div><div
            id="button103"

            class="choicebuttons10 btn btn-default" onclick="$('.choicebuttons10').removeClass('btn-primary');
                            $('#button103').addClass('btn-primary');
                             conf8=3;
                            $('#field10').val(3);">moderate disagreement</div><div
            id="button104"

            class="choicebuttons10 btn btn-default" onclick="$('.choicebuttons10').removeClass('btn-primary');
                            $('#button104').addClass('btn-primary');
                             conf8=4;
                            $('#field10').val(4);">slight disagreement</div><div
            id="button105"

            class="choicebuttons10 btn btn-default" onclick="$('.choicebuttons10').removeClass('btn-primary');
                            $('#button105').addClass('btn-primary');
                             conf8=5;
                            $('#field10').val(5);">neither agreement nor disagreement</div><div
            id="button106"

            class="choicebuttons10 btn btn-default" onclick="$('.choicebuttons10').removeClass('btn-primary');
                            $('#button106').addClass('btn-primary');
                             conf8=6;
                            $('#field10').val(6);">slight agreement</div><div
            id="button107"

            class="choicebuttons10 btn btn-default" onclick="$('.choicebuttons10').removeClass('btn-primary');
                            $('#button107').addClass('btn-primary');
                             conf8=7;
                            $('#field10').val(7);">moderate agreement</div><div
            id="button108"

            class="choicebuttons10 btn btn-default" onclick="$('.choicebuttons10').removeClass('btn-primary');
                            $('#button108').addClass('btn-primary');
                             conf8=8;
                            $('#field10').val(8);">strong agreement</div><div
            id="button109"

            class="choicebuttons10 btn btn-default" onclick="$('.choicebuttons10').removeClass('btn-primary');
                            $('#button109').addClass('btn-primary');
                             conf8=9;
                            $('#field10').val(9);">very strong agreement</div><script>var conf8_options = [1,2,3,4,5,6,7,8,9];
        </script><div id="field10_noEntry" class="messagefield10 alert alert-danger" style="display: none;">Please indicate your response.</div><div id="field10_notcorrect" class="messagefield10 alert alert-danger" style="display: none;">The value you entered is not correct.</div></div></div><script>function checkValue_field10() {
           var label="conf8";var required=1;var inline=0;var orderoptions=0;var graphical=1;var correct=null;var defaultvalue=null;var multiple=null;var options=null;var clicksave=null;
            if(!(true)) { checker=checker+1; } else {
                var value;
                if (bot) { 
                    if (correct != null) { value = correct; }
                    else if (typeof bot_conf8 !== 'undefined') { value=bot_conf8; }
                    else { 
                    var allvalues=["1","2","3","4","5","6","7","8","9"];
                    var index=Math.floor(Math.random()*allvalues.length); 
                    value=allvalues[index]; }
                }
                else {
                value=($('#field10').val()); 
                }
                                
                $('.messagefield10').hide();
                allcorrect=checker+1;
                if ((value === null || value == "") && required==1) {
                    $('#field10_noEntry').show();
                }
                else if (value!=correct && correct != null && required!=0) {
                            $('#field10_notcorrect').show();
                        }
                
                else {
                        

                       record("conf8", value);

                            /* this variable is created in LionElementButton.class */
                           checker = checker+1;


                }
            
            if (allcorrect!=checker) {
                  wronganswers['conf8']=1;
                       totalwronganswers['conf8'] = isNaN(totalwronganswers['conf8']) ? 1 : totalwronganswers['conf8']+1; 
             
               } else wronganswers['conf8']=0;
            
            
            }
            
            
            
         }



        </script></div><script>if((true)) { $('#wrap10').show(); } </script><!-- END Element 10 Type: 23-->
        
        <!-- START Element 11 Type: 23-->
        
        <div class="col-sm-12" id="wrap11" style="display: none;"><div class="btnbox2"><div class="form-group "><input type="hidden" id="field11"><script>var conf9=null;</script><div style="text-align: center"><label for="field11"><br><b>9. I don&#039;t give in to others easily.</b></label></div><div
            id="button111"

            class="choicebuttons11 btn btn-default" onclick="$('.choicebuttons11').removeClass('btn-primary');
                            $('#button111').addClass('btn-primary');
                             conf9=1;
                            $('#field11').val(1);">very strong disagreement</div><div
            id="button112"

            class="choicebuttons11 btn btn-default" onclick="$('.choicebuttons11').removeClass('btn-primary');
                            $('#button112').addClass('btn-primary');
                             conf9=2;
                            $('#field11').val(2);">strong disagreement</div><div
            id="button113"

            class="choicebuttons11 btn btn-default" onclick="$('.choicebuttons11').removeClass('btn-primary');
                            $('#button113').addClass('btn-primary');
                             conf9=3;
                            $('#field11').val(3);">moderate disagreement</div><div
            id="button114"

            class="choicebuttons11 btn btn-default" onclick="$('.choicebuttons11').removeClass('btn-primary');
                            $('#button114').addClass('btn-primary');
                             conf9=4;
                            $('#field11').val(4);">slight disagreement</div><div
            id="button115"

            class="choicebuttons11 btn btn-default" onclick="$('.choicebuttons11').removeClass('btn-primary');
                            $('#button115').addClass('btn-primary');
                             conf9=5;
                            $('#field11').val(5);">neither agreement nor disagreement</div><div
            id="button116"

            class="choicebuttons11 btn btn-default" onclick="$('.choicebuttons11').removeClass('btn-primary');
                            $('#button116').addClass('btn-primary');
                             conf9=6;
                            $('#field11').val(6);">slight agreement</div><div
            id="button117"

            class="choicebuttons11 btn btn-default" onclick="$('.choicebuttons11').removeClass('btn-primary');
                            $('#button117').addClass('btn-primary');
                             conf9=7;
                            $('#field11').val(7);">moderate agreement</div><div
            id="button118"

            class="choicebuttons11 btn btn-default" onclick="$('.choicebuttons11').removeClass('btn-primary');
                            $('#button118').addClass('btn-primary');
                             conf9=8;
                            $('#field11').val(8);">strong agreement</div><div
            id="button119"

            class="choicebuttons11 btn btn-default" onclick="$('.choicebuttons11').removeClass('btn-primary');
                            $('#button119').addClass('btn-primary');
                             conf9=9;
                            $('#field11').val(9);">very strong agreement</div><script>var conf9_options = [1,2,3,4,5,6,7,8,9];
        </script><div id="field11_noEntry" class="messagefield11 alert alert-danger" style="display: none;">Please indicate your response.</div><div id="field11_notcorrect" class="messagefield11 alert alert-danger" style="display: none;">The value you entered is not correct.</div></div></div><script>function checkValue_field11() {
           var label="conf9";var required=1;var inline=0;var orderoptions=0;var graphical=1;var correct=null;var defaultvalue=null;var multiple=null;var options=null;var clicksave=null;
            if(!(true)) { checker=checker+1; } else {
                var value;
                if (bot) { 
                    if (correct != null) { value = correct; }
                    else if (typeof bot_conf9 !== 'undefined') { value=bot_conf9; }
                    else { 
                    var allvalues=["1","2","3","4","5","6","7","8","9"];
                    var index=Math.floor(Math.random()*allvalues.length); 
                    value=allvalues[index]; }
                }
                else {
                value=($('#field11').val()); 
                }
                                
                $('.messagefield11').hide();
                allcorrect=checker+1;
                if ((value === null || value == "") && required==1) {
                    $('#field11_noEntry').show();
                }
                else if (value!=correct && correct != null && required!=0) {
                            $('#field11_notcorrect').show();
                        }
                
                else {
                        

                       record("conf9", value);

                            /* this variable is created in LionElementButton.class */
                           checker = checker+1;


                }
            
            if (allcorrect!=checker) {
                  wronganswers['conf9']=1;
                       totalwronganswers['conf9'] = isNaN(totalwronganswers['conf9']) ? 1 : totalwronganswers['conf9']+1; 
             
               } else wronganswers['conf9']=0;
            
            
            }
            
            
            
         }



        </script></div><script>if((true)) { $('#wrap11').show(); } </script><!-- END Element 11 Type: 23-->
        
        <!-- START Element 12 Type: 23-->
        
        <div class="col-sm-12" id="wrap12" style="display: none;"><div class="btnbox2"><div class="form-group "><input type="hidden" id="field12"><script>var conf10=null;</script><div style="text-align: center"><label for="field12"><br><b>10. I tend to rely on others when I have to make an important decision quickly.</b></label></div><div
            id="button121"

            class="choicebuttons12 btn btn-default" onclick="$('.choicebuttons12').removeClass('btn-primary');
                            $('#button121').addClass('btn-primary');
                             conf10=1;
                            $('#field12').val(1);">very strong disagreement</div><div
            id="button122"

            class="choicebuttons12 btn btn-default" onclick="$('.choicebuttons12').removeClass('btn-primary');
                            $('#button122').addClass('btn-primary');
                             conf10=2;
                            $('#field12').val(2);">strong disagreement</div><div
            id="button123"

            class="choicebuttons12 btn btn-default" onclick="$('.choicebuttons12').removeClass('btn-primary');
                            $('#button123').addClass('btn-primary');
                             conf10=3;
                            $('#field12').val(3);">moderate disagreement</div><div
            id="button124"

            class="choicebuttons12 btn btn-default" onclick="$('.choicebuttons12').removeClass('btn-primary');
                            $('#button124').addClass('btn-primary');
                             conf10=4;
                            $('#field12').val(4);">slight disagreement</div><div
            id="button125"

            class="choicebuttons12 btn btn-default" onclick="$('.choicebuttons12').removeClass('btn-primary');
                            $('#button125').addClass('btn-primary');
                             conf10=5;
                            $('#field12').val(5);">neither agreement nor disagreement</div><div
            id="button126"

            class="choicebuttons12 btn btn-default" onclick="$('.choicebuttons12').removeClass('btn-primary');
                            $('#button126').addClass('btn-primary');
                             conf10=6;
                            $('#field12').val(6);">slight agreement</div><div
            id="button127"

            class="choicebuttons12 btn btn-default" onclick="$('.choicebuttons12').removeClass('btn-primary');
                            $('#button127').addClass('btn-primary');
                             conf10=7;
                            $('#field12').val(7);">moderate agreement</div><div
            id="button128"

            class="choicebuttons12 btn btn-default" onclick="$('.choicebuttons12').removeClass('btn-primary');
                            $('#button128').addClass('btn-primary');
                             conf10=8;
                            $('#field12').val(8);">strong agreement</div><div
            id="button129"

            class="choicebuttons12 btn btn-default" onclick="$('.choicebuttons12').removeClass('btn-primary');
                            $('#button129').addClass('btn-primary');
                             conf10=9;
                            $('#field12').val(9);">very strong agreement</div><script>var conf10_options = [1,2,3,4,5,6,7,8,9];
        </script><div id="field12_noEntry" class="messagefield12 alert alert-danger" style="display: none;">Please indicate your response.</div><div id="field12_notcorrect" class="messagefield12 alert alert-danger" style="display: none;">The value you entered is not correct.</div></div></div><script>function checkValue_field12() {
           var label="conf10";var required=1;var inline=0;var orderoptions=0;var graphical=1;var correct=null;var defaultvalue=null;var multiple=null;var options=null;var clicksave=null;
            if(!(true)) { checker=checker+1; } else {
                var value;
                if (bot) { 
                    if (correct != null) { value = correct; }
                    else if (typeof bot_conf10 !== 'undefined') { value=bot_conf10; }
                    else { 
                    var allvalues=["1","2","3","4","5","6","7","8","9"];
                    var index=Math.floor(Math.random()*allvalues.length); 
                    value=allvalues[index]; }
                }
                else {
                value=($('#field12').val()); 
                }
                                
                $('.messagefield12').hide();
                allcorrect=checker+1;
                if ((value === null || value == "") && required==1) {
                    $('#field12_noEntry').show();
                }
                else if (value!=correct && correct != null && required!=0) {
                            $('#field12_notcorrect').show();
                        }
                
                else {
                        

                       record("conf10", value);

                            /* this variable is created in LionElementButton.class */
                           checker = checker+1;


                }
            
            if (allcorrect!=checker) {
                  wronganswers['conf10']=1;
                       totalwronganswers['conf10'] = isNaN(totalwronganswers['conf10']) ? 1 : totalwronganswers['conf10']+1; 
             
               } else wronganswers['conf10']=0;
            
            
            }
            
            
            
         }



        </script></div><script>if((true)) { $('#wrap12').show(); } </script><!-- END Element 12 Type: 23-->
        
        <!-- START Element 13 Type: 23-->
        
        <div class="col-sm-12" id="wrap13" style="display: none;"><div class="btnbox2"><div class="form-group "><input type="hidden" id="field13"><script>var conf11=null;</script><div style="text-align: center"><label for="field13"><br><b>11. I prefer to make my own way in life rather than find a group I can follow.</b></label></div><div
            id="button131"

            class="choicebuttons13 btn btn-default" onclick="$('.choicebuttons13').removeClass('btn-primary');
                            $('#button131').addClass('btn-primary');
                             conf11=1;
                            $('#field13').val(1);">very strong disagreement</div><div
            id="button132"

            class="choicebuttons13 btn btn-default" onclick="$('.choicebuttons13').removeClass('btn-primary');
                            $('#button132').addClass('btn-primary');
                             conf11=2;
                            $('#field13').val(2);">strong disagreement</div><div
            id="button133"

            class="choicebuttons13 btn btn-default" onclick="$('.choicebuttons13').removeClass('btn-primary');
                            $('#button133').addClass('btn-primary');
                             conf11=3;
                            $('#field13').val(3);">moderate disagreement</div><div
            id="button134"

            class="choicebuttons13 btn btn-default" onclick="$('.choicebuttons13').removeClass('btn-primary');
                            $('#button134').addClass('btn-primary');
                             conf11=4;
                            $('#field13').val(4);">slight disagreement</div><div
            id="button135"

            class="choicebuttons13 btn btn-default" onclick="$('.choicebuttons13').removeClass('btn-primary');
                            $('#button135').addClass('btn-primary');
                             conf11=5;
                            $('#field13').val(5);">neither agreement nor disagreement</div><div
            id="button136"

            class="choicebuttons13 btn btn-default" onclick="$('.choicebuttons13').removeClass('btn-primary');
                            $('#button136').addClass('btn-primary');
                             conf11=6;
                            $('#field13').val(6);">slight agreement</div><div
            id="button137"

            class="choicebuttons13 btn btn-default" onclick="$('.choicebuttons13').removeClass('btn-primary');
                            $('#button137').addClass('btn-primary');
                             conf11=7;
                            $('#field13').val(7);">moderate agreement</div><div
            id="button138"

            class="choicebuttons13 btn btn-default" onclick="$('.choicebuttons13').removeClass('btn-primary');
                            $('#button138').addClass('btn-primary');
                             conf11=8;
                            $('#field13').val(8);">strong agreement</div><div
            id="button139"

            class="choicebuttons13 btn btn-default" onclick="$('.choicebuttons13').removeClass('btn-primary');
                            $('#button139').addClass('btn-primary');
                             conf11=9;
                            $('#field13').val(9);">very strong agreement</div><script>var conf11_options = [1,2,3,4,5,6,7,8,9];
        </script><div id="field13_noEntry" class="messagefield13 alert alert-danger" style="display: none;">Please indicate your response.</div><div id="field13_notcorrect" class="messagefield13 alert alert-danger" style="display: none;">The value you entered is not correct.</div></div></div><script>function checkValue_field13() {
           var label="conf11";var required=1;var inline=0;var orderoptions=0;var graphical=1;var correct=null;var defaultvalue=null;var multiple=null;var options=null;var clicksave=null;
            if(!(true)) { checker=checker+1; } else {
                var value;
                if (bot) { 
                    if (correct != null) { value = correct; }
                    else if (typeof bot_conf11 !== 'undefined') { value=bot_conf11; }
                    else { 
                    var allvalues=["1","2","3","4","5","6","7","8","9"];
                    var index=Math.floor(Math.random()*allvalues.length); 
                    value=allvalues[index]; }
                }
                else {
                value=($('#field13').val()); 
                }
                                
                $('.messagefield13').hide();
                allcorrect=checker+1;
                if ((value === null || value == "") && required==1) {
                    $('#field13_noEntry').show();
                }
                else if (value!=correct && correct != null && required!=0) {
                            $('#field13_notcorrect').show();
                        }
                
                else {
                        

                       record("conf11", value);

                            /* this variable is created in LionElementButton.class */
                           checker = checker+1;


                }
            
            if (allcorrect!=checker) {
                  wronganswers['conf11']=1;
                       totalwronganswers['conf11'] = isNaN(totalwronganswers['conf11']) ? 1 : totalwronganswers['conf11']+1; 
             
               } else wronganswers['conf11']=0;
            
            
            }
            
            
            
         }



        </script></div><script>if((true)) { $('#wrap13').show(); } </script><!-- END Element 13 Type: 23-->
        
        <!-- START Element 14 Type: 18-->
        
        <div class="col-sm-12" id="wrap14" style="display: none;">
        <script>
       
        
        </script>
        
        <div  id="button14">
        <div id="buttonclick14" class="lionessbutton btn btn-default btn-lg btn-block " style=" white-space:normal !important; word-wrap: break-word;" onclick="
        $(this).hide(); $('#buttonload14').show();
        if (additionalCheck14()) {
            hideError14();
            if (checkEntries()) toNextPage14();
            else  { $(this).show(); 
            $('#buttonload14').hide(); }
        } else {
         $(this).show(); 
         $('#buttonload14').hide();
         }
        ">Continue</div><div id="buttonload14" style="width: 100%; text-align: center; display: none;"><img src="<?php echo PATH;?>basis/pic/buttonload.gif"></div><div id="field14_error" class="alert alert-danger" style="display: none; text-align: center;"></div><div id="field14_attempts" class="alert alert-warning" style="display: none; text-align: center;"><span class="attempts_text">Attempts left to answer the control questions</span>:&nbsp;<span id="field14_attempts_num"></span></div></div><script>if(maxFalse!=null) {
            var numFails=quizFail(playerNr,1);  
            $('#field14_attempts').show();
            $('#field14_attempts_num').html(maxFalse-numFails);
           
        }
        function showError14(text) {
            var errorfield= $('#field14_error');
            errorfield.show();
            errorfield.html(text);
        
        }
        
        function hideError14() {
            $('#field14_error').hide();
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
        
        function additionalCheck14() {

           return true;
        }

       



        function checkFail() {} function toNextPage14() {
            if (loopEnd==326687) { showNext('wait326687.php?session_index=<?php echo $_SESSION[sessionID];?>',160464,326687);}
            else {showNext('stage160464.php?session_index=<?php echo $_SESSION[sessionID];?>',160464,326687);}

            };</script></div><script>if((true)) { $('#wrap14').show(); $('#buttonclick14').addClass('buttonclick');} </script><!-- END Element 14 Type: 18-->
        
        </div><script>setInterval(function(){ if (true) $('#wrap2').show();if (!(true)) $('#wrap2').hide();if (true) $('#wrap3').show();if (!(true)) $('#wrap3').hide();if (true) $('#wrap4').show();if (!(true)) $('#wrap4').hide();if (true) $('#wrap5').show();if (!(true)) $('#wrap5').hide();if (true) $('#wrap6').show();if (!(true)) $('#wrap6').hide();if (true) $('#wrap7').show();if (!(true)) $('#wrap7').hide();if (true) $('#wrap8').show();if (!(true)) $('#wrap8').hide();if (true) $('#wrap9').show();if (!(true)) $('#wrap9').hide();if (true) $('#wrap10').show();if (!(true)) $('#wrap10').hide();if (true) $('#wrap11').show();if (!(true)) $('#wrap11').hide();if (true) $('#wrap12').show();if (!(true)) $('#wrap12').hide();if (true) $('#wrap13').show();if (!(true)) $('#wrap13').hide();if (true) $('#wrap14').show();if (!(true)) $('#wrap14').hide(); }, 100);</script></form></div></div></body></html>