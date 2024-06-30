package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"net/url"
)

func main() {
	apiUrl := "http://baidu.com"
	data := url.Values{}         //创建一个URL参数对象
	data.Set("name", "zhangsan") //设置一个名为name的参数，其值为zhangsan。

	u, _ := url.ParseRequestURI(apiUrl) //解析基本URL。
	u.RawQuery = data.Encode()          //将参数编码为查询字符串并附加到URL上。
	fmt.Println(u.String())             //打印完整的URL：

	resp, err := http.Get(u.String()) //http.Get(u.String())：发送GET请求。
	if err != nil {
		fmt.Println(err)
	}
	body, _ := ioutil.ReadAll(resp.Body) //读取响应主体的内容。
	fmt.Println(string(body))            //将响应内容转换为字符串并打印出来。
}
