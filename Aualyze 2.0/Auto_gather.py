from json.tool import main
import sys
import Main.sip_all_ana as sas
import re

def check_ip(ip):
    #通过正则表达式来匹配输入的ip地址是否在正常的范围内以此来判断ip地址是否合法
    ip_moudle = re.compile('((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}')
    if len(ip)!=0 and ip_moudle.match(ip):      #若ip长度不为0且合规则返回真
        return True
    else:
        return False

def main():
    txt = sys.argv[1]
    sucip = []
    defip = []
   
    F = open(str(txt))
    F = F.read().splitlines()
    for ip in F :
        if check_ip(ip):
            sucip.append(ip)
            print(ip)
            sas.siac(ip)
        else:
            defip.append(ip)

    print('已成功扫描分析爬取如下ip列表：')
    for i in sucip:
        print(i)
    print('以下输入ip格式出误')
    for k in defip:
        print(k)


    
if __name__=='__main__':
    main()