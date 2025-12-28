<?php

/**
 * Created by PhpStorm.
 * User: GIAMAT01
 * Date: 26.09.2014
 * Time: 14:16
 */


class liondb
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

    public static function getInstance()
    {
        if (!(self::$_instance instanceof self)) {
            self::$_instance = new self();
        }

        return self::$_instance;
    }

    public function __call($method, $args)
    {
        if (is_callable([$this->_db, $method])) {
            return call_user_func_array([$this->_db, $method], $args);
        } else {
            throw new BadMethodCallException('Undefined method Database::' . $method);
        }
    }

    public function prepareAndFetch($statement, $executeArgs, $fetchAll = false)
    {
        $stmt = $this->prepare($statement);
        $stmt->execute($executeArgs);
        if ($fetchAll) return $stmt->fetchAll(PDO::FETCH_ASSOC);
        else return $stmt->fetch(PDO::FETCH_ASSOC);
    }

    public function prepareAndCount($statement, $executeArgs)
    {
        $stmt = $this->prepare($statement);
        $stmt->execute($executeArgs);
        return $stmt->rowCount();

    }

    public function prepare($statement)
    {
        return $this->_db->prepare($statement);
    }

    public function prepareAndExecute($statement, array $executeArgs)
    {
        $stmt = $this->prepare($statement);
        $stmt->execute($executeArgs);
        return $stmt;
    }

    public function lastInsertID()
    {
        return $this->_db->lastInsertId();
    }

    public function fetchArray($query)
    {
        $result = $this->_db->query($query);
        $resultarray = [];
        while ($row = $result->fetch(PDO::FETCH_NUM)) {
            for ($i = 1; $i < count($row); $i++) {
                $resultarray[$row[0]] = $row[$i];
            }
        }

        return $resultarray;
    }

    /**
     * @param $statement
     * @return bool|PDOStatement
     * @throws PDOException
     */
    public function query($statement)
    {
        try {
            $this->statements .= $statement . "<br>";
            return $this->_db->query($statement);
        } catch (PDOException $e) {
            error_log($e);
            throw new PDOException("MySQL error: " . $statement);
        }
    }

    public function beginTransaction()
    {
        $this->_db->beginTransaction();
    }

    public function commit()
    {
        $this->_db->commit();
    }

    public function rollBack()
    {
        $this->_db->rollBack();
    }

    public function exec($statement)
    {
        $this->statements .= $statement . " => ";


        $result = $this->_db->exec($statement);


        if ($result === FALSE) {
            $this->statements .= "FAILED:" . $statement . "<br>";

            $error = $this->_db->errorInfo();

            $this->statements .= "<span style=\"color:red;\">PROBLEM:" . $error[2] . "</span><br>";

            return 0;
        } else {
            $this->statements .= "affected rows:" . $result . "<br>";


            return $result;
        }
    }

    public function standardInsert($table, $data)
    {
        $var = "";

        $dat = "";

        $i = 1;

        $num = count($data);

        foreach ($data as $key => $value) {
            $dat .= "'" . htmlspecialchars($value, ENT_QUOTES) . "'";

            $var .= "" . htmlspecialchars($key, ENT_QUOTES) . "";;

            if ($i != $num) {
                $var .= ", ";

                $dat .= ", ";
            }

            $i++;
        }


        $insert = "INSERT INTO  $table  ( $var ) VALUES(  $dat )";

        $this->_db->exec($insert);

        $id = $this->_db->lastInsertId();

        //echo $insert;

        return $id;
    }

    public function standardDelete($table, $data, $really = 0)
    {
        $dat = "";

        $i = 1;

        $num = count($data);

        $correct = 1;

        foreach ($data as $key => $value) {
            if ($value == null & $correct == 1) {
                $correct = 0;
            }

            $dat .= "" . htmlspecialchars($key, ENT_QUOTES) . "=" . htmlspecialchars($value, ENT_QUOTES) . "";

            if ($i != $num) {
                $dat .= " AND ";
            }

            $i++;
        }


        $delete = "DELETE FROM $table  WHERE $dat";


        if ($really & $correct) {
            echo $delete;

            $stmt = $this->_db->prepare($delete);

            $stmt->execute();

            $id = $stmt->rowCount();
        } else $id = 0;


        return $id;
    }

    public function standardUpdate($sqlstring)

    {
        $affectedrows = $this->_db->exec($sqlstring);


        return $affectedrows;
    }

    public function insertOrUpdate($tableName, int $idRun, array $keyCol, string $valueCol, array $valuePairs)
    {

        $valuesForInsert = [];
        $valuesForUpdate = [];

        foreach ($valuePairs as $key => $value) {
            array_push($valuesForInsert, "(" . $idRun . ",'" . $key . "','" . ($value) . "')");
            array_push($valuesForUpdate, $valueCol . "= '" . ($value) . "'");
        }

        $insert = "INSERT INTO " . $tableName . " (idRun, " . implode(',', $keyCol) . "," . $valueCol . ") 
                    VALUES " . implode(",", $valuesForInsert) . "  ON DUPLICATE KEY UPDATE " . implode(",", $valuesForUpdate);
        //echo $insert;
        $this->_db->exec($insert);


    }

}