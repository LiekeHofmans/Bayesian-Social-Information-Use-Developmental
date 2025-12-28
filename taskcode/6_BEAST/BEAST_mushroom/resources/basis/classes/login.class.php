<?php


class LoginLioness
{


    public static $redirect = 'index.php';
    private static $iv = "o+3'%kUcSm_!GxTa";
    private static $key = 'fTjWmZq4t7w!z%C*';

    public static function checkValidity($pw)


    {


        $accesstoken = self::decodeAutomaticLogin($_GET['a']);



        if ($accesstoken[0] == 'xXgf65x?' && $accesstoken[1] . '_' == PROJECTID) {
            $_SESSION['LionLogged'] = 1;
            return true;
        }

        if ($pw == -1) return true;

        if (($_SESSION['LionLogged'] < 1 | !isset($_SESSION['LionLogged']))) {


            if (md5($_POST['kennwort']) == $pw) {
                $_SESSION['LionLogged'] = 1;
                return true;

            } else return false;

        } else return true;


    }

    public static function encodeAutomaticLogin($pw, $projectid, $experiment = 0, $logrole = 0, $adminin = 0)
    {
        // refer to decodeAutomaticLogin()

        $code = $pw . "_" . $projectid;

        $code = openssl_encrypt($code, "AES-128-CBC", LoginLioness::$key, $options = OPENSSL_RAW_DATA, LoginLioness::$iv);

        $code = base64_encode($code);

        // make code url safe ('+' and '/' are not in get request values)
        $code = str_replace('+', '-', $code);
        $code = str_replace('/', '_', $code);

        return $code;
    }

    public static function decodeAutomaticLogin($code)
    {
        // refer to encodeAutomaticLogin()
        $code = str_replace('-', '+', $code);
        $code = str_replace('_', '/', $code);

        $login = base64_decode($code . "==");

        $login = openssl_decrypt($login, "AES-128-CBC", LoginLioness::$key, $options = OPENSSL_RAW_DATA, LoginLioness::$iv);


        return explode('_', $login);
    }

    public static function displayLoginField()
    {


        session_destroy();


        LoginLioness::displayLoginHeader();


        echo '<div class="alert alert-info" style="text-align: center; margin-top: 30px;"><form id="login" method="POST">';

        echo 'You are logged out of the control panel. Please log in again. The password is the same as for your LIONESS Lab account.';

        echo '</div>';


        echo '<div class="btnbox2">
                <input class="form-control"
                    style="text-align: center; width: 100%" name="kennwort" type="password"
                    maxlength="20" value="' . $_GET['kennwort'] . '"
                    placeholder="Please insert your password here.">
                </div>';

        echo '<div>
                <input type="hidden" name="choice" value="1" />
                <input type="submit" class="btn btn-block btn-default btn-info btn-lg" value="Login" onclick="document.forms[\'login\'].submit();">
                </form></div>';

        if (isset($_POST['kennwort']) & !isset($_GET['kennwort'])) {
            echo '<div  class="alert alert-danger" style="text-align: center;">Wrong password</div>';
        }

        echo '<div style="margin-bottom: 50px"></div>';
        LoginLioness::displayLoginFooter();


    }


    public static function displayLoginHeader()
    {


        $site = 'http://lioness.classEx.de';
        $text = '<a target="_blank" href="' . $site . '" style="font-size: x-small;">LIONESS Lab</a> is powered by 
                        classEx
                    <a target="_blank" href="http://classex.de" style="font-size: x-small;"><img class="logo" src="pic/logo.svg" border=0 style="width: 25px; padding-left: 5px; padding-right: 5px;"></a>
                     </a>';

        echo '<div class="left">
                        
                        <img class="logo" src="../pagination/pic/lionlogo.svg" border=0 
                            style="width: 100px; padding-left: 5px; padding-right: 5px;">
                        </a>  
                      </div>';


        echo '</div>';
    }


    public static function displayLoginFooter()
    {


    }


    public static function logout($getparam = null, $address = null)
    {

        if ($address == null) $address = self::$redirect;
        $_SESSION['LionLogged'] = 0;
        //session_destroy();
        if ($getparam != null) header('Location: ' . $address . $getparam);
        else header('Location: ' . $address);


    }


}


