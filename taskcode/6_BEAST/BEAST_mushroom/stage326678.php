<html>
        <head>
        
        <?php
    
        include("_projectID.php");
        include(PATH."basis/participant/header.php");
	    $_SESSION['projectID']=PROJECTID;
	    
	    ?>

        <link href="<?php echo PATH;?>basis/css/newlayout.css?v1" rel="stylesheet" type="text/css"  />
        <link href="<?php echo PATH;?>basis/css/newlayout_bootstrap.css" rel="stylesheet" type="text/css"  />
        <link href="<?php echo PATH;?>basis/css/grid.css" rel="stylesheet" type="text/css"  /><title>revise</title>

        <script> var v={}; var wronganswers={}; var totalwronganswers={};var maxFalse = null;
        var firstStageExp = <?php echo json_encode(FIRSTPAGE . ".php"); ?>;
        var thisPage = <?php echo json_encode($thisPage); ?>;
        var sessionIndexJavascript = "<?php echo $_SESSION[sessionID];?>";
        pageRefreshed=0;
        var loopBegin = "stage" + loopStart + ".php";
        var afterLoopEnd = 326677;
        if (thisPage == firstStageExp || (thisPage==loopBegin && period > 1) || loopEnd==afterLoopEnd) firstStage();
        /* if (thisPage == firstStageExp || thisPage==loopBegin || loopEnd==afterLoopEnd) firstStage(); */
        TimeOut=45;
        function skipStage(proceedifpossible) {
         if (proceedifpossible === undefined) proceedifpossible = false;
         if (proceedifpossible) location.replace('stage326679.php?session_index=<?php echo $_SESSION[sessionID];?>');
         else location.replace('wait326678.php?session_index=<?php echo $_SESSION[sessionID];?>');
        }
        $(document).ready(function(){
        if (bot) { document.getElementsByClassName("buttonclick")[0].click(); }
        });
        
        </script>
        </head><body><div id="mainwrap" class="container" style="width: 100%; padding-left: 5%; padding-right: 5%; padding-top: 1%;"><form autocomplete="off"><div class="row"><!-- START Element 1 Type: 19-->
        
        
        <script>iter = 1 + (period-1)%5;


if (period==1) TimeOut = 60;

var numbers = [93,78,59,74,69];
corr = numbers[iter-1];

var animal_names =['mieren', 'bijen', 'flamingo&#8217;s', 'kraanvogels', 'krekels'];

var animal_name = animal_names[(period-1)%5];
firstGuess = getValue('estimate');

