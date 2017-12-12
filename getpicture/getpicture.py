import re
import requests

def getcontent(url):
    content=requests.get(url).content.decode('utf-8')       #根据网页链接请求全部内容信息
    savepicture(content)

def savepicture(content):
    pic_url=re.findall('class="thumbnail vpic_wrap"><img src="" attr="(.*?)" data-original="(.*?)"  bpic="',content,re.S)   #使用正则匹配找出图片的链接地址
    x=1
    for i in pic_url:
        print("正在下载图片"+str(i[1]))       #打印下载图片的进程
        pic=requests.get(str(i[1]))         #下载图片
        f=open("picture\\"+str(x)+".jpg","wb")  #打开picture目录
        f.write(pic.content)                    #写入图片信息
        f.close()
        x=x+1

for n in range(0,2650,50):
    urls="https://tieba.baidu.com/f?kw=%E9%A3%9F%E7%89%A9&ie=utf-8&pn="+str(n)      #每一页贴吧的链接
    getcontent(urls)




