package main

import (
	"gorm.io/driver/mysql"
	"gorm.io/gorm"
)

/*
constraint:OnUpdate:CASCADE 【当User表更新，也会同步给CreditCards】 // 外键约束
OnDelete:SET NULL 【当User中数据被删除时，CreditCard关联设置为 NULL，不删除记录】
*/
type User struct {
	gorm.Model
	Username    string       `json:"username" gorm:"column:username"`
	CreditCards []CreditCard `gorm:"constraint:OnUpdate:CASCADE,OnDelete:SET
NULL;"`
}
type CreditCard struct {
	gorm.Model
	Number string
	UserID uint
}

func main() {
	// 0、连接数据库
	dsn := "root:1@tcp(192.168.184.128:3306)/test_db?charset=utf8mb4&parseTime=True&loc=Local"
	db, _ := gorm.Open(mysql.Open(dsn), &gorm.Config{})
	// 创建表结构
	db.AutoMigrate(User{}, CreditCard{})
	// 1、创建一对多
	user := User{
		Username: "zhangsan",
		CreditCards: []CreditCard{
			{Number: "0001"},
			{Number: "0002"},
		},
	}
	db.Create(&user)
	// 2、为已存在用户添加信用卡
	u := User{Username: "zhangsan"}
	db.First(&u)
	//fmt.Println(u.Username)
	db.Model(&u).Association("CreditCards").Append([]CreditCard{
		{Number: "0003"},
	})
}
