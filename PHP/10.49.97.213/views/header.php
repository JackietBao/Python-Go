<!DOCTYPE html>
<html>
<head>
    <title>博客论坛</title>
    <link rel="stylesheet" href="/public/css/style.css">
</head>
<body>
    <nav>
        <ul>
            <li><a href="/">首页</a></li>
            <li><a href="/posts">文章</a></li>
            <?php if(isset($_SESSION['user_id'])): ?>
                <li><a href="/profile">个人中心</a></li>
                <li><a href="/logout">退出</a></li>
            <?php else: ?>
                <li><a href="/login">登录</a></li>
                <li><a href="/register">注册</a></li>
            <?php endif; ?>
        </ul>
    </nav>
</body>
</html> 