maleMat = [
[ 45 , 70 , 45 , 42 , 64 , 90 , 30 , 80 , 70 , 55 , 55 , 70 , 37 , 43 , 32 , 80 , 63 , 72 , 80 , 37 , 85 , 45 , 55 , 40 , 30 , 40 , 75 , 45 , 99 , 46 , 70 , 87 , 32 , 68 , 25 , 30 , 72 , 53 , 54 , 53 , 58 , 83 , 47 , 84 , 70 , 55 , 60 , 50 , 62 , 80 , 110 , 52 , 70 , 120 , 85 , 52 , 30 , 120 , 34 , 30 , 50 , 52 , 62 , 65 , 75 , 60 , 80 , 30 , 80 , 40 , 62 , 42 , 40 , 40 , 36 , 84 , 35 , 69 , 45 , 45 , 31 , 54 , 65 , 33 , 80 , 45 , 79 , 60 , 60 , 70 , 65 , 46 , 57 , 54 , 46 , 30 , 45 , 37 , 47 , 40 , 60 , 70 , 65 , 70 , 50 , 60 , 40 , 53 , 40 , 64 , 32 , 46 , 60 , 40 , 90 , 50 , 52 , 80 , 37 , 62 , 45 , 80 , 78 , 75 , 80 , 60 ],    
[ 50 , 89 , 80 , 55 , 68 , 96 , 25 , 75 , 110 , 70 , 69 , 65 , 63 , 60 , 26 , 75 , 57 , 62 , 75 , 48 , 120 , 50 , 65 , 40 , 40 , 40 , 65 , 60 , 77 , 60 , 85 , 92 , 30 , 55 , 40 , 45 , 80 , 82 , 62 , 56 , 43 , 95 , 72 , 123 , 85 , 45 , 85 , 60 , 75 , 75 , 105 , 70 , 65 , 100 , 87 , 40 , 35 , 90 , 58 , 30 , 60 , 52 , 75 , 60 , 60 , 70 , 100 , 40 , 90 , 45 , 58 , 50 , 60 , 64 , 56 , 98 , 55 , 61 , 65 , 40 , 34 , 80 , 70 , 56 , 80 , 67 , 79 , 80 , 90 , 95 , 83 , 48 , 64 , 61 , 50 , 42 , 46 , 36 , 64 , 60 , 55 , 65 , 80 , 75 , 45 , 60 , 50 , 66 , 35 , 58 , 27 , 52 , 80 , 50 , 101 , 60 , 64 , 70 , 46 , 49 , 60 , 70 , 63 , 80 , 70 , 78 ], 
[ 32 , 68 , 45 , 37 , 50 , 83 , 32 , 64 , 60 ,  45 , 42 , 55 , 39 , 32 , 20 , 72 , 55 , 48 , 60 , 49 , 75 , 55 , 45 , 35 , 40 , 36 , 55 , 40 , 72 , 48 , 38 , 58 , 26 , 49 , 48 , 42 , 45 , 57 , 45 , 51 , 38 , 85 , 64 , 94 , 80 , 62 , 45 , 45 , 67 , 55 , 74 , 43 , 60 , 60 , 57 , 37 , 30 , 65 , 55 , 30 , 45 , 58 , 52 , 63 , 55 , 55 , 75 , 35 , 55 , 35 , 64 , 35 , 48 , 45 , 54 , 75 , 50 , 55 , 45 , 48 , 28 , 60 , 55 , 38 , 68 , 55 , 60 , 45 , 70 , 55 , 57 , 38 , 60 , 52 , 50 , 37 , 35 , 42 , 56 , 60 , 50 , 60 , 45 , 75 , 34 , 57 , 45 , 45 , 25 , 77 , 32 , 43 , 50 , 50 , 59 , 65 , 63 , 55 , 48 , 39 , 40 , 75 , 74 , 55 , 65 , 33 ],      
[ 40 , 80 , 90 , 80 , 60 , 114 , 35 , 60 , 75 ,  70 , 63 , 70 , 85 , 53 , 34 , 78 , 76 , 58 , 65 , 58 , 130 , 56 , 80 , 53 , 50 , 47 , 80 , 70 , 110 , 70 , 54 , 76 , 36 , 70 , 53 , 58 , 80 , 77 , 70 , 68 , 67 , 95 , 80 , 76 , 75 , 53 , 55 , 55 , 87 , 85 , 90 , 57 , 80 , 80 , 100 , 53 , 40 , 110 , 70 , 30 , 68 , 58 , 106 , 75 , 82 , 65 , 50 , 46 , 70 , 41 , 73 , 45 , 75 , 70 , 75 , 73 , 62 , 67 , 66 , 60 , 45 , 55 , 76 , 60 , 80 , 75 , 81 , 70 , 110 , 70 , 56 , 52 , 58 , 79 , 73 , 53 , 50 , 57 , 73 , 100 , 65 , 65 , 62 , 70 , 59 , 68 , 60 , 55 , 50 , 95 , 65 , 50 , 80 , 60 , 79 , 69 , 60 , 60 , 52 , 54 , 70 , 95 , 82 , 72 , 75 , 68 ],
[ 45 , 69 , 60 , 64 , 60 , 74 , 30 , 67 , 55 ,  50 , 47 , 70 , 67 , 43 , 28 , 72 , 66 , 58 , 70 , 47 , 80 , 62 , 50 , 42 , 60 , 48 , 60 , 50 , 80 , 42 , 57 , 65 , 38 , 55 , 65 , 60 , 84 , 70 , 38 , 65 , 41 , 82 , 68 , 63 , 70 , 32 , 43 , 50 , 60 , 79 , 60 , 63 , 50 , 75 , 83 , 52 , 35 , 70 , 70 , 25 , 65 , 58 , 95 , 70 , 73 , 45 , 84 , 55 , 60 , 45 , 63 , 50 , 45 , 78 , 63 , 87 , 60 , 72 , 75 , 46 , 32 , 59 , 67 , 72 , 70 , 60 , 67 , 85 , 76 , 50 , 72 , 49 , 57 , 53 , 70 , 55 , 58 , 53 , 61 , 50 , 55 , 60 , 75 , 70 , 40 , 60 , 40 , 60 , 37 , 70 , 40 , 37 , 70 , 40 , 54 , 69 , 70 , 70 , 53 , 58 , 46 , 92 , 77 , 78 , 80 , 42 ]
    ];
    
