package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
)

func MiddleWare() gin.HandlerFunc {
	return func(c *gin.Context) {
		fmt.Println("我是一个全局中间件")
	}
}
func main() {
	r := gin.Default()
	r.Use(MiddleWare())
	r.GET("/hello", func(c *gin.Context) {
		fmt.Println("执行了Get方法")
		c.JSON(200, gin.H{"msg": "success"})
	})
	r.Run()
}
