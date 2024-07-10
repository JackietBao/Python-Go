package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
)

func MiddleWare() gin.HandlerFunc {
	return func(c *gin.Context) {
		fmt.Println("这里可以做一些身份验证等")
	}
}
func main() {
	r := gin.Default()
	// 首页无需验证
	r.GET("/index", func(c *gin.Context) {
		c.JSON(200, gin.H{"msg": "index 页面"})
	})
	// home页需要用户登录才能查看
	r.GET("/home", MiddleWare(), func(c *gin.Context) {
		c.JSON(200, gin.H{"msg": "home 页面"})
	})
	r.Run()
}
