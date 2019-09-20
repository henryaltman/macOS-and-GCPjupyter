
# 本帖最后由 xiaohui 于 2018-11-11 15:12 编辑

# 执行下面这些代码条件：
# 需要部署提供运行这些代码的环境
# 安装代码中的外部模块
# 代码中的有些参数需要改成实际的参数，比如Cookie,url,这些
# 分析代码中的路径，在相应路径下建立对应的目录


# 以下就是源代码

#_*_ coding:utf-8 _*_
#导入若干模块
import os
import re
import sys
import requests
import time
from Crypto.Cipher import AES
import subprocess
from binascii import b2a_hex, a2b_hex
#-----------------------------------------------------------------------
#公共请求头/全局通用
headers={
        'Accept': '* / *',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Connection':'keep-alive',
        'Host':'videotts.it211.com.cn',
        'Origin':'http://tts.tmooc.cn',
        'Referer':'http://tts.tmooc.cn/video/showVideo?menuId=691210&version=AIDTN201903',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Connection': 'close',
        'Cookie':'54D0E601D8784E7CAAC8E9A9616BB2D2|E_bfuo1l9'
    }
#-----------------------------------------------------------------------
#获取m3u8url
def get_ts_url(url,filenames):
    #请求m3u8集合文件
    try:
        m3u8=requests.get(url, headers=headers,timeout=10).content.decode()

        #提取文件中的秘钥key地址
        # key_url=re.findall(r'EXT-X-KEY:METHOD=AES-128,URI="(.*)"', m3u8)[0]
        key_url='http://videotts.it211.com.cn/aid19040905am/static.key'
        print(key_url)
    except:
        print("----")
        return 10
    #判断是否是正常的m3u8文件
    if "EXTINF" in m3u8:
        #获取m3u８中的每一行
        file_line = m3u8.split('\n')
        #循环取出每个ts文件的url,并且生成列表
        for line in file_line:
            if '.ts' in line:
                #生成文件名称
                file_name=line.split('-')[1]
                #循环下载每个ts文件
                error1=get_ts(line,file_name,key_url)
                if error1==10:
                    return error1
        # ts全部下载完成后开始合并
        hebin_videos(filenames)
    else:
        print('此文件不是m3u8格式的标准文件！！')
        #退出程序
        exit()
#----------------------------------------------------------------------------
#下载每个ｔｓ文件
def get_ts(url,file_name,key_url):
    #获取ｔｓ二进制文件
    video=requests.get(url,headers=headers,timeout=10).content
    #判断文件是否为空
    if len(video):
        #获取秘钥ｋｅｙ
        key=get_key(key_url)
        #使用aes开始解密算法
        cryptor = AES.new(key, AES.MODE_CBC, key)
        #开始保存ts文件到本地
        with open(os.getcwd() + '/videos/'+file_name, 'ab') as f:
            #解密并且写入保存
            try:
                f.write(cryptor.decrypt(video))
            except:
                return 10

        print(file_name+"下载成功")
    else:
        print('视频获取失败！！')
        exit()
#----------------------------------------------------------------------------
# 获取秘钥文件
def get_key(key_url):
    #秘钥文件地址
    url=key_url
    #请求秘钥
    key=requests.get(url, headers=headers,timeout=10).content
    return key
    pass
#----------------------------------------------------------------------------
#排序处理
def sorts(videos_path):
    file = []
    # 获取目录下的所有ｔｓ文件
    files = os.listdir(videos_path)
    # 只取出文件数字前zui,然后进行从小到大排序
    for i in files:
        num_file = int(i.split('.')[0])
        # 将文件前zui放进列表
        file.append(num_file)
    # 正序排列
    file.sort()
    return file
#-----------------------------------------------------------------------------
#视频合并
def hebin_videos(filenames):
    file=sorts(os.getcwd() +'/videos')
    #定义存储字符串容器
    long_file=''
    for i in file:
        #字符串拼接处理
        long_file += str(i) + '.ts|'
    #删除最后一位处理
    ts = long_file[:-1]
    #合成整条命令
    os.chdir(os.getcwd()+'/videos')
    cmd='ffmpeg -i "concat:%s" -c copy -bsf:a aac_adtstoasc -movflags +faststart ../one_videos/%s.mp4' % (ts,filenames)
    reqult=subprocess.call(cmd,shell=True)
    if reqult==0:
        print(str(filenames)+'.mp4下载成功')
        #删除所有ｔｓ
        tts=subprocess.call("rm -rf %s" % ('/Users/peng/Desktop/ToStudent/Code_Study/spider/videos/*'),shell=True)
        if tts!=0:
            print('删除ts文件失败！！,程序退出')
            exit()
    else:
        print('视频合并失败,程序退出！！')
        exit()
#------------------------------------------------------------------------------
#主函数
def mains():
    errors=[]
    # 删除所有ｔｓ
    subprocess.call("rm -rf %s" % ('/Users/peng/Desktop/ToStudent/Code_Study/spider/videos/*'), shell=True)
    # words='http://videotts.it211.com.cn/aid1904(.*)/aid1904(.*).m3u8'
    words='http://videotts.it211.com.cn/aid19040905am/aid19040905am-(.*).ts'

    with open(os.getcwd() + '/m3u8.txt') as fobj:
        for i in fobj:
            os.chdir('/Users/peng/Desktop/ToStudent/Code_Study/spider')

            try:
                filenames=re.findall(words, i)[0]

            except:
                print( words, i)
                print('IndexError')
                with open('/Users/peng/Desktop/ToStudent/Code_Study/spider/error.txt','a+') as fobj1:
                    fobj1.write(i)
                errors.append(i)
                continue
            error=get_ts_url(i.strip(),filenames)

            if error==10:

                errors.append(filenames)
                print(filenames+'跳过')
                with open('/Users/peng/Desktop/ToStudent/Code_Study/spider/error.txt','a+') as fobj1:
                    fobj1.write(i)
                # 删除所有ｔｓ
                subprocess.call("rm -rf %s" % ('/Users/peng/Desktop/ToStudent/Code_Study/spider/videos/*'), shell=True)
                continue
    return errors
#-------------------------------------------------------------------------------
error=mains()
print('*'*50+'报错ｔｓ如下'+'*'*50)
for i in error:
    print(i)
