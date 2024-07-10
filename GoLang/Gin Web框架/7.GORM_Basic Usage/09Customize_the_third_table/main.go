package main

import (
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

// func (PersonAddress) BeforeCreate(db *gorm.DB) (err error) {
// // 修改 Person 的 Addresses 字段的连接表为 PersonAddress
// // PersonAddress 必须定义好所需的外键，否则会报错
// err = db.SetupJoinTable(&Person{}, "Addresses", &PersonAddress{})
// if err != nil {
// fmt.Println("err", err)
// }
// return nil
// }
func main() {
	// 0、连接数据库
	dsn := "root:1@tcp(192.168.184.128:3306)/test_db?charset=utf8mb4&parseTime=True&loc=Local"
	db, _ := gorm.Open(mysql.Open(dsn), &gorm.Config{})
	// 1、自动创建多对多表结构
	db.AutoMigrate(
		Person{},
		Address{},
	)
	// 2、添加数据
	persons := Person{
		ID:   1,
		Name: "zhangsan",
		Addresses: []Address{
			{ID: 1, Name: "bj"},
			{ID: 2, Name: "sh"},
		},
	}
	db.Create(&persons)
}
