<?php


class Pagination
{
    public $currentGame = null;

    public function __construct($path)
    {
        $this->lioness_mode = true;

        $this->path_pagination = $path . 'pagination/';
        $this->path_basis = $path . 'basis/';

    }

    public function getHead()
    {
        $code = '
                    <!DOCTYPE html>
            <!--[if IE 8]> <html lang="en" class="ie8"> <![endif]-->
            <!--[if IE 9]> <html lang="en" class="ie9"> <![endif]-->
            <!--[if !IE]><!--> <html lang="en"> <!--<![endif]-->
            <head>
            <!-- basis folder is base -->
            <base href="'.$this->path_basis.'"/>

            <meta charset="utf-8" />
            <script src="../pagination/assets/jquery-2.2.4.min.js"></script>
            <meta content="width=device-width, initial-scale=1.0" name="viewport" />
            <link href="../pagination/assets/bootstrap/css/bootstrap.min.css" rel="stylesheet" />
            <link href="../pagination/assets/bootstrap/css/bootstrap-responsive.min.css" rel="stylesheet" />
            <link href="../pagination/assets/css/style.css" rel="stylesheet" />
            <link href="../pagination/assets/css/style_responsive.css" rel="stylesheet" />
            <link href="../pagination/assets/css/style_light.css" rel="stylesheet" id="style_color" />
            <script src="controlpanel_js/controllerFunctions.js?v2"></script>
            <script src="jsLibrary.js?v5"></script>
            
    	<title> LIONESS - Control panel </title>
        <link rel="shortcut icon"  href="pic/logo-head.png">';

        return $code;
    }

    public function beginContainer()
    {
        return '<div class="page-content">
			        <!-- BEGIN PAGE CONTAINER-->
			        <div class="container-fluid">
			            <div id="maincontainer">
			                <!-- BEGIN PAGE CONTENT-->
			                <div id="messages" class="row-fluid" style="margin-top: 2px; display: none;">
			                <div id="message_body" style="margin-bottom: 0"></div></div>';
    }

    public function endContainer()
    {
        return '</div>
				<!-- END PAGE CONTENT-->
			</div>
			<!-- END PAGE CONTAINER-->
		</div>
		<!-- END PAGE -->';
    }

    public function getTopNavigationEmpty($projectID)
    {
        return '<body class="fixed-top">
                    <nav class="navbar navbar-header navbar-default navbar-light" style="margin-bottom: 0;">
                        <div class="container">
                            <ul class="nav navbar-right pull-right"></ul>
                        </div>
                    </nav>
                <!-- END TOP NAVIGATION BAR -->
                    <div class="page-container row-fluid">';
    }

    public function getTopNavigation($projectID, $isDemo = false)
    {


        $code = '<body class="fixed-top">
                    <nav class="navbar navbar-header navbar-default navbar-light" style="margin-bottom: 0;">
                        <div class="container">
                        <div class="nav navbar-nav navbar-brand"><img src="../pagination/pic/lionlogo.svg" width="30px"></div>';

        $code .= $this->getTopNavigationLeft($isDemo);


        $code .= '<ul class="nav navbar-right pull-right">

                    <li class="dropdown">
                      
                      <a class="dropdown-toggle" data-toggle="dropdown" role="button"
                        aria-haspopup="true" aria-expanded="false" style="cursor: pointer;">
                        <span style="font-weight: bolder">menu</span><span class="caret"></span></a>
                    <ul class="dropdown-menu">
                    <li><a data-target="#" onclick="terminatePlayer($(\'#terminatePlayerNr\').val());"><table><tr>
                    <td><form class="form" style="margin: 0;"><input type="text" size="1" style="width: 20px; text-align:center; margin-top: 6px;" id="terminatePlayerNr" autocomplete="off">
					 </form></td><td style="vertical-align: middle; padding-left: 5px; padding-top: 5px; cursor: pointer;">Terminate player					
                    </td></tr></table></a>
                    </li>
                    <li>
					<a href="controlpanel_functions/exportExcel.php?projectID=' . $projectID . '">Export database
					</a></li>
                  	
					<li>
				    <a href="#" onclick="window.open(\'../basis/controlpanel_functions/map.php\'); return false; ">Map</a>
					</li>';
        if (!$isDemo) $code .= '<li role="separator" class="divider"></li><li>
					<a href="#" onclick="if (confirm(\'This will empty all data generated in this session. Are you sure you want to proceed?\')) emptyDataTables( \' ' . $projectID . '\'); return false;"> Empty data tables </a>
					</li>
                    <li role="separator" class="divider"></li><li>
				    <a href="' . parse_url($_SERVER["REQUEST_URI"], PHP_URL_PATH) . '?logout" >Logout</a>
					</li>';


        $code .= ' </ul></li>  </nav>
                <!-- END TOP NAVIGATION BAR -->
            </div> <div class="page-container row-fluid">
            ';

        return $code;
    }

