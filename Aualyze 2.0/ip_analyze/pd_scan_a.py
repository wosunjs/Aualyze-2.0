from json.tool import main
import socket
import re
import time
from . import getinfo as gi

#判断输入的ip地址是否合法
def check_ip(ip):
    #通过正则表达式来匹配输入的ip地址是否在正常的范围内以此来判断ip地址是否合法
    ip_moudle = re.compile('((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}')
    if len(ip)!=0 and ip_moudle.match(ip):      #若ip长度不为0且合规则返回真
        return True
    else:
        return False

#使用Fast_Power函数来修改文本进度条显示与实际的效果，以此来提高用户体验
def Fast_Power(now,scale):
    x = now / scale
    y = (x+(1-x)/2) ** 8
    ii = int (y*50)
    return ii

#通过传入当前工作数与工作总数产生文本进度条
def progbar(now,scale,start_time):     
    i = Fast_Power(now,scale)       #调用Fast_Power函数提高用户体验
    a = '*' * i
    b = '_' * (50 - i)
    c = (i/50) * 100
    dur = time.perf_counter() - start_time
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end="")


#生成文件                  先暂时不生成文件了
'''def download(dpath,ip):
    fpath = dpath + '\\' + ip +'_.txt'
    print("")
'''
#对传入的ip地址，在设定的范围内扫描开放的端口，并打印
def scan_port(ip,list,danger): 

    #取出工作量
    Scale = len(list)

    #存储开放端口
    global open_port_list
    open_port_list = []

    global exdanger_list     #存储存在的可疑漏洞,根据开放端口匹配存在的危险,open-port由全局变量引入
    exdanger_list = []

    #为提高用户体验，此处再加入文本进度条显示
    print("开始扫描".center(50,"_"))
    start_time = time.perf_counter()     #记录工作起始时间
    i = 1       #记录当前进度和列表中位置

    for pt in list:

        #打印文本进度条
        progbar(i,Scale,start_time)
        i = i + 1     #定义当前工作进度

        pt = int(pt)
        #使用ipv4实现tcp连接   
        #AF_INET家族包括Internet地址，AF_UNIX家族用于同一台机器上的进程间通信
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #设置延迟0.5s
        sk.settimeout(0.5)  
        #connect_ex()方法，该方法如果链接成功会返回0，失败会返回errno库中的errorcode中的key
        conn = sk.connect_ex((ip,pt))
        
        if conn ==0:
            open_port_list.append(pt)
            exdanger_list.append(danger[i])
        sk.close()
#    print(open_port_list)    
    print("\n"+"扫描结束".center(50,"_"))

def result_output(ip):          #进行最终的输出
    for i in range(len(open_port_list)):
        print('主机:{}开放的端口{}可能存在{}'.format(ip,open_port_list[i],exdanger_list[i]))

def port_scan():

#    down_path = '..\Output'          #记得修改为Aualyze的Output文件夹

    #读取字典数据
    port = gi.getport()
    danger = gi.getdanger()
    print("加载词典成功")

    ip = input('请输入需要扫描的ip:')
    if check_ip(ip):
        scan_port(ip,port,danger)          #传入字典port数据进行scan
#        print(exdanger_list)
#        download(down_path,ip)              #传入路径和ip地址进行创建/更新文件
        result_output(ip)
    else:
        print("ip格式不正确,请重新输入!")

    
if __name__=='__main__':
    port_scan()