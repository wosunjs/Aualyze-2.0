from json.tool import main
import socket
import re
import time
import os

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
    i = Fast_Power(now,scale)
    a = '*' * i
    b = '_' * (50 - i)
    c = (i/50) * 100
    dur = time.perf_counter() - start_time
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end="")

#对传入的ip地址，在设定的范围内扫描开放的端口，并打印
def scan_port(ip): 
    #取出范围值
    print("请有序输入扫描的开始端口和结束端口。格式为“开始端口号-结束端口号”")
    port_begin,port_end = input().split("-")
    openlist = []
    
    #为提高用户体验，此处再加入文本进度条显示
    print("开始端口扫描".center(50,"_"))
    start_time = time.perf_counter()     #记录工作起始时间
    k=int(port_begin)

    
    for pt in range(int(port_begin),int(port_end)+1):

        pscale = int(port_end) - int(port_begin) + 1   #定义总工程量
        i = pt - k + 1     #定义当前工作进度
        progbar(i,pscale,start_time)

        #使用ipv4实现tcp连接   
        #AF_INET家族包括Internet地址，AF_UNIX家族用于同一台机器上的进程间通信
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #设置延迟0.5s
        sk.settimeout(0.5)  
        #connect_ex()方法，该方法如果链接成功会返回0，失败会返回errno库中的errorcode中的key
        conn = sk.connect_ex((ip,pt))
        
        if conn ==0:
            openlist.append(pt)
#            print(f'主机:{ip},端口:{pt}已开放')
#        else:
#            print(f'主机:{ip},端口:{pt}未开放')
        sk.close()
        
    print("\n"+"扫描结束".center(50,"_"))
    for i in openlist:
        print(f'主机:{ip},端口:{i}已开放')

def port_scan():
    ip = input('请输入需要扫描的ip:')
    if check_ip(ip):
        scan_port(ip)
    else:
        print("ip格式不正确,请重新输入!")
        
if __name__=='__main__':
    port_scan()