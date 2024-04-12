#主程序
#test domain:www.testfire.net    test ip:65.61.137.117

'''
请输入数字1-3进行功能选择:
1.更新/生成字典文件
2.指定ip扫描分析
3.域名解析ip
'''

import os
import socket
import Showup.showme as show
import Dict_craw.leak_list_craw as vlcr
import Dict_craw.service_list_craw as secr
import C_alive_scan.ip_alive_scan as CS
import ip_analyze.inputportscan as inps
import ip_analyze.pd_scan_a as dps
import Main.sip_all_ana as saa

def getIP(domain):
    addr = socket.getaddrinfo(domain,'http')
    print("域名解析结果为")
    print(addr[0][4][0])

def wwwtoip():
    domain = input()
    getIP(domain)

def main():
    show.Banner()
    while 1==1:
        a = int(input())

        if a == 1:                                      #漏洞库更新/生成选项
            print("现在开始更新/生成字典文件")
            vlcr.VLcraw()                               #爬取生成漏洞库字典
            secr.Secraw()                               #爬取生成服务字典

        elif a == 2:                                    #特定主机分析 
            print('-----------------------------------------------')
            print("现在开始扫描分析指定ip主机,请输入数字进行功能选择")
            print("1.指定ip C字段存活主机扫描")
            print("2.指定ip扫描字典漏洞")
            print("3.指定ip端口任意扫描")
            print("4.指定ip全面信息收集")
            b = int(input())
            if b == 1:                  #已完工
                print("现在开始多线程C字段存活主机扫描,请输入ip:")
                CS.Csa()

            elif b == 2:                #已完工
                print("现在开始指定ip扫描字典漏洞扫描")
                dps.port_scan()

            elif b == 3:            #已完工
                print("现在开始指定ip端口任意扫描")
                inps.port_scan()

            elif b == 4:
                print("现在开始对指定ip进行全面分析,请输入ip:")         #已完工
                ip = input()
                saa.siac(ip)

            else:
                print("")

        elif a == 3:                                    #域名解析
            print("现在开始域名解析，请输入网址:")
            wwwtoip()

        else:
            print("输入错误")

        show.keepon()
        print("请继续输入你的请求")


main()