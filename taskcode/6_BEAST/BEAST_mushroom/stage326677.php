<html>
        <head>
        
        <?php
    
        include("_projectID.php");
        include(PATH."basis/participant/header.php");
	    $_SESSION['projectID']=PROJECTID;
	    
	    ?>

        <link href="<?php echo PATH;?>basis/css/newlayout.css?v1" rel="stylesheet" type="text/css"  />
        <link href="<?php echo PATH;?>basis/css/newlayout_bootstrap.css" rel="stylesheet" type="text/css"  />
        <link href="<?php echo PATH;?>basis/css/grid.css" rel="stylesheet" type="text/css"  /><title>estimate</title>

        <script> var v={}; var wronganswers={}; var totalwronganswers={};var maxFalse = null;
        var firstStageExp = <?php echo json_encode(FIRSTPAGE . ".php"); ?>;
        var thisPage = <?php echo json_encode($thisPage); ?>;
        var sessionIndexJavascript = "<?php echo $_SESSION[sessionID];?>";
        pageRefreshed=0;
        var loopBegin = "stage" + loopStart + ".php";
        var afterLoopEnd = 326676;
        if (thisPage == firstStageExp || (thisPage==loopBegin && period > 1) || loopEnd==afterLoopEnd) firstStage();
        /* if (thisPage == firstStageExp || thisPage==loopBegin || loopEnd==afterLoopEnd) firstStage(); */
        TimeOut=30;
        function skipStage(proceedifpossible) {
         if (proceedifpossible === undefined) proceedifpossible = false;
         if (proceedifpossible) location.replace('stage326678.php?session_index=<?php echo $_SESSION[sessionID];?>');
         else location.replace('wait326677.php?session_index=<?php echo $_SESSION[sessionID];?>');
        }
        $(document).ready(function(){
        if (bot) { document.getElementsByClassName("buttonclick")[0].click(); }
        });
        
        </script>
        </head><body><div id="mainwrap" class="container" style="width: 100%; padding-left: 5%; padding-right: 5%; padding-top: 1%;"><form autocomplete="off"><div class="row"><!-- START Element 1 Type: 19-->
        
        
        <script>//store all the names of the animals
var animal_names =['mieren', 'bijen', 'flamingo&#8217;s', 'kraanvogels', 'krekels'];

var animal_name = animal_names[(period-1)%5];

iter = 1 + (period-1)%5;

if (period==1) TimeOut = 45;

