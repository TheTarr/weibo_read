weibo_read

使用方法：有python3环境的win朋友们直接双击0.bat运行。uid就是微博你主页网址后边一串数，输完回车。程序将开始爬取你的所有微博。需要等待较长时间，2分钟左右。之后开始生成。

第一次爬过、不许要更新数据后，下次使用可以直接双击1.bat。

以下是老哥原来的readme
====

新浪微博简易爬虫，读取特定用户原创微博

目前github上排名靠前的几个爬虫都是爬取页面的，有个局限是需要授权，不然会跳到登录页面，非常不友好。

F12后发现微博的ajax接口是没有什么限制的，而且直接返回json，不用处理页面。

## 要求

+ python3
+ requests

```shell
pip install requests
```

或者用`pipenv`

```shell
pip install pipenv
pipenv install
pipenv shell
```

## 运行

```shell
python weibo_read.py <uid>
```

比如打印[深圳天气](https://weibo.com/szmb)的微博

```shell
python weibo_read.py 1871802012
```

## 备注

如果一定要用python2来执行，可以在前面添加：

```shell
reload(sys)
sys.setdefaultencoding('utf-8')
```
