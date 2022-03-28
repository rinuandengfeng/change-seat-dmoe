#change-seats-script
#禁止任何人使用此项目提供付费的代挂服务，禁止浪费公共资源!
在自己生活，发现的一个需求，写一个图书馆自动抢座位的脚本

##设计思路
1.模拟登录\
2.找到传递预约参数的路由\
3.执行脚本\
4.完成定时请求的命令\


##使用

1.先把代码克隆下来\
```
git clone https://github.com/rinuandengfeng/change-seats-script.git
```
2.安装```requirements.txt ```文件中的包
```
pip install -r requirement.txt
```

3.然后修改```libary-script.py```文件中```login```函数中的logi，改为自己的账户和密码

4.修改```qiangzuowei```函数，中的```seat```,```startTime```,```endTime```.

- seat :座位号
- startTime:开始时间的编号
- endTime:结束时间的编号


5.然后就可以运行~~~~~
 


