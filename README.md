# flask-Jianzhi
> flask作为后台实现的一个兼职管理平台,包含手机端，现实现WAB版，以及web后台管理，后续可以实现WEB版

### 实现的功能有

#### WAP版(自适应)：

> 1.home页:首页兼职信息展示，公告信息展示
>
> 2.posts页:发帖界面展示，使用redis作为发帖定时缓存
>
> 3.me页:展示个人相关兼职展示，资料修改，注销账号等

#### Web后台

> 实现一个业务模块(兼职模块),可根据业务需求添加模块
>
> 兼职模块包含：
>
> ​			兼职管理
>
> ​			求职管理
>
> ​			商家管理
>
> ​			通知管理
>
> ​			账号管理
>
> ​			统计模块(暂未完成)
>
> ​			系统管理(部分完成)

##### 未完成功能后续开发



### 效果图

![](G:\2019以前的project\gitsc\flask-Jianzhi\img\webhome.png)

![jianzhihome](G:\2019以前的project\gitsc\flask-Jianzhi\img\jianzhihome.png)

![jianzhihome2](G:\2019以前的project\gitsc\flask-Jianzhi\img\jianzhihome2.png)

![pingtai](G:\2019以前的project\gitsc\flask-Jianzhi\img\pingtai.png)

![wapindex](G:\2019以前的project\gitsc\flask-Jianzhi\img\wapindex.png)![wapme](G:\2019以前的project\gitsc\flask-Jianzhi\img\wapme.png)



![](G:\2019以前的project\gitsc\flask-Jianzhi\img\wappost.png)









### 技术栈

- flask
- flask相关模块
- mysql
- redis

### 运行项目

```
#clone项目到本地
https://github.com/agamgn/flask-Jianzhi.git
#安装依赖
pip install -r requirement.txt
#运行sql
#启动项目
python manage.py runserver
#默认超级管理员
root:root
```

