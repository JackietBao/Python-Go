package middleware

import (
	"bookManage/dao/mysql"
	"bookManage/model"
	"github.com/gin-gonic/gin"
)

func AuthMiddleware() func(c *gin.Context) {
	return func(c *gin.Context) {
		// 客户端携带Token有三种方式 1.放在请求头 2.放在请求体 3.放在URI
		// token验证成功，返回c.Next继续，否则返回c.Abort()直接返回
		token := c.Request.Header.Get("token")
		var u model.User
		// 如果没有当前用户
		if rows := mysql.DB.Where("token = ?", token).First(&u).RowsAffected; rows !=
			1 {
			c.JSON(403, gin.H{"msg": "当前token错误"})
			c.Abort()
			return
		}
		// 将当前请求的userID信息保存到请求的上下文c上
		c.Set("UserId", u.Id)
		c.Next()
	}
}
