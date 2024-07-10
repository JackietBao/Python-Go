package controller

import (
	"bookManage/dao/mysql"
	"bookManage/model"
	"github.com/gin-gonic/gin"
	"strconv"
)

// 增
func CreateBookHandler(c *gin.Context) {
	p := new(model.Book)
	if err := c.ShouldBindJSON(p); err != nil {
		c.JSON(400, gin.H{"err": err.Error()})
		return
	}
	mysql.DB.Create(p)
	c.JSON(200, gin.H{"msg": "success"})
}

// 查看书籍列表
func GetBookListHandler(c *gin.Context) {
	books := []model.Book{}
	mysql.DB.Preload("Users").Find(&books)
	//mysql.DB.Find(&books) // 只查书籍，不查关联User
	c.JSON(200, gin.H{"books": books})
}

// 查看指定书籍
func GetBookDetailHandler(c *gin.Context) {
	pipelineIdStr := c.Param("id") // 获取URL参数
	bookId, _ := strconv.ParseInt(pipelineIdStr, 10, 64)
	book := model.Book{Id: bookId}
	//mysql.DB.Preload("Users").Find(&book)
	mysql.DB.Find(&book) // 只查书籍，不查关联User
	c.JSON(200, gin.H{"books": book})
}

// 改
func UpdateBookHandler(c *gin.Context) {
	p := new(model.Book)
	if err := c.ShouldBindJSON(p); err != nil {
		c.JSON(400, gin.H{"err": err.Error()})
		return
	}
	oldBook := &model.Book{Id: p.Id}
	var newBook model.Book
	if p.Name != "" {
		newBook.Name = p.Name
	}
	if p.Desc != "" {
		newBook.Desc = p.Desc
	}
	mysql.DB.Model(&oldBook).Updates(newBook)
	c.JSON(200, gin.H{"book": newBook})
}

// 删除
func DeleteBookHandler(c *gin.Context) {
	pipelineIdStr := c.Param("id") // 获取URL参数
	bookId, _ := strconv.ParseInt(pipelineIdStr, 10, 64)
	// 删除book时，也删除第三张表中的 用户对应关系记录
	mysql.DB.Select("Users").Delete(&model.Book{Id: bookId})
	c.JSON(200, gin.H{"msg": "success"})
}
