#python 3.10
import socket
import re
import time
from . import getinfo as gi

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

#对传入的ip地址，在设定的范围内扫描开放的端口，并打印
def scan_port(ip,list,i_list): 

    #取出工作量
    Scale = len(list)

    #为提高用户体验，此处再加入文本进度条显示
    print("开始服务端口扫描".center(50,"_"))
    start_time = time.perf_counter()     #记录工作起始时间
    i = -1       #记录当前进度和列表中位置

    for pt in list:

        #打印文本进度条
        progbar(i+2,Scale,start_time)
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
            i_list.append(i)
        sk.close()
#    print(open_port_list)    
    print("\n"+"服务端口扫描结束".center(50,"_"))

def ser_scan(ip):

    #读取字典数据
    se_port = gi.get_se_port()
    print("加载服务词典成功")

    i_list = []

    scan_port(ip,se_port,i_list)          #传入字典port数据进行scan

    return i_list               #最终返回一个i的列表，i即为开放端口所在Seini文件中所在行数

    
if __name__=='__main__':
    ip = '39.156.66.14'
    print(ser_scan(ip))       #测试ip为39.156.66.14