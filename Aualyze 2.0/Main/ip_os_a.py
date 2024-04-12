import os
import re

def ipos(ip):
    a = 0
    b = 1
    cmd="ping %s -w 1000 -n 1"%ip
    r2=os.popen(cmd).read()
    result=re.search(r"TTL=(\d+)",r2)
    if result:
        if int(result.group(1))>64:
            return 'windows'
        else:
            return 'linux'
    else:
        pass



if __name__=="__main__":
    print("请输入一个ip:")
    ip = input()
    print(ipos(ip))
