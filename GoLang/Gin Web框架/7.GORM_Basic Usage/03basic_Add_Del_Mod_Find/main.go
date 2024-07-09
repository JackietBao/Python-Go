package main

import (
	"fmt"
	"gorm.io/driver/mysql"
	"gorm.io/gorm"
)

// User 表的结构体ORM映射
type User struct {
	Id       int64 `gorm:"primary_key" json:"id"`
	Username string
	Password string
}

func main() {
	// 0、连接数据库
	dsn := "root:1@tcp(192.168.184.128:3306)/test_db?charset=utf8mb4&parseTime=True&loc=Local"
	db, _ := gorm.Open(mysql.Open(dsn), &gorm.Config{})
	db.AutoMigrate(User{})
	// 1、增
	db.Create(&User{
		//Id: 3,
		Username: "zhangsan",
		Password: "123456",
	})
	// 2、改
	db.Model(User{
		Id: 3,
	}).Update("username", "lisi")
	// 3、查
	// 3.1 过滤查询
	u := User{Id: 3}
	db.First(&u)
	fmt.Println(u)
	// 3.2 查询所有数据
	users := []User{}
	db.Find(&users)
	fmt.Println(users)
	// 4、删
	// 4.1 删除 id = 3 的用户
	db.Delete(&User{Id: 3})
	// 4.2 条件删除
	db.Where("username = ?", "zhangsan").Delete(&User{})
}
