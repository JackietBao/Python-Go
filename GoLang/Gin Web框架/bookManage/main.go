package main

import (
	"bookManage/dao/mysql"
	"bookManage/router"
)

func main() {
	// 初始化mysql连接
	mysql.InitMysql()
	// 初始化路由分层
	r := router.InitRouter()
	r.Run(":8888")
}
