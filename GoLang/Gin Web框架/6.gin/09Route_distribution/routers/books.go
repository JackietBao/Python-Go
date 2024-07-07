package routers

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

func LoadBooks(e *gin.Engine) {
	e.GET("/book", GetBookHandler)
}
func GetBookHandler(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H{
		"message": "Book Router",
	})
}
