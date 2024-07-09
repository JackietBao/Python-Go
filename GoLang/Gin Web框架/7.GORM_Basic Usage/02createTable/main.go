package main

import (
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
	// 1、连接数据库
	dsn := "root:1@tcp(192.168.184.128:3306)/test_db?charset=utf8mb4&parseTime=True&loc=Local"
	db, _ := gorm.Open(mysql.Open(dsn), &gorm.Config{})
	// 2、自动创建表
	db.AutoMigrate(
		User{},
	)
}
