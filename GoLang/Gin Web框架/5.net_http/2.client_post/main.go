package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"strings"
)

func main() {
	url := "http://baidu.com"
	contentType := "application/json"
	data := `{
		"name": "root",
		"password": "123456"
	}`
	resp, _ := http.Post(url, contentType, strings.NewReader(data))
	b, _ := ioutil.ReadAll(resp.Body)
	fmt.Println(string(b))
}
