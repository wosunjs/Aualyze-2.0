#通过传入数据来生成html文档
import codecs



def download(f_path,ip,ip_os,ip_ad,ip_opp_list,ip_danger_list,ip_ser_list,ip_hweb_list,ip_sweb_list):
    a = '''
    <!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <title>信息收集-分析结果</title>
  <style>
    body {
      margin: 0;
      overflow: hidden;
      width: 100vw;
      user-select: none;
      overflow-y: auto;
    }
  

    * {
      text-align: center;
    }

    .div0 {
      width: 100vw;
      overflow: hidden;
    }
    .bg{
      width: 100%;
    }
    .div_in {
      margin: auto;
    }

    .div1 {
      box-sizing: border-box;
      width: 100vw;
      padding-top: 16px;
      margin-bottom: 18px;
    }

    .head1 {
      font-weight: 900;
      font-size: 32px;
        color: rgb(179, 45, 45);
    }

    .head2 {
      font-weight: 200;
    }

    .div2 {
      box-sizing: border-box;
      width: 100vw;
      display: flex;
      justify-content: space-evenly;
    }

    .item {
      width:20vw;
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    .img {
      width: 10vh;
      height: 10vh;
      background-color: black;
      display: flex;
    }

    .img_in {
      margin: auto;
    }

    .head {
      font-weight: 800;
      margin: 20px;
    }

    .content {
      margin: 10px;
    }
  </style>
</head>

<body>
  <div class="div0">
    <img class="bg" src="./bg.png"  alt="">
  </div>
  <div class="div1">
    <div class="head1">IP:
    '''
    b = '''
    </div>
    <div class="head2">操作系统为:
    '''
    c = '''
    </div>
  </div>
  <div class="div2">
    <div class="item">
      <div class="img">
        <img src="./端口.jpg" alt="">
      </div>
      <div class="head">开放端口列表</div>
    '''
    d = '''
    </div>
    <div class="item">
      <div class="img">
        <img src="./1.jpg" alt="">
      </div>
      <div class="head">可疑威胁列表</div>
    '''
    e = '''
     </div>
    <div class="item">
      <div class="img">
        <img src="./2.jpg" alt="">
      </div>
      <div class="head">开放服务列表</div>
    '''
    f = '''
    </div>
    <div class="item">
      <div class="img">
        <img src="./3.jpg" alt="">
      </div>
      <div class="head">历史挂载网页列表</div>
    '''
    g = '''
    </div>
    <div class="item">
      <div class="img">
        <img src="./4.jpg" alt="">
      </div>
      <div class="head">旁站列表</div>
    '''
    h = '''
    </div>
  </div>
  <script></script>
</body>

</html>
    '''
    F=codecs.open(f_path,'w','utf-8')
#    F=open(f_path,'w','utf-8')
    F.write(a)          #写入最前端代码
    F.write(ip)         #写入ip
    F.write(b)
    F.write(ip_os)      #写入操作系统
    F.write('归属地为:')
    F.write(ip_ad)
    F.write(c)
    for i in ip_opp_list:           #循环写入端口列表
        i = '<div class="content">' + i + '</div>'
        F.write(i)
    if len(ip_opp_list) == 0 :
        i = '<div class="content">未检测到可疑端口</div>'
        F.write(i)
    F.write(d)                      
    for j in ip_danger_list:        #循环写入可疑威胁列表
        j = '<div class="content">' + j + '</div>'
        F.write(j)
    if len(ip_danger_list) == 0 :
        j = '<div class="content">未检测到可疑威胁</div>'
        F.write(j)
    F.write(e)
    for k in ip_ser_list:           #循环写入开放服务列表
        k = '<div class="content">' + k + '</div>'
        F.write(k)
    if len(ip_danger_list) == 0 :
        k = '<div class="content">未检测到可疑威胁</div>'
        F.write(k)
    F.write(f)
    for l in ip_hweb_list:           #循环写入历史挂载网页列表
        l = '<div class="content">' + l + '</div>'
        F.write(l)
    F.write(g)
    for m in ip_sweb_list:           #循环写入历史挂载网页列表
        m = '<div class="content">' + str(m) + '</div>'
        F.write(m)
    F.write(h)
    F.close()

if __name__=='__main__':
    path = r'C:\Users\七星\Desktop\Aualyze\Output\65.61.137.117.html'
    ip = '65.61.137.117'
    ip_os = 'windows'
    port = ['445', '1099', '9000']
    danger = [' MS17<span class="to\n', ' java_rmi反序列化远程命令执行\n', 'an class="token numb\n']
    serive = ['端口服务匹配失败,常见端口已被修改']
    his_weh = ['/www.testfire.net/', '/testfire.net/', '/demo.testfire.net/', '/altoromutual.com/', '/lfshengtang.com/', '/cdhdd.net/']
    si_web = ['65.61.137.117']
    download(path,ip,ip_os,port,danger,serive,his_weh,si_web)