if (bot) estimate = 30 + Math.round(Math.random() * 50);</script><!-- END Element 1 Type: 19-->
        
        <!-- START Element 2 Type: 1-->
        
        <div class="col-sm-12" id="wrap2" style="display: none;"><div class="btnbox2 paddlr" style="text-align: center"><h3>Ronde <script>document.write(period)</script>: deel A schatting</h3><p>Hoeveel <script>document.write(animal_name)</script> stonden er op het plaatje?</p></div>
        </div><script>if((true)) { $('#wrap2').show(); } </script><!-- END Element 2 Type: 1-->
        
        <!-- START Element 3 Type: 20-->
        
        <div class="col-sm-12" id="wrap3" style="display: none;"><div class="btnbox2"  style="vertical-align: middle;"><div class="form-group btnbox2 btnbox2"><label for="field3"></label><input name="3" id="field3"

                            type="text"

                            size="10"

                            maxlength="10"

                            max="150"

                            step="0"

                            value=""
                            
                            onchange="estimate=parseFloat(this.value);"
                            class="form-control input-lg" style="text-align: center;"><div id="field3_minmax" class=" messagefield3 alert alert-danger" style="display: none;">Please enter a number between 1 and 150.</div><div id="field3_noNumber" class="messagefield3 alert alert-danger" style="display: none;">Please enter a number. </div><div id="field3_tooManyDigits" class="messagefield3 alert alert-danger" style="display: none;">You entered too many digits.</div><div id="field3_notcorrect" class="messagefield3 alert alert-danger" style="display: none;">The value you entered is not correct.</div><script>var estimate=null;function checkValue_field3() {
           var label="estimate";var min=1;var max=150;var digits=0;var correct=null;var required=1;var inline=0;var label1=null;var label2=null;
            if(!(true)) { checker=checker+1; } else {
            
                var value;
                if (bot) { 
                    if (correct != null) { value = correct; }
                    else if (typeof bot_estimate !== 'undefined') { value=bot_estimate; }
                    else { value=Math.floor(Math.random()*max)+min; }
                    value=parseFloat(value);
                }
                else {
                value=($('#field3').val()).trim(); 
                }
                
                $('.messagefield3').hide();
                
                
                
                var allcorrect=checker+1;
                
                /* check if any entry has been made */
                if ((isNaN(value) || value === "") && required==1) {
                    $('#field3_noNumber').show();
                    
                }
                else if (isNaN(value)) {
                    $('#field3_noNumber').show();
                    
                }
                else {
                  


                    var digs = 0;
                    if (value % 1 !==0 && typeof value != undefined) {
                        var testvalue=value.toString();
                        digs = testvalue.split(".")[1].length;
                    }
                    if (digs>digits){ $('#field3_tooManyDigits').show(); }
                    else {
                        if (value>max || value < min) {
                            $('#field3_minmax').show();
                           
                        }
                        else { 

                        if (value!=correct && correct != null && required!=0) {
                           
                           
                            $('#field3_notcorrect').show();
                        } else {


                            record("estimate", value);

                           checker = checker+1;
                       }
                       }
                   }
               }
               if (allcorrect!=checker) {
                  wronganswers['estimate']=1;
                  totalwronganswers['estimate'] = isNaN(totalwronganswers['estimate']) ? 1 : totalwronganswers['estimate']+1; 
                } else wronganswers['estimate']=0;
            }

}

        </script></div></div></div><script>if((true)) { $('#wrap3').show(); } </script><!-- END Element 3 Type: 20-->
        
        <!-- START Element 4 Type: 18-->
        
        <div class="col-sm-12" id="wrap4" style="display: none;">
        <script>
       
        
        </script>
        
        <div  id="button4">
        <div id="buttonclick4" class="lionessbutton btn btn-default btn-lg btn-block " style=" white-space:normal !important; word-wrap: break-word;" onclick="
        $(this).hide(); $('#buttonload4').show();
        if (additionalCheck4()) {
            hideError4();
            if (checkEntries()) toNextPage4();
            else  { $(this).show(); 
            $('#buttonload4').hide(); }
        } else {
         $(this).show(); 
         $('#buttonload4').hide();
         }
        ">Ga verder</div><div id="buttonload4" style="width: 100%; text-align: center; display: none;"><img src="<?php echo PATH;?>basis/pic/buttonload.gif"></div><div id="field4_error" class="alert alert-danger" style="display: none; text-align: center;"></div><div id="field4_attempts" class="alert alert-warning" style="display: none; text-align: center;"><span class="attempts_text">Attempts left to answer the control questions</span>:&nbsp;<span id="field4_attempts_num"></span></div></div><script>if(maxFalse!=null) {
            var numFails=quizFail(playerNr,1);  
            $('#field4_attempts').show();
            $('#field4_attempts_num').html(maxFalse-numFails);
           
        }
        function showError4(text) {
            var errorfield= $('#field4_error');
            errorfield.show();
            errorfield.html(text);
        
        }
        
        function hideError4() {
            $('#field4_error').hide();
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
        
        function additionalCheck4() {

           return true;
        }

       



        function checkFail() {} function toNextPage4() {
            if (loopEnd==326677) { showNext('wait326677.php?session_index=<?php echo $_SESSION[sessionID];?>',326678,326677);}
            else {showNext('stage326678.php?session_index=<?php echo $_SESSION[sessionID];?>',326678,326677);}

            };</script></div><script>if((true)) { $('#wrap4').show(); $('#buttonclick4').addClass('buttonclick');} </script><!-- END Element 4 Type: 18-->
        
        </div><script>setInterval(function(){ if (true) $('#wrap2').show();if (!(true)) $('#wrap2').hide();if (true) $('#wrap3').show();if (!(true)) $('#wrap3').hide();if (true) $('#wrap4').show();if (!(true)) $('#wrap4').hide(); }, 100);</script></form></div></div></body></html>