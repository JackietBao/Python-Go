<?php
session_start();
require_once 'config/database.php';
require_once 'includes/db.php';
require_once 'includes/functions.php';

include 'views/header.php';

$posts = get_posts();
?>

<div class="container">
    <h1>最新文章</h1>
    
    <?php foreach($posts as $post): ?>
        <div class="post">
            <h2><?php echo htmlspecialchars($post['title']); ?></h2>
            <p class="meta">
                作者: <?php echo htmlspecialchars($post['username']); ?> | 
                发布时间: <?php echo $post['created_at']; ?>
            </p>
            <div class="content">
                <?php echo nl2br(htmlspecialchars($post['content'])); ?>
            </div>
        </div>
    <?php endforeach; ?>
</div>

<?php include 'views/footer.php'; ?>