femaleMat = [
[ 65 , 80 , 45 , 200 , 45 , 80 , 64 , 75 , 46 , 100 , 100 , 45 , 40 , 125 , 40 , 50 , 40 , 65 , 58 , 92 , 34 , 30 , 67 , 60 , 48 , 90 , 60 , 110 , 60 , 53 , 50 , 65 , 65 , 55 , 47 , 75 , 50 , 50 , 60 , 68 , 70 , 40 , 60 , 50 , 80 , 65 , 45 , 65 , 70 , 55 , 80 , 40 , 27 , 60 , 60 , 30 , 50 , 70 , 60 , 48 , 65 , 88 , 54 , 50 , 70 , 65 , 30 , 82 , 65 , 45 , 32 , 38 , 75 , 75 , 62 , 60 , 57 , 43 , 56 , 60 , 38 , 56 , 50 , 49 , 43 , 80 , 50 , 45 , 42 , 60 , 70 , 40 , 45 , 100 , 60 , 80 , 75 , 70 , 120 , 98 , 60 , 56 , 32 , 72 , 35 , 75 , 70 , 70 , 44 , 56 , 200 , 53 , 75 , 45 , 45 , 100 , 50 , 53 , 60 , 49 , 63 , 63 , 67 , 80 , 80 , 56 , 35 , 87 , 45 , 78 , 50 , 52 , 75 , 125 , 40 , 50 , 75 , 64 , 35 , 32 , 41 , 78 , 36 , 60 , 67 , 90 , 68 , 50 , 75 , 65 , 60 , 30 , 40 , 100 , 80 , 50 , 65 , 45 , 80 , 56 , 72 , 200 , 67 , 60 , 70 , 45 , 50 , 30 , 39 , 50 , 40 , 51 , 57 , 55 , 48 , 48 , 42 , 45 , 63 , 50 , 70 , 60 , 63 , 70 , 76 , 55 , 36 , 75 , 35 , 80 , 40 , 60 , 50 , 68 , 66 , 60 , 60 , 50 , 40 , 65 , 51 , 60 , 85 , 36 , 45 , 115 , 55 , 43 , 60 , 46 , 42 , 50 , 55 , 80 , 60 , 70 , 65 , 60 , 50 , 50 , 46 , 50 , 45 , 40 , 40 , 65 , 62 , 60 , 50 , 55 , 62 , 80 , 75 , 87 , 95 , 90 , 42 , 60 , 35 , 50 , 50 , 50 , 60 , 100 , 55 , 64 , 75 , 30 , 52 , 70 , 42 , 60 , 50 , 65 , 25 , 46 , 30 , 90 , 80 , 60 , 50 , 54 , 80 , 40 , 67 , 70 , 62 , 44 , 64 , 42 , 34 , 40 , 100 , 35 , 46 , 79 , 32 , 50 , 65 , 35 , 50 , 35 , 60 , 50 , 100 , 55 , 32 , 35 , 80 , 89 , 80 , 75 , 72 , 80 , 55 , 80 , 45 , 46 , 70 , 75 , 35 , 60 , 80 , 50 , 45 , 45 , 100 , 57 , 60 , 50 , 32 , 50 , 87 , 43 , 55 , 80 , 75 , 81 , 50 , 50 , 118 , 83 , 70 , 50 , 40 , 70 , 55 , 60 , 64 ],
[ 83 , 70 , 60 , 120 , 61 , 70 , 82 , 106 , 44 , 80 , 55 , 50 , 50 , 118 , 50 , 70 , 60 , 84 , 55 , 70 , 54 , 60 , 60 , 70 , 59 , 70 , 55 , 70 , 60 , 71 , 77 , 75 , 70 , 53 , 62 , 70 , 55 , 75 , 80 , 89 , 60 , 60 , 75 , 63 , 70 , 65 , 40 , 90 , 90 , 65 , 75 , 56 , 23 , 60 , 60 , 60 , 60 , 82 , 50 , 60 , 64 , 88 , 61 , 70 , 65 , 85 , 40 , 89 , 65 , 36 , 47 , 42 , 80 , 76 , 60 , 80 , 75 , 52 , 74 , 90 , 52 , 80 , 40 , 51 , 60 , 70 , 60 , 50 , 51 , 40 , 65 , 40 , 52 , 60 , 55 , 100 , 70 , 80 , 65 , 68 , 60 , 77 , 28 , 85 , 55 , 61 , 60 , 60 , 46 , 58 , 100 , 63 , 90 , 66 , 40 , 95 , 66 , 70 , 50 , 68 , 48 , 57 , 71 , 78 , 100 , 77 , 45 , 92 , 36 , 108 , 60 , 71 , 75 , 100 , 49 , 70 , 80 , 76 , 45 , 72 , 43 , 58 , 51 , 65 , 70 , 80 , 68 , 70 , 98 , 65 , 70 , 45 , 45 , 50 , 70 , 50 , 59 , 58 , 75 , 55 , 70 , 125 , 60 , 70 , 50 , 56 , 60 , 30 , 42 , 57 , 60 , 54 , 42 , 58 , 57 , 70 , 37 , 65 , 92 , 50 , 45 , 70 , 68 , 54 , 90 , 48 , 55 , 65 , 45 , 50 , 45 , 55 , 60 , 70 , 71 , 80 , 70 , 45 , 50 , 78 , 60 , 80 , 65 , 57 , 55 , 96 , 54 , 63 , 40 , 60 , 70 , 50 , 40 , 90 , 60 , 65 , 60 , 45 , 49 , 35 , 72 , 48 , 63 , 40 , 60 , 75 , 65 , 70 , 45 , 67 , 75 , 60 , 50 , 70 , 76 , 65 , 75 , 78 , 53 , 65 , 60 , 60 , 50 , 50 , 45 , 63 , 80 , 30 , 48 , 75 , 62 , 60 , 60 , 90 , 43 , 51 , 44 , 115 , 80 , 90 , 57 , 36 , 75 , 55 , 72 , 95 , 70 , 50 , 78 , 63 , 43 , 50 , 50 , 47 , 55 , 78 , 35 , 68 , 59 , 50 , 55 , 46 , 60 , 60 , 150 , 73 , 50 , 45 , 115 , 104 , 64 , 90 , 70 , 55 , 60 , 85 , 38 , 56 , 78 , 60 , 40 , 85 , 80 , 55 , 52 , 60 , 75 , 43 , 80 , 60 , 28 , 60 , 96 , 53 , 63 , 70 , 70 , 109 , 39 , 55 , 98 , 78 , 75 , 66 , 80 , 70 , 43 , 55 , 65 ],
[ 62 , 60 , 70 , 90 , 55 , 60 , 48 , 115 , 41 , 60 , 75 , 60 , 35 , 80 , 42 , 55 , 70 , 62 , 50 , 62 , 37 , 55 , 53 , 50 , 49 , 60 , 50 , 50 , 50 , 66 , 48 , 65 , 52 , 49 , 46 , 55 , 53 , 59 , 80 , 56 , 45 , 60 , 63 , 48 , 45 , 60 , 42 , 70 , 70 , 52 , 55 , 30 , 27 , 58 , 45 , 45 , 55 , 62 , 55 , 43 , 68 , 60 , 46 , 60 , 50 , 45 , 25 , 57 , 57 , 25 , 39 , 51 , 55 , 90 , 50 , 40 , 85 , 37 , 45 , 60 , 46 , 48 , 46 , 48 , 54 , 60 , 55 , 27 , 66 , 60 , 65 , 52 , 65 , 50 , 45 , 70 , 65 , 70 , 51 , 65 , 58 , 38 , 21 , 70 , 60 , 53 , 60 , 55 , 41 , 72 , 59 , 58 , 55 , 72 , 44 , 92 , 35 , 55 , 47 , 50 , 56 , 40 , 67 , 70 , 65 , 50 , 40 , 73 , 40 , 63 , 50 , 54 , 65 , 80 , 55 , 43 , 37 , 61 , 45 , 56 , 36 , 72 , 54 , 65 , 48 , 60 , 65 , 64 , 60 , 40 , 65 , 45 , 55 , 45 , 60 , 44 , 55 , 46 , 70 , 48 , 60 , 140 , 60 , 60 , 60 , 49 , 55 , 25 , 35 , 48 , 55 , 57 , 33 , 58 , 47 , 80 , 63 , 50 , 67 , 65 , 52 , 45 , 49 , 60 , 45 , 58 , 50 , 68 , 50 , 42 , 35 , 45 , 45 , 45 , 52 , 50 , 50 , 40 , 60 , 103 , 56 , 50 , 60 , 54 , 65 , 76 , 42 , 46 , 75 , 50 , 102 , 65 , 45 , 60 , 40 , 70 , 60 , 55 , 35 , 28 , 72 , 51 , 66 , 30 , 55 , 55 , 55 , 50 , 48 , 87 , 57 , 78 , 63 , 66 , 63 , 62 , 38 , 60 , 45 , 50 , 45 , 60 , 50 , 60 , 55 , 62 , 73 , 20 , 36 , 50 , 53 , 50 , 65 , 85 , 50 , 59 , 58 , 73 , 63 , 45 , 60 , 46 , 53 , 53 , 66 , 45 , 64 , 65 , 62 , 52 , 31 , 60 , 50 , 30 , 54 , 62 , 41 , 64 , 72 , 46 , 55 , 55 , 60 , 60 , 75 , 64 , 47 , 30 , 70 , 85 , 65 , 60 , 80 , 45 , 45 , 55 , 45 , 45 , 60 , 55 , 36 , 64 , 60 , 48 , 43 , 32 , 80 , 38 , 50 , 30 , 33 , 40 , 83 , 42 , 62 , 63 , 56 , 70 , 55 , 50 , 98 , 72 , 70 , 45 , 71 , 55 , 43 , 45 , 56 ],            
[ 68 , 65 , 65 , 100 , 60 , 75 , 56 , 93 , 65 , 100 , 80 , 70 , 55 , 66 , 60 , 65 , 70 , 68 , 75 , 65 , 78 , 90 , 75 , 70 , 69 , 80 , 75 , 70 , 70 , 70 , 77 , 90 , 77 , 70 , 78 , 68 , 60 , 71 , 85 , 72 , 60 , 60 , 70 , 59 , 60 , 70 , 65 , 100 , 85 , 66 , 78 , 45 , 30 , 82 , 75 , 65 , 65 , 65 , 70 , 69 , 70 , 69 , 59 , 65 , 70 , 85 , 32 , 72 , 70 , 37 , 62 , 60 , 80 , 70 , 60 , 85 , 110 , 62 , 78 , 55 , 53 , 75 , 57 , 69 , 78 , 80 , 70 , 50 , 75 , 70 , 100 , 71 , 60 , 65 , 48 , 90 , 90 , 70 , 73 , 132 , 75 , 66 , 41 , 95 , 70 , 75 , 80 , 70 , 60 , 72 , 70 , 74 , 70 , 55 , 60 , 70 , 43 , 77 , 63 , 41 , 53 , 64 , 81 , 65 , 60 , 65 , 50 , 103 , 48 , 89 , 60 , 78 , 70 , 100 , 62 , 85 , 58 , 94 , 58 , 84 , 46 , 85 , 68 , 70 , 72 , 77 , 67 , 78 , 71 , 70 , 80 , 55 , 45 , 65 , 60 , 67 , 69 , 52 , 100 , 72 , 98 , 130 , 80 , 85 , 74 , 62 , 75 , 50 , 48 , 52 , 80 , 65 , 45 , 68 , 63 , 75 , 58 , 65 , 65 , 80 , 90 , 60 , 78 , 83 , 65 , 40 , 65 , 82 , 60 , 60 , 40 , 60 , 60 , 60 , 56 , 68 , 60 , 60 , 70 , 96 , 65 , 70 , 95 , 69 , 61 , 65 , 57 , 68 , 40 , 70 , 105 , 80 , 68 , 70 , 55 , 78 , 65 , 65 , 65 , 36 , 81 , 68 , 86 , 37 , 70 , 90 , 66 , 65 , 62 , 107 , 72 , 76 , 80 , 71 , 78 , 60 , 53 , 70 , 60 , 80 , 68 , 70 , 80 , 65 , 75 , 78 , 83 , 35 , 52 , 70 , 61 , 55 , 80 , 70 , 59 , 65 , 68 , 115 , 71 , 87 , 66 , 67 , 78 , 74 , 83 , 75 , 72 , 70 , 75 , 88 , 49 , 65 , 60 , 48 , 63 , 65 , 49 , 68 , 83 , 52 , 55 , 63 , 70 , 50 , 85 , 77 , 50 , 50 , 95 , 120 , 78 , 70 , 65 , 50 , 50 , 90 , 52 , 46 , 80 , 60 , 50 , 65 , 75 , 65 , 60 , 68 , 100 , 57 , 90 , 80 , 42 , 70 , 83 , 62 , 68 , 65 , 71 , 97 , 80 , 64 , 105 , 94 , 60 , 73 , 100 , 73 , 67 , 65 , 60 ],
[ 55 , 70 , 60 , 80 , 59 , 65 , 74 , 70 , 70 , 75 , 45 , 70 , 50 , 78 , 50 , 65 , 55 , 56 , 64 , 60 , 40 , 50 , 65 , 55 , 68 , 60 , 55 , 60 , 45 , 80 , 50 , 70 , 62 , 83 , 80 , 70 , 57 , 65 , 65 , 63 , 45 , 50 , 7 , 56 , 60 , 67 , 42 , 75 , 70 , 49 , 60 , 35 , 35 , 90 , 45 , 75 , 65 , 64 , 55 , 55 , 63 , 70 , 53 , 60 , 53 , 50 , 36 , 68 , 60 , 35 , 58 , 47 , 60 , 67 , 57 , 45 , 95 , 50 , 50 , 70 , 61 , 59 , 55 , 75 , 58 , 72 , 55 , 48 , 55 , 50 , 90 , 45 , 50 , 58 , 42 , 100 , 55 , 50 , 62 , 100 , 67 , 73 , 33 , 78 , 65 , 43 , 60 , 70 , 45 , 48 , 60 , 64 , 50 , 45 , 60 , 65 , 45 , 56 , 51 , 48 , 43 , 45 , 64 , 75 , 60 , 63 , 48 , 61 , 45 , 73 , 45 , 66 , 50 , 81 , 45 , 53 , 66 , 63 , 50 , 67 , 40 , 93 , 77 , 70 , 60 , 75 , 64 , 57 , 71 , 65 , 65 , 40 , 60 , 70 , 40 , 54 , 49 , 45 , 80 , 80 , 75 , 145 , 58 , 80 , 63 , 60 , 65 , 35 , 35 , 60 , 70 , 60 , 53 , 58 , 53 , 80 , 64 , 45 , 67 , 80 , 67 , 35 , 64 , 64 , 70 , 44 , 50 , 65 , 40 , 53 , 36 , 50 , 37 , 60 , 57 , 54 , 40 , 52 , 60 , 92 , 70 , 60 , 90 , 49 , 54 , 56 , 48 , 37 , 30 , 70 , 90 , 55 , 67 , 65 , 40 , 68 , 70 , 50 , 42 , 35 , 83 , 56 , 86 , 30 , 60 , 75 , 52 , 60 , 55 , 79 , 67 , 40 , 55 , 55 , 64 , 45 , 48 , 83 , 57 , 67 , 50 , 65 , 70 , 50 , 45 , 72 , 82 , 32 , 48 , 55 , 71 , 60 , 55 , 55 , 58 , 73 , 38 , 85 , 80 , 69 , 46 , 68 , 62 , 63 , 62 , 82 , 56 , 60 , 57 , 73 , 33 , 60 , 60 , 45 , 70 , 68 , 56 , 66 , 57 , 44 , 55 , 37 , 54 , 50 , 90 , 78 , 40 , 37 , 60 , 77 , 58 , 65 , 60 , 42 , 45 , 70 , 44 , 50 , 66 , 45 , 40 , 80 , 68 , 62 , 52 , 52 , 75 , 42 , 60 , 40 , 44 , 80 , 78 , 51 , 65 , 50 , 57 , 49 , 83 , 65 , 78 , 69 , 80 , 65 , 87 , 78 , 39 , 53 , 53 ]
    ]
    
