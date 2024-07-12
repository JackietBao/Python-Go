var computer = ["主机", "显示器", "键盘", "鼠标"];

// 方式1：使用 for...in 循环
for (var i in computer) {
    console.log(computer[i]); // 使用索引获取值
}

// 方式2：使用 forEach 方法
computer.forEach(function (item) {
    console.log(item);
});
