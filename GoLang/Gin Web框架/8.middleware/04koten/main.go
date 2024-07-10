package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
)

func AuthMiddleware() func(c *gin.Context) {
	return func(c *gin.Context) {
		// 客户端携带Token有三种方式 1.放在请求头 2.放在请求体 3.放在URI
		// token验证成功，返回c.Next继续，否则返回c.Abort()直接返回
		token := c.Request.Header.Get("token")
		fmt.Println("获取token：", token) // 获取token： xxxxxx
		if token == "" {
			c.String(200, "身份验证不通过")
			c.Abort()
			return
		}
		c.Next()
	}
}
func main() {
	r := gin.Default()
	// 首页无需验证
	r.GET("/index", func(c *gin.Context) {
		c.JSON(200, gin.H{"msg": "index 页面"})
	})
	// home页需要用户登录才能查看
	r.GET("/home", AuthMiddleware(), func(c *gin.Context) {
		c.JSON(200, gin.H{"msg": "home 页面"})
	})
	r.Run()
}
