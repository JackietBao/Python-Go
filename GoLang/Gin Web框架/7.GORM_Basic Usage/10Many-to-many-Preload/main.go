package main

import (
	"encoding/json"
	"fmt"
	"gorm.io/driver/mysql"
	"gorm.io/gorm"
	"time"
)

type Person struct {
	ID        int
	Name      string
	Addresses []Address `gorm:"many2many:person_addresses;"`
}
type Address struct {
	ID   uint
	Name string
}
type PersonAddress struct {
	PersonID  int `gorm:"primaryKey"`
	AddressID int `gorm:"primaryKey"`
	CreatedAt time.Time
	DeletedAt gorm.DeletedAt
}

func main() {
	// 0、连接数据库
	dsn := "root:1@tcp(192.168.184.128:3306)/test_db?charset=utf8mb4&parseTime=True&loc=Local"
	db, _ := gorm.Open(mysql.Open(dsn), &gorm.Config{})
	// 1、获取 name="zhangsan" 用户的地址
	persons := []Person{}
	db.Preload("Addresses").Find(&persons)
	strPersons, _ := json.Marshal(&persons)
	fmt.Println(string(strPersons))
	// [{"ID":1,"Name":"zhangsan","Addresses":[{"ID":1,"Name":"bj"}, {"ID":2,"Name":"sh"}]}]
	// 2、获取 name="zhangsan" 用户的地址
	person := Person{Name: "zhangsan"}
	db.Preload("Addresses").Find(&person)
	strPerson, _ := json.Marshal(&person)
	fmt.Println(string(strPerson))
	// {"ID":1,"Name":"zhangsan","Addresses":[{"ID":1,"Name":"bj"}, {"ID":2,"Name":"sh"}]}
}
