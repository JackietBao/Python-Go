package main

import (
	"fmt"
	"os"
)

func main() {
	// 1、获取目录
	fmt.Println(os.Getwd())
	// 2、cd 切换路径
	os.Chdir("D:\\Github\\")
	fmt.Println(os.Getwd())
	// 3、创建文件夹
	os.Mkdir("test_dir", 0777)
	// 4、删除文件夹
	os.Remove("test_dir")
	//// 5、重命名文件
	//os.Rename("test_dir", "xxx")
	//// 6、新建文件夹
	//os.Create("./file.txt")
	file, err := os.OpenFile("file.txt", os.O_WRONLY, 0666)
	if err != nil {
		fmt.Println(err)
	}
	_, err = file.WriteString("hello world")
	if err != nil {
		fmt.Println(err)
	}
}
