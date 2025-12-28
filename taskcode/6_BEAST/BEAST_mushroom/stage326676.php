<html>
        <head>
        
        <?php
    
        include("_projectID.php");
        include(PATH."basis/participant/header.php");
	    $_SESSION['projectID']=PROJECTID;
	    
	    ?>

        <link href="<?php echo PATH;?>basis/css/newlayout.css?v1" rel="stylesheet" type="text/css"  />
        <link href="<?php echo PATH;?>basis/css/newlayout_bootstrap.css" rel="stylesheet" type="text/css"  />
        <link href="<?php echo PATH;?>basis/css/grid.css" rel="stylesheet" type="text/css"  /><title>watch pic</title>

        <script> var v={}; var wronganswers={}; var totalwronganswers={};var maxFalse = null;
        var firstStageExp = <?php echo json_encode(FIRSTPAGE . ".php"); ?>;
        var thisPage = <?php echo json_encode($thisPage); ?>;
        var sessionIndexJavascript = "<?php echo $_SESSION[sessionID];?>";
        pageRefreshed=0;
        var loopBegin = "stage" + loopStart + ".php";
        var afterLoopEnd = 326675;
        if (thisPage == firstStageExp || (thisPage==loopBegin && period > 1) || loopEnd==afterLoopEnd) firstStage();
        /* if (thisPage == firstStageExp || thisPage==loopBegin || loopEnd==afterLoopEnd) firstStage(); */
        TimeOut=6;
        function skipStage(proceedifpossible) {
         if (proceedifpossible === undefined) proceedifpossible = false;
         if (proceedifpossible) location.replace('stage326677.php?session_index=<?php echo $_SESSION[sessionID];?>');
         else location.replace('wait326676.php?session_index=<?php echo $_SESSION[sessionID];?>');
        }
        $(document).ready(function(){
        if (bot) { document.getElementsByClassName("buttonclick")[0].click(); }
        });
        
        </script>
        </head><body><div id="mainwrap" class="container" style="width: 100%; padding-left: 5%; padding-right: 5%; padding-top: 1%;"><form autocomplete="off"><div class="row"><!-- START Element 1 Type: 19-->
        
        
        <script>//get current iteration
var iter = 1 + (period-1)%5;


//store all the names of the animals
var animal_names =['ant', 'bee', 'flamingo', 'crane', 'cricket'];
var parameters = ['antsNumber','beesNumber','flamingosNumber','cranesNumber','cricketsNumber'];

//get number of animals to be printed 
var animal_name = animal_names[iter-1];
numberAnimals = getParameter(parameters[iter-1]);

//get fixed picture parameters from server
var animal_size = getParameter('img_size'); //in px
var overlap_ratio = getParameter('overlap_ratio'); 
var border = getParameter('border');

//get screen size and create final size of the picture
var img_width = screen.width/2; // in px
var img_heigth = screen.height/2; // in px
var total_width = img_width + border;
var total_height = img_heigth + border;

//calculate how many positions in the grid  can be obtained given pic size
n_positions = img_width/(animal_size * (overlap_ratio)); 
n_positions_y = img_heigth/(animal_size * (overlap_ratio)); 

// function to generate random numbers according to seed
// unique seeds are set by the period number
seed = period;
function random() {
    var x = Math.sin(seed++) * img_width; // this assumes a 100x100 grid
    return x - Math.floor(x);
}
// fuction to kick out double entries in an array (to have only unique entries)
function onlyUnique(value, index, self) {
    return self.indexOf(value) === index;
}
 
rnds=[];
for (j=0; j<200; j++) rnds.push(Math.round(random() * img_width));  // draw 200 random numbers
rnds = rnds.filter( onlyUnique ); // remove non-unique values
//document.write(rnds + '<br>') // write to screen for checking
rnds = rnds.slice(0,numberAnimals);
rnds = rnds.sort();

//generate picture
pic = '<div style="text-align:center; margin-left:auto; margin-right:auto">';
pic +='<svg width="'+total_width+'" height="'+total_height+'" style=" background-color: rgb(204,204,255);">';
    //loop through numberAnimals and add pics
for (i = 0; i<numberAnimals; ++i){
    rndx = rnds[i];
    x = rndx%(n_positions)*(img_width/n_positions);
    y = Math.floor(rndx/n_positions)*(n_positions_y);
   pic +='<image xlink:href="pics/'+animal_name+'_small.png" x="'+x+ '" y="'+y+'" height="'+animal_size+'" width="'+animal_size+'"/>';
  }
  
pic+= '</svg> </div>';

document.write(pic)

///////////////// BACKGROUND /////////////////////
var loadBgr = function(){
    var body = document.getElementsByTagName('body')[0];

    body.setAttribute('style', 'background: url(https://arc-vlab.mpib-berlin.mpg.de/BEAST_museum/resources/media/Experiment.jpg) no-repeat bottom left fixed; -webkit-background-size: cover; -moz-background-size: cover; -o-background-size: cover; background-size: cover; ');
 
};

//load background on window load
window.onload = function(){loadBgr(); document.getElementById('countdown_text').innerHTML = 'Resterende tijd: &nbsp;'; };

</script><!-- END Element 1 Type: 19-->
        
        </div><script>setInterval(function(){  }, 100);</script><script>countdownTimer(TimeOut, 'stage326677.php?session_index=<?php echo $_SESSION[sessionID];?>',true);</script></form></div></div></body></html>