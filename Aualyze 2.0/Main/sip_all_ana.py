#单个ip全面分析主文件
'''
全部信息收集包括：
1.操作系统分析
2.端口扫描,可疑漏洞分析，
3.端口服务匹配
4.挂载网页信息爬取
5.旁站信息爬取          
5.whois爬取                     #待定
6.归属地爬取            #4里面有
'''
import os
import re
from . import ip_os_a as iposs
from . import ip_addr_craw as ipadr
from . import ip_port_scan as ipps
from . import ip_ser_scan as ipse
from . import getinfo as gi
from . import ip_web_craw as ipws
from . import side_ip_craw as sips
from . import mess_keep as mk

def check_ip(ip):
    #通过正则表达式来匹配输入的ip地址是否在正常的范围内以此来判断ip地址是否合法
    ip_moudle = re.compile('((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}')
    if len(ip)!=0 and ip_moudle.match(ip):      #若ip长度不为0且合规则返回真
        return True
    else:
        return False

#主函数
def siac(ip):
#    ip = input()                #输入ip，并对其格式进行检查
    if check_ip(ip):
        pass
    else:
        print("ip格式不正确,请重新输入!")

    f_path = r'C:\Users\七星\Desktop\Aualyze 2.0\Output\\'  + ip + '.html'        #创建报告html文件

    if os.path.exists(f_path):                  #检测文件是否存在若存在则清空若不存在则创建
        F=open(f_path,'w')
    else:
        F=open(f_path,'x')
    print('报告文件创建成功')

    ipos = iposs.ipos(ip)           #获取ip的操作系统
    print('操作系统解析完成')

    ipad = ipadr.ipaddr_craw(ip)        #获取ip归属地
    print('ip归属地信息爬取成功')
    
    i_list = ipps.s_port_scan(ip)               #端口扫描——漏洞匹配
    ipps_list = []      #获取开放端口信息（危险端口）
    ipda_list = []       #匹配可能存在的漏洞
    port = gi.getport()       #读取字典获取数据
    danger = gi.getdanger()
    for i in i_list:        #进行信息匹配
        i = int(i)
        ipps_list.append(port[i])
        ipda_list.append(danger[i])
#    print(ipps_list)
#    print(ipda_list)
    
    i_se_port_list = ipse.ser_scan(ip)          #进行服务扫描，返回开放服务所在Seini文件中所在行数
    serive_list = []
    d_se_port_list = gi.get_se_port()           #获取字典数据
    d_ser = gi.get_servie()
    for i in i_se_port_list:                    #进行信息匹配
        i = int(i)
        ipps_list.append(d_se_port_list[i])     #将开放的服务端口添加进开放端口列表中                   后期再去重
        serive_list.append(d_ser[i])
                                
    web_list = ipws.hw_craw(ip)                                            #获取历史挂载网页
#    print(web_list)

    side_ip_list = sips.sip_craw(ip)                          #获取旁站列表
#    print(side_ip_list)

    print('现在开始写入数据')
    mk.download(f_path,ip,ipos,ipad,ipps_list,ipda_list,serive_list,web_list,side_ip_list)                                                    #调用所有信息进行写入
    print('分析报告已生成，请点击查看')

'''
    print('操作系统为:{}'.format(ipos))
    print('归属地为:{}'.format(ipad))
    print('开放的端口有:{}'.format(ipps_list))
    print('可能存在的威胁有:{}'.format(ipda_list))
    print('开放的服务有:{}'.format(serive_list))
    print('历史挂载的网页有:{}'.format(web_list))
    print('它的旁站有:{}'.format(side_ip_list))'''


if __name__=='__main__':
#    ip = '39.156.66.14'             #实验ip为39.156.66.14
#    ip = '65.61.137.117'            #实验ip为65.61.137.117
    ip = input('请输入一个ip:')
    siac(ip)
