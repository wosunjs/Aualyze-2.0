import time
from subprocess import Popen, PIPE
import threading
import os

threads = []
thread_max = threading.BoundedSemaphore(255)

#创建存储文件
def store(fpath,list):
    if os.path.isfile(fpath):
        with open(fpath,'w') as f:        #若文件存在则直接将相关信息覆盖地全部保存到文件中
            for i in list:
                f.write(str(i)+'\n')
    else:
        with open(fpath,'x') as f:        #若文件不存在则创建写入
            for i in list:
                f.write(str(i)+'\n')


# ping检测
def ping_check(ip):
    # ip = '127.0.0.1'
    check = Popen('ping {0}\n'.format(ip), stdin=PIPE, stdout=PIPE, shell=True)
    data = check.stdout.read()
    data = data.decode('GBK')

    if 'TTL' in data:
        print('[+] The host {0} is alive'.format(ip))
        list.append(ip)

# 多线程执行
def main(ip):
    # ip = '192.168.1.'
    down_path = '.\ip_alive_list.txt'    #默认存储在当前目录下CSini.txt文件中

    global list
    list = []
    for i in range(1, 255):
        new_ip = ip + str(i)
        thread_max.acquire()
        t = threading.Thread(target=ping_check, args=(new_ip,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    iplist = list
    store(down_path,iplist)

def Csa():
    ip = input()
    print('[+] Strat scaning......Please wait...')
    start = time.time()
    main(ip[:-1])
    end = time.time()
    print('[+] Scan success---------------------')
    print("------------耗时{0:.5f}秒------------".format(end - start))

if __name__ == '__main__':
    ip = input("Please input ip (192.168.1.1): ")

    print('[+] Strat scaning......Please wait...')
    start = time.time()
    main(ip[:-1])
    end = time.time()
    print('[+] Scan success---------------------')
    print("------------耗时{0:.5f}秒------------".format(end - start))
    
