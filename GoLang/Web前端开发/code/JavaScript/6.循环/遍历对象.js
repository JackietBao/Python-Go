var user = {name: "阿良", sex: "男", age: "30"};

// 方式1：使用 for...in 循环
for (var key in user) {
    if (user.hasOwnProperty(key)) { // 确保不是原型链上的属性
        console.log(key + ": " + user[key]);
    }
}

// 方式2：使用 Object.keys() 和 forEach 方法
Object.keys(user).forEach(function (key) {
    console.log(key + ": " + user[key]);
});
