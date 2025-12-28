<html>
        <head>
        
        <?php
    
        include("_projectID.php");
        include(PATH."basis/participant/header.php");
	    $_SESSION['projectID']=PROJECTID;
	    
	    ?>

        <link href="<?php echo PATH;?>basis/css/newlayout.css?v1" rel="stylesheet" type="text/css"  />
        <link href="<?php echo PATH;?>basis/css/newlayout_bootstrap.css" rel="stylesheet" type="text/css"  />
        <link href="<?php echo PATH;?>basis/css/grid.css" rel="stylesheet" type="text/css"  /><title>Questionnaire 3</title>

        <script> var v={}; var wronganswers={}; var totalwronganswers={};var maxFalse = null;
        var firstStageExp = <?php echo json_encode(FIRSTPAGE . ".php"); ?>;
        var thisPage = <?php echo json_encode($thisPage); ?>;
        var sessionIndexJavascript = "<?php echo $_SESSION[sessionID];?>";
        pageRefreshed=0;
        var loopBegin = "stage" + loopStart + ".php";
        var afterLoopEnd = 326683;
        if (thisPage == firstStageExp || (thisPage==loopBegin && period > 1) || loopEnd==afterLoopEnd) firstStage();
        /* if (thisPage == firstStageExp || thisPage==loopBegin || loopEnd==afterLoopEnd) firstStage(); */
        TimeOut=null;
        function skipStage(proceedifpossible) {
         if (proceedifpossible === undefined) proceedifpossible = false;
         if (proceedifpossible) location.replace('stage326685.php?session_index=<?php echo $_SESSION[sessionID];?>');
         else location.replace('wait326684.php?session_index=<?php echo $_SESSION[sessionID];?>');
        }
        $(document).ready(function(){
        if (bot) { document.getElementsByClassName("buttonclick")[0].click(); }
        });
        
        </script>
        </head><body><div id="mainwrap" class="container" style="width: 100%; padding-left: 5%; padding-right: 5%; padding-top: 1%;"><form autocomplete="off"><div class="row"><!-- START Element 1 Type: 19-->
        
        
        <script>record('iterationQ',0);