    public function getTopNavigationLeft($isDemo)
    {
        $decoded = str_replace('e', 'experimenter', PROJECTID);
        $decoded = str_replace('g', '/game', $decoded);
        $decoded = str_replace('_', '/', $decoded);
        if (PATH == '../../../resources/') {
            $path = '../../experiments/' . $decoded;
        } else $path = '../../';
        $code = '
        <ul id="menubar" class="nav navbar-left">
        <li><div class="btn disabled" style="margin-right: 5px; width: 80px;"><img style="width: 20px" src=\'../pagination/pic/heart.png\' id="heart">
        
    <span id="controllerDone" style="width: 20px"></span></div></li>
         <li class="btn" id="gameactive" style="margin-left: 5px" onclick="switchActive(true);">experiment active</li>
        
        <li class="btn" id="testmode" style="margin-left: 5px" onclick="switchTestMode(true);">test mode off</li>
        <span id="testplayer" style="display: none;"><a target="_blank" href="' . $path . '_beginParticipant.php?newsession=1"><li class="btn" title="Start test player" >start testplayer</li></a></span>
        <span id="testplayer_off"><li class="btn disabled" title="Testplayers and bots can only be used if the test mode is switched on." >start testplayer</li></span>
        <span id="testbot" style="display: none;"><a  target="_blank" title="Click + Crtl-Button starts the bot in a new tab." href="' . $path . '_beginParticipant.php?newsession=1&bot=1">
         <li class="btn"  >start bot</li></a></span>
         <span id="testbot_off"><li class="btn disabled" title="Testplayers and bots can only be used if the test mode is switched on.">start bot</li></span>
        
        </ul>';
        $code .= '<ul id="menubar_add" class="nav navbar-left">
        
        </ul>';

        if ($isDemo) $code .= ' <script>switchTestMode(true); switchActive(false);</script>';
        else $code .= ' <script>switchTestMode(false); switchActive(false);</script>';
        return $code;
    }

    public function getNavBar()
    {
        return '<!-- BEGIN SIDEBAR -->
                <div class="page-sidebar nav-collapse collapse">
                    <!-- BEGIN SIDEBAR MENU -->
                    <ul id="navbarfolder"></ul>
                    <ul id="navbar"></ul>
                </div>';
    }

    public function getBodyEnd()
    {
        return '<div class="footer">
                    <a class="nav navbar-nav navbar-brand" href="http://www.wiwi.uni-passau.de/en/chair-in-economic-theory/">
                        <img src="../pagination/pic/unipa.png" width="150px">
                    </a>
                    <a class="nav navbar-nav navbar-brand" href="http://www.nottingham.ac.uk/cedex/">
                        <img src="../pagination/pic/uon.png" width="50px">
                    </a>
                    Lioness Builder Tool Version 1.0 (powered by classEx)
                    
                    <div class="pull-right">
                       <span class="scrollup" style="background: none;">
                            <img src="../pagination/pic/hide.png" style="cursor: pointer" title="scroll to top">
                        </span>
                    </div>
                </div>
            </div>

        	<!-- Load javascripts at bottom, this will reduce page load time-->
            <script src="../pagination/assets/bootstrap/js/bootstrap.min.js"></script>            
     
            
            
            <script>            
                $(document).ready(function () {
                   $(\'.scrollup\').click(function () {
                        $("html, body").animate({
                            scrollTop: 0
                        }, 600);
                        return false;
                    });
                });            
            </script>
           
            
        </body>
    </html>';
    }
}