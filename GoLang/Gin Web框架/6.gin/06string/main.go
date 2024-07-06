package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"net/http"
)

func main() {
	r := gin.Default()
	r.GET("/response/", ResponseStringHandler)
	fmt.Println("http://127.0.0.1:8000/response/")
	r.Run(":8000")
}
func ResponseStringHandler(c *gin.Context) {
	c.String(http.StatusOK, "返回简单字符串")
}
