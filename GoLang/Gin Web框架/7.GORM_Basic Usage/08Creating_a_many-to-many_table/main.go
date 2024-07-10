package main

import (
	"gorm.io/driver/mysql"
	"gorm.io/gorm"
)

// User 拥有并属于多种 language，`user_languages` 是连接表
type User struct {
	gorm.Model
	Languages []Language `gorm:"many2many:user_languages;"`
}
type Language struct {
	gorm.Model
	Name string
}

func main() {
	// 0、连接数据库
	dsn := "root:1@tcp(192.168.184.128:3306)/test_db?charset=utf8mb4&parseTime=True&loc=Local"
	db, _ := gorm.Open(mysql.Open(dsn), &gorm.Config{})
	// 1、自动创建多对多表结构
	db.AutoMigrate(
		User{},
		Language{},
	)
}
