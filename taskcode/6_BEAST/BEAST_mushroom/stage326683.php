<html>
        <head>
        
        <?php
    
        include("_projectID.php");
        include(PATH."basis/participant/header.php");
	    $_SESSION['projectID']=PROJECTID;
	    
	    ?>

        <link href="<?php echo PATH;?>basis/css/newlayout.css?v1" rel="stylesheet" type="text/css"  />
        <link href="<?php echo PATH;?>basis/css/newlayout_bootstrap.css" rel="stylesheet" type="text/css"  />
        <link href="<?php echo PATH;?>basis/css/grid.css" rel="stylesheet" type="text/css"  /><title>Questionnaire 2</title>

        <script> var v={}; var wronganswers={}; var totalwronganswers={};var maxFalse = null;
        var firstStageExp = <?php echo json_encode(FIRSTPAGE . ".php"); ?>;
        var thisPage = <?php echo json_encode($thisPage); ?>;
        var sessionIndexJavascript = "<?php echo $_SESSION[sessionID];?>";
        pageRefreshed=0;
        var loopBegin = "stage" + loopStart + ".php";
        var afterLoopEnd = 326682;
        if (thisPage == firstStageExp || (thisPage==loopBegin && period > 1) || loopEnd==afterLoopEnd) firstStage();
        /* if (thisPage == firstStageExp || thisPage==loopBegin || loopEnd==afterLoopEnd) firstStage(); */
        TimeOut=null;
        function skipStage(proceedifpossible) {
         if (proceedifpossible === undefined) proceedifpossible = false;
         if (proceedifpossible) location.replace('stage326684.php?session_index=<?php echo $_SESSION[sessionID];?>');
         else location.replace('wait326683.php?session_index=<?php echo $_SESSION[sessionID];?>');
        }
        $(document).ready(function(){
        if (bot) { document.getElementsByClassName("buttonclick")[0].click(); }
        });
        
        </script>
        </head><body><div id="mainwrap" class="container" style="width: 100%; padding-left: 5%; padding-right: 5%; padding-top: 1%;"><form autocomplete="off"><div class="row"><!-- START Element 1 Type: 19-->
        
        
        <script></script><!-- END Element 1 Type: 19-->
        
        <!-- START Element 2 Type: 1-->
        
        <div class="col-sm-12" id="wrap2" style="display: none;"><div class="btnbox2 paddlr" style="text-align: center"><h3>Questionnaire part 2 of 4</h3><p>Please respond to each of the following statements by expressing how much you agree with it (if you do generally
&nbsp;<span style="background-color: rgba(223, 240, 216, 0);">agree)&nbsp;<br></span><span style="background-color: rgba(223, 240, 216, 0);">or how much you disagree with it (if you generally disagree).&nbsp;</span></p><p><span style="background-color: rgba(223, 240, 216, 0);">Please be as accurate as you can be throughout,&nbsp;<br></span><span style="background-color: rgba(223, 240, 216, 0);">and try especially&nbsp;</span><span style="background-color: rgba(223, 240, 216, 0);">hard not to let your answer to any one item influence your answer to any other item.&nbsp;<br></span><span style="background-color: rgba(223, 240, 216, 0);">Treat each one as though it&nbsp;</span><span style="background-color: rgba(223, 240, 216, 0);">is completely unrelated to the others.&nbsp;</span></p><p><span style="background-color: rgba(223, 240, 216, 0);">There are no right or wrong answers, you are simply to express your own&nbsp;</span><span style="background-color: rgba(223, 240, 216, 0);">personal feelings and opinions.</span></p><p></p></div>
        </div><script>if((true)) { $('#wrap2').show(); } </script><!-- END Element 2 Type: 1-->
        
        <!-- START Element 3 Type: 23-->
        
        <div class="col-sm-12" id="wrap3" style="display: none;"><div class="btnbox2"><div class="form-group "><input type="hidden" id="field3"><script>var maq1=null;</script><div style="text-align: center"><label for="field3"><br><b>1. When I&#039;m close to someone, it gives me a sense of comfort about life in general.</b></label></div><div
            id="button31"

            class="choicebuttons3 btn btn-default" onclick="$('.choicebuttons3').removeClass('btn-primary');
                            $('#button31').addClass('btn-primary');
                             maq1=1;
                            $('#field3').val(1);">Disagree a lot</div><div
            id="button32"

            class="choicebuttons3 btn btn-default" onclick="$('.choicebuttons3').removeClass('btn-primary');
                            $('#button32').addClass('btn-primary');
                             maq1=2;
                            $('#field3').val(2);">Disagree a little</div><div
            id="button33"

            class="choicebuttons3 btn btn-default" onclick="$('.choicebuttons3').removeClass('btn-primary');
                            $('#button33').addClass('btn-primary');
                             maq1=3;
                            $('#field3').val(3);">Agree a little</div><div
            id="button34"

            class="choicebuttons3 btn btn-default" onclick="$('.choicebuttons3').removeClass('btn-primary');
                            $('#button34').addClass('btn-primary');
                             maq1=4;
                            $('#field3').val(4);">Agree a lot</div><script>var maq1_options = [1,2,3,4];
        </script><div id="field3_noEntry" class="messagefield3 alert alert-danger" style="display: none;">Please indicate your response.</div><div id="field3_notcorrect" class="messagefield3 alert alert-danger" style="display: none;">The value you entered is not correct.</div></div></div><script>function checkValue_field3() {
           var label="maq1";var required=0;var inline=0;var orderoptions=0;var graphical=1;var correct=null;var defaultvalue=null;var multiple=0;var options=null;var clicksave=0;
            if(!(true)) { checker=checker+1; } else {
                var value;
                if (bot) { 
                    if (correct != null) { value = correct; }
                    else if (typeof bot_maq1 !== 'undefined') { value=bot_maq1; }
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
                        

                       record("maq1", value);

                            /* this variable is created in LionElementButton.class */
                           checker = checker+1;


                }
            
            if (allcorrect!=checker) {
                  wronganswers['maq1']=1;
                       totalwronganswers['maq1'] = isNaN(totalwronganswers['maq1']) ? 1 : totalwronganswers['maq1']+1; 
             
               } else wronganswers['maq1']=0;
            
            
            }
            
            
            
         }



        </script></div><script>if((true)) { $('#wrap3').show(); } </script><!-- END Element 3 Type: 23-->
        
        <!-- START Element 4 Type: 23-->
        
        <div class="col-sm-12" id="wrap4" style="display: none;"><div class="btnbox2"><div class="form-group "><input type="hidden" id="field4"><script>var maq2=null;</script><div style="text-align: center"><label for="field4"><br><b>2. I often worry that my partner doesn&#039;t really love me.</b></label></div><div
            id="button41"

            class="choicebuttons4 btn btn-default" onclick="$('.choicebuttons4').removeClass('btn-primary');
                            $('#button41').addClass('btn-primary');
                             maq2=1;
                            $('#field4').val(1);">Disagree a lot</div><div
            id="button42"

            class="choicebuttons4 btn btn-default" onclick="$('.choicebuttons4').removeClass('btn-primary');
                            $('#button42').addClass('btn-primary');
                             maq2=2;
                            $('#field4').val(2);">Disagree a little</div><div
            id="button43"

            class="choicebuttons4 btn btn-default" onclick="$('.choicebuttons4').removeClass('btn-primary');
                            $('#button43').addClass('btn-primary');
                             maq2=3;
                            $('#field4').val(3);">Agree a little</div><div
            id="button44"

            class="choicebuttons4 btn btn-default" onclick="$('.choicebuttons4').removeClass('btn-primary');
                            $('#button44').addClass('btn-primary');
                             maq2=4;
                            $('#field4').val(4);">Agree a lot</div><script>var maq2_options = [1,2,3,4];
        </script><div id="field4_noEntry" class="messagefield4 alert alert-danger" style="display: none;">Please indicate your response.</div><div id="field4_notcorrect" class="messagefield4 alert alert-danger" style="display: none;">The value you entered is not correct.</div></div></div><script>function checkValue_field4() {
           var label="maq2";var required=0;var inline=0;var orderoptions=0;var graphical=1;var correct=null;var defaultvalue=null;var multiple=0;var options=null;var clicksave=0;
            if(!(true)) { checker=checker+1; } else {
                var value;
                if (bot) { 
                    if (correct != null) { value = correct; }
                    else if (typeof bot_maq2 !== 'undefined') { value=bot_maq2; }
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
                        

                       record("maq2", value);

                            /* this variable is created in LionElementButton.class */
                           checker = checker+1;


                }
            
            if (allcorrect!=checker) {
                  wronganswers['maq2']=1;
                       totalwronganswers['maq2'] = isNaN(totalwronganswers['maq2']) ? 1 : totalwronganswers['maq2']+1; 
             
               } else wronganswers['maq2']=0;
            
            
            }
            
            
            
         }



        </script></div><script>if((true)) { $('#wrap4').show(); } </script><!-- END Element 4 Type: 23-->
        
        <!-- START Element 5 Type: 23-->
        
        <div class="col-sm-12" id="wrap5" style="display: none;"><div class="btnbox2"><div class="form-group "><input type="hidden" id="field5"><script>var maq3=null;</script><div style="text-align: center"><label for="field5"><br><b>3. I have trouble getting others to be as close as I want them to be.</b></label></div><div
            id="button51"

            class="choicebuttons5 btn btn-default" onclick="$('.choicebuttons5').removeClass('btn-primary');
                            $('#button51').addClass('btn-primary');
                             maq3=1;
                            $('#field5').val(1);">Disagree a lot</div><div
            id="button52"

            class="choicebuttons5 btn btn-default" onclick="$('.choicebuttons5').removeClass('btn-primary');
                            $('#button52').addClass('btn-primary');
                             maq3=2;
                            $('#field5').val(2);">Disagree a little</div><div
            id="button53"

            class="choicebuttons5 btn btn-default" onclick="$('.choicebuttons5').removeClass('btn-primary');
                            $('#button53').addClass('btn-primary');
                             maq3=3;
                            $('#field5').val(3);">Agree a little</div><div
            id="button54"

            class="choicebuttons5 btn btn-default" onclick="$('.choicebuttons5').removeClass('btn-primary');
                            $('#button54').addClass('btn-primary');
                             maq3=4;
                            $('#field5').val(4);">Agree a lot</div><script>var maq3_options = [1,2,3,4];
        </script><div id="field5_noEntry" class="messagefield5 alert alert-danger" style="display: none;">Please indicate your response.</div><div id="field5_notcorrect" class="messagefield5 alert alert-danger" style="display: none;">The value you entered is not correct.</div></div></div><script>function checkValue_field5() {
           var label="maq3";var required=0;var inline=0;var orderoptions=0;var graphical=1;var correct=null;var defaultvalue=null;var multiple=0;var options=null;var clicksave=0;
            if(!(true)) { checker=checker+1; } else {
                var value;
                if (bot) { 
                    if (correct != null) { value = correct; }
                    else if (typeof bot_maq3 !== 'undefined') { value=bot_maq3; }
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
                        

                       record("maq3", value);

                            /* this variable is created in LionElementButton.class */
                           checker = checker+1;


                }
            
            if (allcorrect!=checker) {
                  wronganswers['maq3']=1;
                       totalwronganswers['maq3'] = isNaN(totalwronganswers['maq3']) ? 1 : totalwronganswers['maq3']+1; 
             
               } else wronganswers['maq3']=0;
            
            
            }
            
            
            
         }



        </script></div><script>if((true)) { $('#wrap5').show(); } </script><!-- END Element 5 Type: 23-->
        
        <!-- START Element 6 Type: 23-->
        
        <div class="col-sm-12" id="wrap6" style="display: none;"><div class="btnbox2"><div class="form-group "><input type="hidden" id="field6"><script>var maq4=null;</script><div style="text-align: center"><label for="field6"><br><b>4. I find it easy to be close to others.</b></label></div><div
            id="button61"

            class="choicebuttons6 btn btn-default" onclick="$('.choicebuttons6').removeClass('btn-primary');
                            $('#button61').addClass('btn-primary');
                             maq4=1;
                            $('#field6').val(1);">Disagree a lot</div><div
            id="button62"

            class="choicebuttons6 btn btn-default" onclick="$('.choicebuttons6').removeClass('btn-primary');
                            $('#button62').addClass('btn-primary');
                             maq4=2;
                            $('#field6').val(2);">Disagree a little</div><div
            id="button63"

            class="choicebuttons6 btn btn-default" onclick="$('.choicebuttons6').removeClass('btn-primary');
                            $('#button63').addClass('btn-primary');
                             maq4=3;
                            $('#field6').val(3);">Agree a little</div><div
            id="button64"

            class="choicebuttons6 btn btn-default" onclick="$('.choicebuttons6').removeClass('btn-primary');
                            $('#button64').addClass('btn-primary');
                             maq4=4;
                            $('#field6').val(4);">Agree a lot</div><script>var maq4_options = [1,2,3,4];
        </script><div id="field6_noEntry" class="messagefield6 alert alert-danger" style="display: none;">Please indicate your response.</div><div id="field6_notcorrect" class="messagefield6 alert alert-danger" style="display: none;">The value you entered is not correct.</div></div></div><script>function checkValue_field6() {
           var label="maq4";var required=0;var inline=0;var orderoptions=0;var graphical=1;var correct=null;var defaultvalue=null;var multiple=0;var options=null;var clicksave=0;
            if(!(true)) { checker=checker+1; } else {
                var value;
                if (bot) { 
                    if (correct != null) { value = correct; }
                    else if (typeof bot_maq4 !== 'undefined') { value=bot_maq4; }
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
                        

                       record("maq4", value);

                            /* this variable is created in LionElementButton.class */
                           checker = checker+1;


                }
            
            if (allcorrect!=checker) {
                  wronganswers['maq4']=1;
                       totalwronganswers['maq4'] = isNaN(totalwronganswers['maq4']) ? 1 : totalwronganswers['maq4']+1; 
             
               } else wronganswers['maq4']=0;
            
            
            }
            
            
            
         }



        </script></div><script>if((true)) { $('#wrap6').show(); } </script><!-- END Element 6 Type: 23-->
        
        <!-- START Element 7 Type: 23-->
        
        <div class="col-sm-12" id="wrap7" style="display: none;"><div class="btnbox2"><div class="form-group "><input type="hidden" id="field7"><script>var maq5=null;</script><div style="text-align: center"><label for="field7"><br><b>5. I often worry my partner will not want to stay with me.</b></label></div><div
            id="button71"

            class="choicebuttons7 btn btn-default" onclick="$('.choicebuttons7').removeClass('btn-primary');
                            $('#button71').addClass('btn-primary');
                             maq5=1;
                            $('#field7').val(1);">Disagree a lot</div><div
            id="button72"

            class="choicebuttons7 btn btn-default" onclick="$('.choicebuttons7').removeClass('btn-primary');
                            $('#button72').addClass('btn-primary');
                             maq5=2;
                            $('#field7').val(2);">Disagree a little</div><div
            id="button73"

            class="choicebuttons7 btn btn-default" onclick="$('.choicebuttons7').removeClass('btn-primary');
                            $('#button73').addClass('btn-primary');
                             maq5=3;
                            $('#field7').val(3);">Agree a little</div><div
            id="button74"

            class="choicebuttons7 btn btn-default" onclick="$('.choicebuttons7').removeClass('btn-primary');
                            $('#button74').addClass('btn-primary');
                             maq5=4;
                            $('#field7').val(4);">Agree a lot</div><script>var maq5_options = [1,2,3,4];
        </script><div id="field7_noEntry" class="messagefield7 alert alert-danger" style="display: none;">Please indicate your response.</div><div id="field7_notcorrect" class="messagefield7 alert alert-danger" style="display: none;">The value you entered is not correct.</div></div></div><script>function checkValue_field7() {
           var label="maq5";var required=0;var inline=0;var orderoptions=0;var graphical=1;var correct=null;var defaultvalue=null;var multiple=0;var options=null;var clicksave=0;
            if(!(true)) { checker=checker+1; } else {
                var value;
                if (bot) { 
                    if (correct != null) { value = correct; }
                    else if (typeof bot_maq5 !== 'undefined') { value=bot_maq5; }
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
                        

                       record("maq5", value);

                            /* this variable is created in LionElementButton.class */
                           checker = checker+1;


                }
            
            if (allcorrect!=checker) {
                  wronganswers['maq5']=1;
                       totalwronganswers['maq5'] = isNaN(totalwronganswers['maq5']) ? 1 : totalwronganswers['maq5']+1; 
             
               } else wronganswers['maq5']=0;
            
            
            }
            
            
            
         }



        </script></div><script>if((true)) { $('#wrap7').show(); } </script><!-- END Element 7 Type: 23-->
        
        <!-- START Element 8 Type: 23-->
        
        <div class="col-sm-12" id="wrap8" style="display: none;"><div class="btnbox2"><div class="form-group "><input type="hidden" id="field8"><script>var maq6=null;</script><div style="text-align: center"><label for="field8"><br><b>6. Others want me to be more intimate than I feel comfortable being.</b></label></div><div
            id="button81"

            class="choicebuttons8 btn btn-default" onclick="$('.choicebuttons8').removeClass('btn-primary');
                            $('#button81').addClass('btn-primary');
                             maq6=1;
                            $('#field8').val(1);">Disagree a lot</div><div
            id="button82"

            class="choicebuttons8 btn btn-default" onclick="$('.choicebuttons8').removeClass('btn-primary');
                            $('#button82').addClass('btn-primary');
                             maq6=2;
                            $('#field8').val(2);">Disagree a little</div><div
            id="button83"

            class="choicebuttons8 btn btn-default" onclick="$('.choicebuttons8').removeClass('btn-primary');
                            $('#button83').addClass('btn-primary');
                             maq6=3;
                            $('#field8').val(3);">Agree a little</div><div
            id="button84"

            class="choicebuttons8 btn btn-default" onclick="$('.choicebuttons8').removeClass('btn-primary');
                            $('#button84').addClass('btn-primary');
                             maq6=4;
                            $('#field8').val(4);">Agree a lot</div><script>var maq6_options = [1,2,3,4];
        </script><div id="field8_noEntry" class="messagefield8 alert alert-danger" style="display: none;">Please indicate your response.</div><div id="field8_notcorrect" class="messagefield8 alert alert-danger" style="display: none;">The value you entered is not correct.</div></div></div><script>function checkValue_field8() {
           var label="maq6";var required=0;var inline=0;var orderoptions=0;var graphical=1;var correct=null;var defaultvalue=null;var multiple=0;var options=null;var clicksave=0;
            if(!(true)) { checker=checker+1; } else {
                var value;
                if (bot) { 
                    if (correct != null) { value = correct; }
                    else if (typeof bot_maq6 !== 'undefined') { value=bot_maq6; }
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
                        

                       record("maq6", value);

                            /* this variable is created in LionElementButton.class */
                           checker = checker+1;


                }
            
            if (allcorrect!=checker) {
                  wronganswers['maq6']=1;
                       totalwronganswers['maq6'] = isNaN(totalwronganswers['maq6']) ? 1 : totalwronganswers['maq6']+1; 
             
               } else wronganswers['maq6']=0;
            
            
            }
            
            
            
         }



        </script></div><script>if((true)) { $('#wrap8').show(); } </script><!-- END Element 8 Type: 23-->
        
        <!-- START Element 9 Type: 23-->
        
        <div class="col-sm-12" id="wrap9" style="display: none;"><div class="btnbox2"><div class="form-group "><input type="hidden" id="field9"><script>var maq7=null;</script><div style="text-align: center"><label for="field9"><br><b>7. It feels relaxing and good to be close to someone.</b></label></div><div
            id="button91"

            class="choicebuttons9 btn btn-default" onclick="$('.choicebuttons9').removeClass('btn-primary');
                            $('#button91').addClass('btn-primary');
                             maq7=1;
                            $('#field9').val(1);">Disagree a lot</div><div
            id="button92"

            class="choicebuttons9 btn btn-default" onclick="$('.choicebuttons9').removeClass('btn-primary');
                            $('#button92').addClass('btn-primary');
                             maq7=2;
                            $('#field9').val(2);">Disagree a little</div><div
            id="button93"

            class="choicebuttons9 btn btn-default" onclick="$('.choicebuttons9').removeClass('btn-primary');
                            $('#button93').addClass('btn-primary');
                             maq7=3;
                            $('#field9').val(3);">Agree a little</div><div
            id="button94"

            class="choicebuttons9 btn btn-default" onclick="$('.choicebuttons9').removeClass('btn-primary');
                            $('#button94').addClass('btn-primary');
                             maq7=4;
                            $('#field9').val(4);">Agree a lot</div><script>var maq7_options = [1,2,3,4];
        </script><div id="field9_noEntry" class="messagefield9 alert alert-danger" style="display: none;">Please indicate your response.</div><div id="field9_notcorrect" class="messagefield9 alert alert-danger" style="display: none;">The value you entered is not correct.</div></div></div><script>function checkValue_field9() {
           var label="maq7";var required=0;var inline=0;var orderoptions=0;var graphical=1;var correct=null;var defaultvalue=null;var multiple=0;var options=null;var clicksave=0;
            if(!(true)) { checker=checker+1; } else {
                var value;
                if (bot) { 
                    if (correct != null) { value = correct; }
                    else if (typeof bot_maq7 !== 'undefined') { value=bot_maq7; }
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
                        

                       record("maq7", value);

                            /* this variable is created in LionElementButton.class */
                           checker = checker+1;


                }
            
            if (allcorrect!=checker) {
                  wronganswers['maq7']=1;
                       totalwronganswers['maq7'] = isNaN(totalwronganswers['maq7']) ? 1 : totalwronganswers['maq7']+1; 
             
               } else wronganswers['maq7']=0;
            
            
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
            if (loopEnd==326683) { showNext('wait326683.php?session_index=<?php echo $_SESSION[sessionID];?>',326684,326683);}
            else {showNext('stage326684.php?session_index=<?php echo $_SESSION[sessionID];?>',326684,326683);}

            };</script></div><script>if((true)) { $('#wrap10').show(); $('#buttonclick10').addClass('buttonclick');} </script><!-- END Element 10 Type: 18-->
        
        </div><script>setInterval(function(){ if (true) $('#wrap2').show();if (!(true)) $('#wrap2').hide();if (true) $('#wrap3').show();if (!(true)) $('#wrap3').hide();if (true) $('#wrap4').show();if (!(true)) $('#wrap4').hide();if (true) $('#wrap5').show();if (!(true)) $('#wrap5').hide();if (true) $('#wrap6').show();if (!(true)) $('#wrap6').hide();if (true) $('#wrap7').show();if (!(true)) $('#wrap7').hide();if (true) $('#wrap8').show();if (!(true)) $('#wrap8').hide();if (true) $('#wrap9').show();if (!(true)) $('#wrap9').hide();if (true) $('#wrap10').show();if (!(true)) $('#wrap10').hide(); }, 100);</script></form></div></div></body></html>