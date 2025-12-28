<?php

/**
 * Created by PhpStorm.
 * User: GIAMAT01
 * Date: 26.09.2014
 * Time: 14:16
 */


class liondb_leg extends liondb
{
    static $_instance;
    public $statements;
    private $_db;

    private function __construct()
    {

        /*
         * REQUIRES CREDENTIALS TO BE INCLUDED BEFOREHAND
         */
        try {
            $this->_db = new PDO(DNS_LEGACY, ADMIN, PASSW);
            $this->_db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            $this->_db->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);
            $this->_db->exec('SET NAMES UTF8');

        } catch (PDOException $e) {
            error_log("dbloggin failed");
        }
    }


}