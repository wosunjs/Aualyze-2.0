#实现爬取在线漏洞库中有关于**的有用信息并保存在本地
#python 3.10
#encodi = UTF-8
'''
功能描述
目标：实现爬取在线漏洞库中关于“端口——漏洞”的用信息并保存在本地
输出：保存到文件中
技术路线:requests-re-bp4
程序的结构设计
步骤1:从指定网站爬取页面
步骤2:根据端口、危害生成字典
步骤3:将结果存储到相关文件
'''
from importlib.resources import path
from turtle import down
import requests
import re
import os
from bs4 import BeautifulSoup

def getHTMLText (url):      ##爬取网页函数
    try:
        kv = {'user-agent':'Mozilla/5.0'}   #仿制浏览器身份
        r = requests.get(url,headers=kv)
        r.raise_for_status()                #如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding    #使用网页本身的编码方式
        return r.text
    except:
        return "网页请求异常"

def info_draw(html,fpath):
    soup = BeautifulSoup(html,"html.parser")            #先用bp将其做成一锅汤
    pre = soup.find_all('pre')
#    pattern = re.compile('\<span class\=\"token number\"\>1.*')
    dangerList = []
    for i in pre:
        i = i.text
        i = re.findall(r'1\..*',i)
        i = str(i)[4:-2]
        dangerList.append(i)
#    print(i)


    try:
        
        portList = re.findall(r'[0-9]+</span>端口',html)    #利用正则表达式匹配获取有危险的端口列表

        for i in range(len(portList)):
            port = eval(portList[i].split('<')[0])      #进一步对端口信息处理
            danger = dangerList[i]
#            danger = getelite(danger)
            with open(fpath,'a') as f:        
                f.write(str(port)+':'+str(danger))
                f.write('\n')

    except:
        print("")

def is_exist_file(fpath):       #检测文件是否存在，若存在则清空数据若不存在则创建
    if os.path.isfile(fpath):
        F=open(fpath,"w")	
    else:
        F=open(fpath,"x")

def VLcraw():
    url = 'https://blog.csdn.net/Alluresec/article/details/103171729?utm_source=app&app_version=5.3.0&utm_source=app'
    down_path = os.getcwd() + '\VLini.txt'    #默认存储在当前目录下init.txt文件中

    is_exist_file(down_path)                    #检查文件是否存在,若不存在则创建


    #进行页面爬取以及信息处理
    try:
        html = getHTMLText(url)                     #爬取网页
        info_draw(html,down_path)
    except:
        return "信息提取失败"
    
    print("漏洞库更新/生成成功")
    
if __name__=='__main__':
    VLcraw()
