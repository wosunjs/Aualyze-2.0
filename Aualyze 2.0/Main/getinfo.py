#python 3.10
import os

def getport():      #获取漏洞端口列表
    port = []
    danger = []
    f = open(r"C:\Users\七星\Desktop\Aualyze 2.0\VLini.txt")             # 返回一个文件对象  
    line = f.readline()             # 调用文件的 readline()方法  
    while line:                   #逐行读入 
        port.append(line.split(":")[0])     #根据:可分别读入端口与危险
        danger.append(line.split(":")[1])
        line = f.readline()  
    f.close() 
#    print(port)
    return port

def getdanger():    #获取漏洞danger列表
    port = []
    danger = []
    f = open(r"C:\Users\七星\Desktop\Aualyze 2.0\VLini.txt")             # 返回一个文件对象  
    line = f.readline()             # 调用文件的 readline()方法  
    while line:                   #逐行读入 
        line = line.strip('\n')
        danger.append(line.split(":")[1])
        line = f.readline()  
    f.close() 
#    print(danger)
    return danger

def get_se_port():
    se_port_list = []
    f = open(r'C:\Users\七星\Desktop\Aualyze 2.0\Seini.txt')
    line = f.readline()
    while line:             #逐行读入
        se_port_list.append(line.split(":")[0])
        line = f.readline()         #读入下一行
    f.close()
#    print(se_port_list)
    return se_port_list

def get_servie():
    ser_list = []
    f = open(r'C:\Users\七星\Desktop\Aualyze 2.0\Seini.txt')
    line = f.readline()
    while line:             #逐行读入
        line = line.strip('\n')                 #去掉每行结尾的换行
        ser_list.append(line.split(":")[1])
        line = f.readline()         #读入下一行
    f.close()
#    print(ser_list)
    return ser_list

def get_alive_ip():
    ip_list = []
    f = open(r'C:\Users\七星\Desktop\Aualyze 2.0\ip_alive_list.txt')
    line = f.readline()
    while line:
        line = line.strip('\n')
        ip_list.append(line)
        line = f.readline()
    f.close()
#    print(ip_list)
    return ip_list

if __name__=='__main__':
    getport()
    getdanger()
    get_se_port()
    get_servie()
    get_alive_ip()