peers = femaleMat[iter-1];
peers = peers.concat(maleMat[iter-1]);

peers.sort(function(a, b){return a-b});

// which deviation applies?
thisDev = 0.2;
// if lower than corr
target = firstGuess * (1 + thisDev);
// if higher than corr
if (firstGuess > corr){
    target = firstGuess * (1 - thisDev);
}
// if guess == corr, random higher or lower
if (firstGuess == corr){
    if (Math.random()<0.5) target = firstGuess * (1 - thisDev);
}

closestNumber = [];
minDev = 10000;
for (var i=0; i<peers.length; i++) {
    var dev = Math.abs(peers[i] - target)
    if (dev < minDev){
        minDev = dev;
        closestNumber=[]
        closestNumber.push(peers[i]);
    }
    if (dev == minDev){
        closestNumber.push(peers[i]);        
    }
}

closestNumber = shuffle(closestNumber);
obsSoc = closestNumber[0];

record('socialInfo', obsSoc);


if (bot) estimate_revised = 30 + Math.round(Math.random() * 50);</script><!-- END Element 1 Type: 19-->
        
        <!-- START Element 2 Type: 1-->
        
        <div class="col-sm-12" id="wrap2" style="display: none;"><div class="btnbox2 paddlr" style="text-align: center"><h3>Ronde <script>document.write(iter)</script>: deel B schatting</h3>Je schatting van <b><script>document.write(firstGuess)</script></b> is opgeslagen.<p><span style="background-color: initial;">We laten je nu de deel A schatting van een eerdere deelnemer zien.<br>Hij/zij zag hetzelfde plaatje als jij net zag. Hij/zij zag dit ook voor 6 seconden.</span></p><p><span style="background-color: initial;">&nbsp;Zijn/haar schatting was</span><span style="background-color: initial;">:&nbsp;</span><b style="background-color: initial;"><script>document.write(obsSoc)</script></b></p><p><span style="background-color: initial;">Je kunt je tweede schatting nu hieronder invullen.</span></p><p></p><p></p></div>
        </div><script>if((true)) { $('#wrap2').show(); } </script><!-- END Element 2 Type: 1-->
        
        <!-- START Element 3 Type: 20-->
        
        <div class="col-sm-12" id="wrap3" style="display: none;"><div class="btnbox2"  style="vertical-align: middle;"><div class="form-group btnbox2 btnbox2"><label for="field3"><b>Hoeveel <script>document.write(animal_name)</script> stonden er op het plaatje?</b></label><input name="3" id="field3"

                            type="text"

                            size="10"

                            maxlength="10"

                            max="150"

                            step="0"

                            value=""
                            
                            onchange="estimate_revised=parseFloat(this.value);"
                            class="form-control input-lg" style="text-align: center;"><div id="field3_minmax" class=" messagefield3 alert alert-danger" style="display: none;">Please enter a number between 0 and 150.</div><div id="field3_noNumber" class="messagefield3 alert alert-danger" style="display: none;">Please enter a number. </div><div id="field3_tooManyDigits" class="messagefield3 alert alert-danger" style="display: none;">You entered too many digits.</div><div id="field3_notcorrect" class="messagefield3 alert alert-danger" style="display: none;">The value you entered is not correct.</div><script>var estimate_revised=null;function checkValue_field3() {
           var label="estimate_revised";var min=0;var max=150;var digits=0;var correct=null;var required=1;var inline=0;var label1=null;var label2=null;
            if(!(true)) { checker=checker+1; } else {
            
                var value;
                if (bot) { 
                    if (correct != null) { value = correct; }
                    else if (typeof bot_estimate_revised !== 'undefined') { value=bot_estimate_revised; }
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


                            record("estimate_revised", value);

                           checker = checker+1;
                       }
                       }
                   }
               }
               if (allcorrect!=checker) {
                  wronganswers['estimate_revised']=1;
                  totalwronganswers['estimate_revised'] = isNaN(totalwronganswers['estimate_revised']) ? 1 : totalwronganswers['estimate_revised']+1; 
                } else wronganswers['estimate_revised']=0;
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
            if (loopEnd==326678) { showNext('wait326678.php?session_index=<?php echo $_SESSION[sessionID];?>',326679,326678);}
            else {showNext('stage326679.php?session_index=<?php echo $_SESSION[sessionID];?>',326679,326678);}

            };</script></div><script>if((true)) { $('#wrap4').show(); $('#buttonclick4').addClass('buttonclick');} </script><!-- END Element 4 Type: 18-->
        
        </div><script>setInterval(function(){ if (true) $('#wrap2').show();if (!(true)) $('#wrap2').hide();if (true) $('#wrap3').show();if (!(true)) $('#wrap3').hide();if (true) $('#wrap4').show();if (!(true)) $('#wrap4').hide(); }, 100);</script></form></div></div></body></html>