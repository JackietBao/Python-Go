package main

import (
	"fmt"
	"time"
)

func main() {
	// 1、时间对象
	now := time.Now()
	fmt.Printf("%T %v \n", now, now)
	// 2、格式化时间：给人看的时间（2022-03-27 09:15:29）
	// "2006-01-02 15:04:05" golang中固定的时间标记，是确定的不能改
	strTime := now.Format("2006-01-02 15:04:05")
	fmt.Printf("%T %v \n", strTime, strTime)

	// 3、时间戳：秒的整数形式
	ts := now.Unix()
	fmt.Printf("%T %v \n", ts, ts)
	// 4、格式化时间转换成时间对象
	// 设置转换的时区
	loc, _ := time.LoadLocation("Asia/Shanghai")
	// 转换成对应时区的时间对象
	timeObj, _ := time.ParseInLocation("2006-01-02 15:04:05", strTime, loc)
	fmt.Printf("%T %v \n", timeObj, timeObj)
	fmt.Println(timeObj.Unix()) // 时间搓

	time.Sleep(time.Second * 2)
	fmt.Println("over")
}
