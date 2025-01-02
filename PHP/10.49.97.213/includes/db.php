<?php
require_once 'config/database.php';
class Database {
    private $conn;
    
    public function __construct() {
        try {
            $this->conn = new PDO(
                "mysql:host=" . DB_HOST . ";dbname=" . DB_NAME,
                DB_USER,
                DB_PASS
            );
            $this->conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        } catch(PDOException $e) {
            echo "连接失败: " . $e->getMessage();
        }
    }
    
    public function query($sql, $params = []) {
        try {
            $stmt = $this->conn->prepare($sql);
            $stmt->execute($params);
            return $stmt;
        } catch(PDOException $e) {
            // 记录错误信息并返回false
            error_log("数据库查询错误: " . $e->getMessage());
            error_log("SQL: " . $sql);
            error_log("参数: " . print_r($params, true));
            return false;
        }
    }
}