record('socialLadder',0);
record('dominanceLadder',0);
record('popularityLadder',0);
record('intelligenceLadder',0);
record('economicsLadder',0);</script><!-- END Element 1 Type: 19-->
        
        <!-- START Element 2 Type: 1-->
        
        <div class="col-sm-12" id="wrap2" style="display: none;"><div class="btnbox2 paddlr" style="text-align: center"><h3>Questionnaire part 3 of 4</h3><p>Please respond to each of the following statements by expressing how much you agree with it (if you do generally
&nbsp;<span style="background-color: rgba(223, 240, 216, 0);">agree)&nbsp;<br></span><span style="background-color: rgba(223, 240, 216, 0);">or how much you disagree with it (if you generally disagree).&nbsp;</span></p><p><span style="background-color: rgba(223, 240, 216, 0);">Please be as accurate as you can be throughout,&nbsp;<br></span><span style="background-color: rgba(223, 240, 216, 0);">and try especially&nbsp;</span><span style="background-color: rgba(223, 240, 216, 0);">hard not to let your answer to any one item influence your answer to any other item.&nbsp;<br></span><span style="background-color: rgba(223, 240, 216, 0);">Treat each one as though it&nbsp;</span><span style="background-color: rgba(223, 240, 216, 0);">is completely unrelated to the others.&nbsp;</span></p><p><span style="background-color: rgba(223, 240, 216, 0);">There are no right or wrong answers, you are simply to express your own&nbsp;</span><span style="background-color: rgba(223, 240, 216, 0);">personal feelings and opinions.</span></p><p></p></div>
        </div><script>if((true)) { $('#wrap2').show(); } </script><!-- END Element 2 Type: 1-->
        
        <!-- START Element 3 Type: 23-->
        
        <div class="col-sm-12" id="wrap3" style="display: none;"><div class="btnbox2"><div class="form-group "><input type="hidden" id="field3"><script>var maq8=null;</script><div style="text-align: center"><label for="field3"><br><b>8. I am very comfortable being close to others.</b></label></div><div
            id="button31"

            class="choicebuttons3 btn btn-default" onclick="$('.choicebuttons3').removeClass('btn-primary');
                            $('#button31').addClass('btn-primary');
                             maq8=1;
                            $('#field3').val(1);">Disagree a lot</div><div
            id="button32"

            class="choicebuttons3 btn btn-default" onclick="$('.choicebuttons3').removeClass('btn-primary');
                            $('#button32').addClass('btn-primary');
                             maq8=2;
                            $('#field3').val(2);">Disagree a little</div><div
            id="button33"

            class="choicebuttons3 btn btn-default" onclick="$('.choicebuttons3').removeClass('btn-primary');
                            $('#button33').addClass('btn-primary');
                             maq8=3;
                            $('#field3').val(3);">Agree a little</div><div
            id="button34"

            class="choicebuttons3 btn btn-default" onclick="$('.choicebuttons3').removeClass('btn-primary');
                            $('#button34').addClass('btn-primary');
                             maq8=4;
                            $('#field3').val(4);">Agree a lot</div><script>var maq8_options = [1,2,3,4];
        </script><div id="field3_noEntry" class="messagefield3 alert alert-danger" style="display: none;">Please indicate your response.</div><div id="field3_notcorrect" class="messagefield3 alert alert-danger" style="display: none;">The value you entered is not correct.</div></div></div><script>function checkValue_field3() {
           var label="maq8";var required=0;var inline=0;var orderoptions=0;var graphical=1;var correct=null;var defaultvalue=null;var multiple=0;var options=null;var clicksave=0;
            if(!(true)) { checker=checker+1; } else {
                var value;
                if (bot) { 
                    if (correct != null) { value = correct; }
                    else if (typeof bot_maq8 !== 'undefined') { value=bot_maq8; }
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
                        

                       record("maq8", value);

                            /* this variable is created in LionElementButton.class */
                           checker = checker+1;


                }
            
            if (allcorrect!=checker) {
                  wronganswers['maq8']=1;
                       totalwronganswers['maq8'] = isNaN(totalwronganswers['maq8']) ? 1 : totalwronganswers['maq8']+1; 
             
               } else wronganswers['maq8']=0;
            
            
            }
            
            
            
         }



        </script></div><script>if((true)) { $('#wrap3').show(); } </script><!-- END Element 3 Type: 23-->
        
        <!-- START Element 4 Type: 23-->
        
        <div class="col-sm-12" id="wrap4" style="display: none;"><div class="btnbox2"><div class="form-group "><input type="hidden" id="field4"><script>var maq9=null;</script><div style="text-align: center"><label for="field4"><br><b>9. I don’t worry about others abandoning me.</b></label></div><div
            id="button41"

            class="choicebuttons4 btn btn-default" onclick="$('.choicebuttons4').removeClass('btn-primary');
                            $('#button41').addClass('btn-primary');
                             maq9=1;
                            $('#field4').val(1);">Disagree a lot</div><div
            id="button42"

            class="choicebuttons4 btn btn-default" onclick="$('.choicebuttons4').removeClass('btn-primary');
                            $('#button42').addClass('btn-primary');
                             maq9=2;
                            $('#field4').val(2);">Disagree a little</div><div
            id="button43"

            class="choicebuttons4 btn btn-default" onclick="$('.choicebuttons4').removeClass('btn-primary');
                            $('#button43').addClass('btn-primary');
                             maq9=3;
                            $('#field4').val(3);">Agree a little</div><div
            id="button44"

            class="choicebuttons4 btn btn-default" onclick="$('.choicebuttons4').removeClass('btn-primary');
                            $('#button44').addClass('btn-primary');
                             maq9=4;
                            $('#field4').val(4);">Agree a lot</div><script>var maq9_options = [1,2,3,4];
        </script><div id="field4_noEntry" class="messagefield4 alert alert-danger" style="display: none;">Please indicate your response.</div><div id="field4_notcorrect" class="messagefield4 alert alert-danger" style="display: none;">The value you entered is not correct.</div></div></div><script>function checkValue_field4() {
           var label="maq9";var required=0;var inline=0;var orderoptions=0;var graphical=1;var correct=null;var defaultvalue=null;var multiple=0;var options=null;var clicksave=0;
            if(!(true)) { checker=checker+1; } else {
                var value;
                if (bot) { 
                    if (correct != null) { value = correct; }
                    else if (typeof bot_maq9 !== 'undefined') { value=bot_maq9; }
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
                        

                       record("maq9", value);

                            /* this variable is created in LionElementButton.class */
                           checker = checker+1;


                }
            
            if (allcorrect!=checker) {
                  wronganswers['maq9']=1;
                       totalwronganswers['maq9'] = isNaN(totalwronganswers['maq9']) ? 1 : totalwronganswers['maq9']+1; 
             
               } else wronganswers['maq9']=0;
            
            
            }
            
            
            
         }



        </script></div><script>if((true)) { $('#wrap4').show(); } </script><!-- END Element 4 Type: 23-->
        
        <!-- START Element 5 Type: 23-->
        
        <div class="col-sm-12" id="wrap5" style="display: none;"><div class="btnbox2"><div class="form-group "><input type="hidden" id="field5"><script>var maq10=null;</script><div style="text-align: center"><label for="field5"><br><b>10. My desire to merge sometimes scares people away.</b></label></div><div
            id="button51"

            class="choicebuttons5 btn btn-default" onclick="$('.choicebuttons5').removeClass('btn-primary');
                            $('#button51').addClass('btn-primary');
                             maq10=1;
                            $('#field5').val(1);">Disagree a lot</div><div
            id="button52"

            class="choicebuttons5 btn btn-default" onclick="$('.choicebuttons5').removeClass('btn-primary');
                            $('#button52').addClass('btn-primary');
                             maq10=2;
                            $('#field5').val(2);">Disagree a little</div><div
            id="button53"

            class="choicebuttons5 btn btn-default" onclick="$('.choicebuttons5').removeClass('btn-primary');
                            $('#button53').addClass('btn-primary');
                             maq10=3;
                            $('#field5').val(3);">Agree a little</div><div
            id="button54"

            class="choicebuttons5 btn btn-default" onclick="$('.choicebuttons5').removeClass('btn-primary');
                            $('#button54').addClass('btn-primary');
                             maq10=4;
                            $('#field5').val(4);">Agree a lot</div><script>var maq10_options = [1,2,3,4];
        </script><div id="field5_noEntry" class="messagefield5 alert alert-danger" style="display: none;">Please indicate your response.</div><div id="field5_notcorrect" class="messagefield5 alert alert-danger" style="display: none;">The value you entered is not correct.</div></div></div><script>function checkValue_field5() {
           var label="maq10";var required=0;var inline=0;var orderoptions=0;var graphical=1;var correct=null;var defaultvalue=null;var multiple=0;var options=null;var clicksave=0;
            if(!(true)) { checker=checker+1; } else {
                var value;
                if (bot) { 
                    if (correct != null) { value = correct; }
                    else if (typeof bot_maq10 !== 'undefined') { value=bot_maq10; }
                    else { 
                    var allvalues=["1","2","3","4"];
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
                        

                       record("maq10", value);

                            /* this variable is created in LionElementButton.class */
                           checker = checker+1;


                }
            
            if (allcorrect!=checker) {
                  wronganswers['maq10']=1;
                       totalwronganswers['maq10'] = isNaN(totalwronganswers['maq10']) ? 1 : totalwronganswers['maq10']+1; 
             
               } else wronganswers['maq10']=0;
            
            
            }
            
            
            
         }



        </script></div><script>if((true)) { $('#wrap5').show(); } </script><!-- END Element 5 Type: 23-->
        
        <!-- START Element 6 Type: 23-->
        
        <div class="col-sm-12" id="wrap6" style="display: none;"><div class="btnbox2"><div class="form-group "><input type="hidden" id="field6"><script>var maq11=null;</script><div style="text-align: center"><label for="field6"><br><b>11. I prefer not to be too close to others</b></label></div><div
            id="button61"

            class="choicebuttons6 btn btn-default" onclick="$('.choicebuttons6').removeClass('btn-primary');
                            $('#button61').addClass('btn-primary');
                             maq11=1;
                            $('#field6').val(1);">Disagree a lot</div><div
            id="button62"

            class="choicebuttons6 btn btn-default" onclick="$('.choicebuttons6').removeClass('btn-primary');
                            $('#button62').addClass('btn-primary');
                             maq11=2;
                            $('#field6').val(2);">Disagree a little</div><div
            id="button63"

            class="choicebuttons6 btn btn-default" onclick="$('.choicebuttons6').removeClass('btn-primary');
                            $('#button63').addClass('btn-primary');
                             maq11=3;
                            $('#field6').val(3);">Agree a little</div><div
            id="button64"

            class="choicebuttons6 btn btn-default" onclick="$('.choicebuttons6').removeClass('btn-primary');
                            $('#button64').addClass('btn-primary');
                             maq11=4;
                            $('#field6').val(4);">Agree a lot</div><script>var maq11_options = [1,2,3,4];
        </script><div id="field6_noEntry" class="messagefield6 alert alert-danger" style="display: none;">Please indicate your response.</div><div id="field6_notcorrect" class="messagefield6 alert alert-danger" style="display: none;">The value you entered is not correct.</div></div></div><script>function checkValue_field6() {
           var label="maq11";var required=0;var inline=0;var orderoptions=0;var graphical=1;var correct=null;var defaultvalue=null;var multiple=0;var options=null;var clicksave=0;
            if(!(true)) { checker=checker+1; } else {
                var value;
                if (bot) { 
                    if (correct != null) { value = correct; }
                    else if (typeof bot_maq11 !== 'undefined') { value=bot_maq11; }
                    else { 
                    var allvalues=["1","2","3","4"];
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
                        

                       record("maq11", value);

                            /* this variable is created in LionElementButton.class */
                           checker = checker+1;


                }
            
            if (allcorrect!=checker) {
                  wronganswers['maq11']=1;
                       totalwronganswers['maq11'] = isNaN(totalwronganswers['maq11']) ? 1 : totalwronganswers['maq11']+1; 
             
               } else wronganswers['maq11']=0;
            
            
            }
            
            
            
         }



        </script></div><script>if((true)) { $('#wrap6').show(); } </script><!-- END Element 6 Type: 23-->
        
        <!-- START Element 7 Type: 23-->
        
        <div class="col-sm-12" id="wrap7" style="display: none;"><div class="btnbox2"><div class="form-group "><input type="hidden" id="field7"><script>var maq12=null;</script><div style="text-align: center"><label for="field7"><br><b>12. I find others are reluctant to get as close as I would like.</b></label></div><div
            id="button71"

            class="choicebuttons7 btn btn-default" onclick="$('.choicebuttons7').removeClass('btn-primary');
                            $('#button71').addClass('btn-primary');
                             maq12=1;
                            $('#field7').val(1);">Disagree a lot</div><div
            id="button72"

            class="choicebuttons7 btn btn-default" onclick="$('.choicebuttons7').removeClass('btn-primary');
                            $('#button72').addClass('btn-primary');
                             maq12=2;
                            $('#field7').val(2);">Disagree a little</div><div
            id="button73"

            class="choicebuttons7 btn btn-default" onclick="$('.choicebuttons7').removeClass('btn-primary');
                            $('#button73').addClass('btn-primary');
                             maq12=3;
                            $('#field7').val(3);">Agree a little</div><div
            id="button74"

            class="choicebuttons7 btn btn-default" onclick="$('.choicebuttons7').removeClass('btn-primary');
                            $('#button74').addClass('btn-primary');
                             maq12=4;
                            $('#field7').val(4);">Agree a lot</div><script>var maq12_options = [1,2,3,4];
        </script><div id="field7_noEntry" class="messagefield7 alert alert-danger" style="display: none;">Please indicate your response.</div><div id="field7_notcorrect" class="messagefield7 alert alert-danger" style="display: none;">The value you entered is not correct.</div></div></div><script>function checkValue_field7() {
           var label="maq12";var required=0;var inline=0;var orderoptions=0;var graphical=1;var correct=null;var defaultvalue=null;var multiple=0;var options=null;var clicksave=0;
            if(!(true)) { checker=checker+1; } else {
                var value;
                if (bot) { 
                    if (correct != null) { value = correct; }
                    else if (typeof bot_maq12 !== 'undefined') { value=bot_maq12; }
                    else { 
                    var allvalues=["1","2","3","4"];
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
                        

                       record("maq12", value);

                            /* this variable is created in LionElementButton.class */
                           checker = checker+1;


                }
            
            if (allcorrect!=checker) {
                  wronganswers['maq12']=1;
                       totalwronganswers['maq12'] = isNaN(totalwronganswers['maq12']) ? 1 : totalwronganswers['maq12']+1; 
             
               } else wronganswers['maq12']=0;
            
            
            }
            
            
            
         }



        </script></div><script>if((true)) { $('#wrap7').show(); } </script><!-- END Element 7 Type: 23-->
        
        <!-- START Element 8 Type: 23-->
        
        <div class="col-sm-12" id="wrap8" style="display: none;"><div class="btnbox2"><div class="form-group "><input type="hidden" id="field8"><script>var maq13=null;</script><div style="text-align: center"><label for="field8"><br><b>13. I get uncomfortable when someone wants to be very close.</b></label></div><div
            id="button81"

            class="choicebuttons8 btn btn-default" onclick="$('.choicebuttons8').removeClass('btn-primary');
                            $('#button81').addClass('btn-primary');
                             maq13=1;
                            $('#field8').val(1);">Disagree a lot</div><div
            id="button82"

            class="choicebuttons8 btn btn-default" onclick="$('.choicebuttons8').removeClass('btn-primary');
                            $('#button82').addClass('btn-primary');
                             maq13=2;
                            $('#field8').val(2);">Disagree a little</div><div
            id="button83"

            class="choicebuttons8 btn btn-default" onclick="$('.choicebuttons8').removeClass('btn-primary');
                            $('#button83').addClass('btn-primary');
                             maq13=3;
                            $('#field8').val(3);">Agree a little</div><div
            id="button84"

            class="choicebuttons8 btn btn-default" onclick="$('.choicebuttons8').removeClass('btn-primary');
                            $('#button84').addClass('btn-primary');
                             maq13=4;
                            $('#field8').val(4);">Agree a lot</div><script>var maq13_options = [1,2,3,4];
        </script><div id="field8_noEntry" class="messagefield8 alert alert-danger" style="display: none;">Please indicate your response.</div><div id="field8_notcorrect" class="messagefield8 alert alert-danger" style="display: none;">The value you entered is not correct.</div></div></div><script>function checkValue_field8() {
           var label="maq13";var required=0;var inline=0;var orderoptions=0;var graphical=1;var correct=null;var defaultvalue=null;var multiple=0;var options=null;var clicksave=0;
            if(!(true)) { checker=checker+1; } else {
                var value;
                if (bot) { 
                    if (correct != null) { value = correct; }
                    else if (typeof bot_maq13 !== 'undefined') { value=bot_maq13; }
                    else { 
                    var allvalues=["1","2","3","4"];
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
                        

                       record("maq13", value);

                            /* this variable is created in LionElementButton.class */
                           checker = checker+1;


                }
            
            if (allcorrect!=checker) {
                  wronganswers['maq13']=1;
                       totalwronganswers['maq13'] = isNaN(totalwronganswers['maq13']) ? 1 : totalwronganswers['maq13']+1; 
             
               } else wronganswers['maq13']=0;
            
            
            }
            
            
            
         }



        </script></div><script>if((true)) { $('#wrap8').show(); } </script><!-- END Element 8 Type: 23-->
        
        <!-- START Element 9 Type: 23-->
        
        <div class="col-sm-12" id="wrap9" style="display: none;"><div class="btnbox2"><div class="form-group "><input type="hidden" id="field9"><script>var maq14=null;</script><div style="text-align: center"><label for="field9"><br><b>14. Being close to someone gives me a source of strength for other activities. </b></label></div><div
            id="button91"

            class="choicebuttons9 btn btn-default" onclick="$('.choicebuttons9').removeClass('btn-primary');
                            $('#button91').addClass('btn-primary');
                             maq14=1;
                            $('#field9').val(1);">Disagree a lot</div><div
            id="button92"

            class="choicebuttons9 btn btn-default" onclick="$('.choicebuttons9').removeClass('btn-primary');
                            $('#button92').addClass('btn-primary');
                             maq14=2;
                            $('#field9').val(2);">Disagree a little</div><div
            id="button93"

            class="choicebuttons9 btn btn-default" onclick="$('.choicebuttons9').removeClass('btn-primary');
                            $('#button93').addClass('btn-primary');
                             maq14=3;
                            $('#field9').val(3);">Agree a little</div><div
            id="button94"

            class="choicebuttons9 btn btn-default" onclick="$('.choicebuttons9').removeClass('btn-primary');
                            $('#button94').addClass('btn-primary');
                             maq14=4;
                            $('#field9').val(4);">Agree a lot</div><script>var maq14_options = [1,2,3,4];
        </script><div id="field9_noEntry" class="messagefield9 alert alert-danger" style="display: none;">Please indicate your response.</div><div id="field9_notcorrect" class="messagefield9 alert alert-danger" style="display: none;">The value you entered is not correct.</div></div></div><script>function checkValue_field9() {
           var label="maq14";var required=0;var inline=0;var orderoptions=0;var graphical=1;var correct=null;var defaultvalue=null;var multiple=0;var options=null;var clicksave=0;
            if(!(true)) { checker=checker+1; } else {
                var value;
                if (bot) { 
                    if (correct != null) { value = correct; }
                    else if (typeof bot_maq14 !== 'undefined') { value=bot_maq14; }
                    else { 
                    var allvalues=["1","2","3","4"];
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
                        

                       record("maq14", value);

                            /* this variable is created in LionElementButton.class */
                           checker = checker+1;


                }
            
            if (allcorrect!=checker) {
                  wronganswers['maq14']=1;
                       totalwronganswers['maq14'] = isNaN(totalwronganswers['maq14']) ? 1 : totalwronganswers['maq14']+1; 
             
               } else wronganswers['maq14']=0;
            
            
            }
            
            
            
         }



        </script></div><script>if((true)) { $('#wrap9').show(); } </script><!-- END Element 9 Type: 23-->
        
        <!-- START Element 10 Type: 18-->
        
        <div class="col-sm-12" id="wrap10" style="display: none;">
        <script>
       
        
        </script>
        
        <div  id="button10">
        <div id="buttonclick10" class="lionessbutton btn btn-default btn-lg btn-block " style=" white-space:normal !important; word-wrap: break-word;" onclick="
        $(this).hide(); $('#buttonload10').show();
        if (additionalCheck10()) {
            hideError10();
            if (checkEntries()) toNextPage10();
            else  { $(this).show(); 
            $('#buttonload10').hide(); }
        } else {
         $(this).show(); 
         $('#buttonload10').hide();
         }
        ">Continue</div><div id="buttonload10" style="width: 100%; text-align: center; display: none;"><img src="<?php echo PATH;?>basis/pic/buttonload.gif"></div><div id="field10_error" class="alert alert-danger" style="display: none; text-align: center;"></div><div id="field10_attempts" class="alert alert-warning" style="display: none; text-align: center;"><span class="attempts_text">Attempts left to answer the control questions</span>:&nbsp;<span id="field10_attempts_num"></span></div></div><script>if(maxFalse!=null) {
            var numFails=quizFail(playerNr,1);  
            $('#field10_attempts').show();
            $('#field10_attempts_num').html(maxFalse-numFails);
           
        }
        function showError10(text) {
            var errorfield= $('#field10_error');
            errorfield.show();
            errorfield.html(text);
        
        }
        
        function hideError10() {
            $('#field10_error').hide();
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
        
        function additionalCheck10() {

           return true;
        }

       



        function checkFail() {} function toNextPage10() {
            if (loopEnd==326684) { showNext('wait326684.php?session_index=<?php echo $_SESSION[sessionID];?>',326685,326684);}
            else {showNext('stage326685.php?session_index=<?php echo $_SESSION[sessionID];?>',326685,326684);}

            };</script></div><script>if((true)) { $('#wrap10').show(); $('#buttonclick10').addClass('buttonclick');} </script><!-- END Element 10 Type: 18-->
        
        </div><script>setInterval(function(){ if (true) $('#wrap2').show();if (!(true)) $('#wrap2').hide();if (true) $('#wrap3').show();if (!(true)) $('#wrap3').hide();if (true) $('#wrap4').show();if (!(true)) $('#wrap4').hide();if (true) $('#wrap5').show();if (!(true)) $('#wrap5').hide();if (true) $('#wrap6').show();if (!(true)) $('#wrap6').hide();if (true) $('#wrap7').show();if (!(true)) $('#wrap7').hide();if (true) $('#wrap8').show();if (!(true)) $('#wrap8').hide();if (true) $('#wrap9').show();if (!(true)) $('#wrap9').hide();if (true) $('#wrap10').show();if (!(true)) $('#wrap10').hide(); }, 100);</script></form></div></div></body></html>