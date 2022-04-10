# change-seats-script

# 禁止任何人使用此项目提供付费的代挂服务，禁止浪费公共资源!
- 在自己生活，发现的一个需求，写一个图书馆自动抢座位的脚本

## 开发灵感
自己在去图书馆的时间每次都需要进行预约，而且有时候预约不到座位，然后自己就想着写一个抢座位的脚本，来帮助自己去抢座位。

## 使用的工具
- 抓包工具:Fiddler
- 开发工具:pycharm


## 设计思路
1.模拟登录，拿到登录的Token。  
2.找到传递预约参数的路由，伪造请求表单。 
3.定时执行，并push到github，可以看到执行的结果。 
4.使用docker部署到服务器上。  


## 使用说明：

1.先把代码克隆下来  
```
git clone https://github.com/rinuandengfeng/change-seats-script.git
```  
2.安装```requirements.txt ```文件中的包
```
pip install -r requirements.txt
```

3.然后找到```libary-script.py```文件中```login```函数中的logi变量
```logi = "https://leosys.cn/hnuahe/rest/auth?username=username&password=password"```  
将变量中```username```改为自己的学号```password```改为自己学号对应的密码。

4.找到```libary-script.py```文件中```qiangzuowei```函数，修改```Form_data```变量中的值.  
```
Form_data = {
        "seat": "46001",
        "date": str(today),
        "startTime": "1080",
        "endTime": "1260",
        "authid": authid,
    }
```

- seat:座位号。需要进行抓包，来找到自己想要的位置。(目前没有找到座位号的规律。)  

- date:为今天的时间，也可以是明天。(这个主要看你预约什么时间的座位。如果预约当天的就填入当天的时间，要是预约明天的就填入明天的时间。)  

- startTime:开始时间的编号。(位置的初始时间编号。这个时间也是需要进行抓包进行处理。目前没有找到相应的规律。)  
- endTime:结束时间的编号。(位置结束的时间编号，这个和开始的时间一样需要进行抓包查看。)  

* 注：```startTime```和```endTime```两个时间编号每天都是固定的，你只需要找到自己想预约的时间的开始的时间编号和结束的时间编号就可以。  


5.将Dockerfile文件放到该文件的上一级。  
 - 拉取镜像文件。  
 ```docker build -t test:1 . ```
 - 运行docker容器。
 ``` docker run -itd -v /etc/localtime:/etc/localtime:ro test:1 ```
 *注*：-v /etc/localtime:/etc/localtime:ro 是使容器的时间和宿主时间一致。一定要加。
  

## 总结：  
这只是一个简单的dome，后续有时间在进行改进。还有很多的地方可以改进。有什么问题欢迎跟我讨论。
 


