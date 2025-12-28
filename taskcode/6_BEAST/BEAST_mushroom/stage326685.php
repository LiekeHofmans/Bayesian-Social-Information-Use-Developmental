<html>
        <head>
        
        <?php
    
        include("_projectID.php");
        include(PATH."basis/participant/header.php");
	    $_SESSION['projectID']=PROJECTID;
	    
	    ?>

        <link href="<?php echo PATH;?>basis/css/newlayout.css?v1" rel="stylesheet" type="text/css"  />
        <link href="<?php echo PATH;?>basis/css/newlayout_bootstrap.css" rel="stylesheet" type="text/css"  />
        <link href="<?php echo PATH;?>basis/css/grid.css" rel="stylesheet" type="text/css"  /><title>Questionnaire 4</title>

        <script> var v={}; var wronganswers={}; var totalwronganswers={};var maxFalse = null;
        var firstStageExp = <?php echo json_encode(FIRSTPAGE . ".php"); ?>;
        var thisPage = <?php echo json_encode($thisPage); ?>;
        var sessionIndexJavascript = "<?php echo $_SESSION[sessionID];?>";
        pageRefreshed=0;
        var loopBegin = "stage" + loopStart + ".php";
        var afterLoopEnd = 326684;
        if (thisPage == firstStageExp || (thisPage==loopBegin && period > 1) || loopEnd==afterLoopEnd) firstStage();
        /* if (thisPage == firstStageExp || thisPage==loopBegin || loopEnd==afterLoopEnd) firstStage(); */
        TimeOut=null;
        function skipStage(proceedifpossible) {
         if (proceedifpossible === undefined) proceedifpossible = false;
         if (proceedifpossible) location.replace('stage326686.php?session_index=<?php echo $_SESSION[sessionID];?>');
         else location.replace('wait326685.php?session_index=<?php echo $_SESSION[sessionID];?>');
        }
        $(document).ready(function(){
        if (bot) { document.getElementsByClassName("buttonclick")[0].click(); }
        });
        
        </script>
        </head><body><div id="mainwrap" class="container" style="width: 100%; padding-left: 5%; padding-right: 5%; padding-top: 1%;"><form autocomplete="off"><div class="row"><!-- START Element 1 Type: 19-->
        
        
        <script>iter = getValue('iterationQ');

traits = ['Think of this ladder as representing where people from your country stand in terms of their <b>social status</b>. <br>The most prestigious people (who, for example, are generally respected by others) are at the top, the least prestigious people are at the bottom.',
        'Think of this ladder as representing where people from your country stand in terms of their <b>dominance</b>. <br>The people with the most dominant personality (who, for example, enjoy having control over others) are at the top, the people with the least dominant personality are at the bottom.',
        'Think of this ladder as representing where people from your country stand in terms of their <b>popularity</b>. <br>The most popular people (who, for example, have many friends) are at the top, the least popular people are at the bottom.',      
        'Think of this ladder as representing where people from your country stand in terms of their <b>intelligence</b>. <br>The most intelligent people (who, for example, are vey skilled in solving complex problems) are at the top, the least intelligent people are at the bottom.',
        'Think of this ladder as representing where <i>families</i> from your country stand in terms of their <b>wealth</b>. <br>The most wealthy families are at the top, the poorest families are at the bottom.'];
        
traitT = traits[iter];

variables = ['socialLadder', 'dominanceLadder', 'popularityLadder', 'intelligenceLadder', 'economicsLadder'];
thisVariable = variables[iter];

questionT = '<b>Where would you place yourself on this ladder?</b>';
if (iter==4) questionT = '<b>Where would you place <i>the family you grew up in</i> on this ladder?</b>';

if (iter==0) questionT+='<br> Click on the human icon on the rung where you think you should stand, relative to other people from your country.'</script><!-- END Element 1 Type: 19-->
        
        <!-- START Element 2 Type: 1-->
        
        <div class="col-sm-12" id="wrap2" style="display: none;"><div class="btnbox2 paddlr" style="text-align: center"><h3>Questionnaire part 4 of 4</h3><p><script>document.write(traitT)</script></p><p><span style="background-color: initial;"><script>document.write(questionT)</script></span></p></div>
        </div><script>if((true)) { $('#wrap2').show(); } </script><!-- END Element 2 Type: 1-->
        
        <!-- START Element 3 Type: 19-->
        
        
        <script>var ladder = '<div style="text-align:center;"><svg width="300" height="600" align="center">';
