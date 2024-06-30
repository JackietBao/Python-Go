package main

import "fmt"

func main() {
	//创建一个名为 m 的映射（map），映射中包含一个键值对："username" 键对应的值是 "zhangsan"。
	//换句话说，这个映射用来存储用户名，其中键是 "username"，值是 "zhangsan"。
	m := map[string]string{
		"username": "zhangsan",
	}
	// 1、占位符
	fmt.Printf("%T %v \n", m, m)
	fmt.Printf("%T %+v \n", m, m)
	//在 %v 的基础上，对结构体字段名和值进行展开
	fmt.Printf("%T %#v \n", m, m)
	//输出 Go 语言语法格式的值
	// Println: 自动换行
	fmt.Println("Println, 自动换行")
	fmt.Println("Println, 自动换行")
	// Print
	fmt.Print("Print, 换行")
	fmt.Print("Print, 换行")
	name := "zhangsan"
	age := 24
	// Printf : 格式化打印输出
	fmt.Printf("\n 姓名：%s age: %d \n", name, age)
	// Sprint(最常用的) ：字符串格式化
	s := fmt.Sprintf("姓名：%s age: %d", name, age)
	fmt.Println(s)
}
