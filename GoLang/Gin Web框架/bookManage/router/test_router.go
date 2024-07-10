package router

import (
	"github.com/gin-gonic/gin"
)

func TestRouters(r *gin.Engine) {
	v1 := r.Group("/api/v1")
	v1.GET("test", TestHandler)
}

// 测试路由访问： http://127.0.0.1:8888/api/v1/test
func TestHandler(c *gin.Context) {
	c.String(200, "ok")
}
