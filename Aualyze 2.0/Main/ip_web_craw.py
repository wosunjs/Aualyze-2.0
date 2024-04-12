#实现通过ip地址爬取其绑定过的域名（爬虫爬取https://ipchaxun.com/202.204.80.112/）
'''
功能分析:
目标:通过输入的ip定向爬取历史挂载网页列表并返回
输出:返回一个列表
技术路线:requests-re-bp4
程序的结构设计
步骤1:从指定网站爬取页面
步骤2:根据标签爬取指定数据
步骤3:将结果返回
'''
import requests
from bs4 import BeautifulSoup
import re

def getHTMLText (url):      ##爬取网页函数
    try:
        kv = {'user-agent':'Mozilla/5.0'}   #仿制浏览器身份
        r = requests.get(url,headers=kv)
        r.raise_for_status()  #如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding    #使用网页本身的编码方式
        return r.text
    except:
        return "网页请求异常"

def hw_craw(ip):        #定义主函数，传入ip，返回历史挂载网页列表
    print('现在开始对历史挂载网页进行爬取收集')
    ip = 'https://ipchaxun.com/' + ip
    text = getHTMLText(ip)
    soup = BeautifulSoup(text,"html.parser")
    get_div = soup.find(id = 'J_domain')                #先用bp的find函数找到ip为Jd的标签
    a_list =get_div.find_all('a')                       #再在其中找到a标签
#    pattern = re.compile(ur'/.*/"')
    result = []
    for i in a_list:
        i = str(i['href'])
        i = i[1:-1]
        result.append(i)                        #读取a标签中所有的内容
    print('历史挂载网页爬取结束')
    return result
    


if __name__=='__main__':
#    ip=input('请输入一个ip:')
    ip = '202.204.80.112'
    print(hw_craw(ip))