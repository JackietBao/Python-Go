package main

import (
	"encoding/json"
	"fmt"
	"gorm.io/driver/mysql"
	"gorm.io/gorm"
)

/*
constraint:OnUpdate:CASCADE 【当User表更新，也会同步给CreditCards】
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
	// 1、预加载: 查找 user 时预加载相关 CreditCards
	//users := User{Username: "zhangsan"} // 只查找张三用户的信用卡信息
	users := []User{}
	db.Preload("CreditCards").Find(&users)
	strUser, _ := json.Marshal(&users)
	fmt.Println(string(strUser))
}
