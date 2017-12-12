# python-getpicture
基于python3.6获取食物贴吧的全部图片
## 准备条件(安装re和requests库)
```python
pip install re  #使用cmd进入本地安装的python目录下的Scripts执行该语句，安装re正则库
```
```python
pip install requests #使用cmd进入本地安装的python目录下的Scripts执行该语句，安装requests库
```
## 使用知识点
    函数定义
    requests请求
    findall正则
    文件处理
## 资源请求地址
```php
https://tieba.baidu.com/f?kw=%E9%A3%9F%E7%89%A9&ie=utf-8&pn=0
```
### 第一步、分析网页图片的结构
    使用chrome浏览器打开上面的资源链接网页，使用查看元素功能分析。发现每张图片都有class="thumbnail vpic_wrap"这个属性
    进而可以是使用正则表达式根据这个属性来匹配
### 第二步、分析分页结构
  * 通过点击不同页面观察url可以得到，一共有54页，最基本的url为https://tieba.baidu.com/f?kw=%E9%A3%9F%E7%89%A9&ie=utf-8&pn=
  * 然后改变页数的是pn=?，这个值从0到2650，这个可以用range来改变
### 第三步、获取网页内容
    使用requests的get方法获取内容全部信息
    ![这是爬取成功后的部分截图](https://github.com/legendheng/python-getpicture/blob/master/demo.png)
