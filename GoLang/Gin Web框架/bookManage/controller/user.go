package controller

import (
	"bookManage/dao/mysql"
	"bookManage/model"
	"github.com/gin-gonic/gin"
	"github.com/google/uuid"
)

// 注册
func RegisterHandler(c *gin.Context) {
	p := new(model.User)
	if err := c.ShouldBindJSON(p); err != nil {
		c.JSON(400, gin.H{"err": err.Error()})
		return
	}
	// 密码进行加密：这里自己实现
	mysql.DB.Create(p)
	c.JSON(200, gin.H{"msg": p})
}

// 登录
func LoginHandler(c *gin.Context) {
	p := new(model.User)
	if err := c.ShouldBindJSON(p); err != nil {
		c.JSON(400, gin.H{"err": err.Error()})
		return
	}
	u := model.User{Username: p.Username, Password: p.Password}
	if rows := mysql.DB.Where(&u).First(&u).Row(); rows == nil {
		c.JSON(403, gin.H{"msg": "用户名密码错误"})
		return
	}
	token := uuid.New().String()
	mysql.DB.Model(u).Update("token", token)
	c.JSON(200, gin.H{"token": token})
}