ladder += '<style>margin-left:auto; margin-right:auto; display:block;</style>';

ladder += '<line x1="0" y1="580" x2="50" y2="30" style="stroke:rgb(0,0,0);stroke-width:2" />'
ladder += '<line x1="50" y1="580" x2="100" y2="30" style="stroke:rgb(0,0,0);stroke-width:2" />'

var headSize = 5;
var bodyWidth = 8;

var selectedPosition = 0;
$(function(){
    $(".clickOption").on("click",function(){
        var id = this.id;
        selectedPosition = parseInt(id.substr(3));
        $(".clickOption").css({fill: "lightgrey", cursor: "pointer"});
        $(this).css({ fill: "blue" });
    });
});


var cnt=1;
for (var i=540; i>=60; i=i-50){
    x1 = (560-i) / 11
    x2 = x1+50
   ladder += '<line x1="'+ x1 +'" y1="' + i +'" x2="'+ x2 + '" y2="'+i+'" style="stroke:rgb(0,0,0);stroke-width:2" />' 
   
   // add the man to the ladder
   var man;
    var yStart = i-45;

    var xStart = x1 + 25;
    
    xpos = xStart;
    xposLeft = xpos-8;
    xposLeftLeg = xpos-33/5+0.02;
    xposRightLeg = xpos+2/5+0.02;
    ypos = yStart + 4;
    bodyPos = yStart + 90/5;
    yposLegs = yStart + 140/5;
    
    man += '<g id="man' + cnt + '" class="clickOption" fill="lightgrey">  <circle cx= "' + xpos + '" cy="' + ypos + '" r="'+ headSize+ '" />';
    man += ' <circle cx= "' + xpos + '" cy="' + bodyPos + '" r="'+ bodyWidth + '" />';
    man += ' <rect x= "' + xposLeft + '" y="' + bodyPos + '" width="16" height="12" />';
    man += ' <rect x= "' + xposLeftLeg + '" y="' + yposLegs + '" width="5.5" height="16" />';
    man += ' <rect x= "' + xposRightLeg + '" y="' + yposLegs + '" width="5.5" height="16" />';
    man += '</g>';
    
    ladder+=man;
    ++cnt;
}

ladder += '</svg></div>';

document.write(ladder);</script><!-- END Element 3 Type: 19-->
        
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
        ">Continue</div><div id="buttonload4" style="width: 100%; text-align: center; display: none;"><img src="<?php echo PATH;?>basis/pic/buttonload.gif"></div><div id="field4_error" class="alert alert-danger" style="display: none; text-align: center;"></div><div id="field4_attempts" class="alert alert-warning" style="display: none; text-align: center;"><span class="attempts_text">Attempts left to answer the control questions</span>:&nbsp;<span id="field4_attempts_num"></span></div></div><script>if(maxFalse!=null) {
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
        
        function additionalCheck4() {if (selectedPosition > 0) {setValue(thisVariable, selectedPosition); }

           return true;
        }

       



        function checkFail() {} function toNextPage4() {
            if (loopEnd==326685) { showNext('wait326685.php?session_index=<?php echo $_SESSION[sessionID];?>',326686,326685);}
            else {showNext('stage326686.php?session_index=<?php echo $_SESSION[sessionID];?>',326686,326685);}

            };</script></div><script>if((true)) { $('#wrap4').show(); $('#buttonclick4').addClass('buttonclick');} </script><!-- END Element 4 Type: 18-->
        
        </div><script>setInterval(function(){ if (true) $('#wrap2').show();if (!(true)) $('#wrap2').hide();if (true) $('#wrap4').show();if (!(true)) $('#wrap4').hide(); }, 100);</script></form></div></div></body></html>