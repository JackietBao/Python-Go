<?php
function register_user($username, $password, $email) {
    $db = new Database();
    $hashed_password = password_hash($password, PASSWORD_DEFAULT);
    
    $sql = "INSERT INTO users (username, password, email) VALUES (?, ?, ?)";
    return $db->query($sql, [$username, $hashed_password, $email]);
}

function create_post($title, $content, $user_id) {
    $db = new Database();
    $sql = "INSERT INTO posts (title, content, user_id) VALUES (?, ?, ?)";
    return $db->query($sql, [$title, $content, $user_id]);
}

function get_posts($limit = 10) {
    $db = new Database();
    $sql = "SELECT p.*, u.username 
            FROM posts p 
            JOIN users u ON p.user_id = u.id 
            ORDER BY p.created_at DESC 
            LIMIT ?";
    $result = $db->query($sql, [$limit]);
    
    if ($result === false) {
        error_log("Database query failed in get_posts()");
        return [];
    }
    
    return $result->fetchAll(PDO::FETCH_ASSOC);
}