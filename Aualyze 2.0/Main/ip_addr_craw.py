#实现通过ip地址爬取其绑定过的域名（爬虫爬取https://ipchaxun.com/202.204.80.112/）
'''
功能分析:
目标:通过输入的ip定向爬取ip归属地并返回
输出:返回归属地字符串
技术路线:requests-re-bp4
程序的结构设计
步骤1:从指定网站爬取页面
步骤2:根据标签爬取指定数据
步骤3:将结果返回
'''
import requests
from bs4 import BeautifulSoup
import re
import random
from . import getinfo as gi

def getHTMLText (url):      ##爬取网页函数
    a_ip_list = gi.get_alive_ip()
    useip = random.choice(a_ip_list)
    
    try:
        kv = {'user-agent':'Mozilla/5.0'}   #仿制浏览器身份
        proxies={'http':useip}#代理ip
        r = requests.get(url,headers=kv,proxies=proxies)
        r.raise_for_status()  #如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding    #使用网页本身的编码方式
        return r.text
    except:
        return "网页请求异常"

def ipaddr_craw(ip):        #定义主函数，传入ip，返回历史挂载网页列表
    print('现在开始对ip归属地进行爬取收集')
    ip = 'https://ipchaxun.com/' + ip
    text = getHTMLText(ip)
    soup = BeautifulSoup(text,"html.parser")
    get_p = soup.find('p')                #先用bp的find函数找到p标签
    i = re.findall(r'归属地：.*',get_p.text)
    result = i[0][4:]                   #通过正则表达式匹配获取所需要的信息
    return result
    


if __name__=='__main__':
#    ip=input('请输入一个ip:')
    ip = '202.204.80.112'
    print(ipaddr_craw(ip))