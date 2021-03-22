#!/usr/bin/env python
# -*- coding: utf-8 -*-

'爬取笔芯网图片'

__author__ = 'WH-2099'

import urllib.request
import urllib.parse
import urllib.error
import json
import os
import time
import random
import re
from urllib.request import urlretrieve
from multiprocessing import Process

def bixin(idstart,idend):
    i = 0
    opener = urllib.request.build_opener(urllib.request.HTTPHandler)
    ip = str(random.randint(1, 210)) + '.' + str(random.randint(1, 210)) + '.' + str(
        random.randint(1, 210)) + '.' + str(random.randint(1, 210))
    opener.addheaders = [
        ('User-Agent',
         'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'),
        ('X-Forwarded-For', ip),
        ('Host', '118.31.40.206:8888'),
        ('Connection', 'close'),
        ('X-Requested-With', 'XMLHttpRequest'),
        ('Referer', '118.31.40.206:8888')
    ]
    urllib.request.install_opener(opener)
    #伪装为IPhone访问
    for i in range(idstart, idend+1):
        t=0
        while True:
            try:
                result=getpic('http://118.31.40.206:8888/api/moment/list?len=200&userid=' + str(i) )
                if (result != -1):
                    print("ID：[%d] 爬取开始" % i)
                    download(i, result)
            except:
                if t>=10:
                    with open('/storage/emulated/0/programming/Python3/download/data.txt','a') as f:
                        f.write(str(i)+'\n')
                        print(''+'\n[%d]下载失败，存储至data文件')

                        #



                    break
                time.sleep(1)
                t+=1
            else:
                break
          
  
def getpic(url):
    response = json.loads(urllib.request.urlopen(url).read().decode())
    if response['Sucess'] and response['Data'] != []:
        datas = {}
        pattern=re.compile(r'[/\:*"<>|?\s\n]+')
        i=0
        for data in response['Data']:
            content=data['content']
            imgs=data['imgs']
            if content!='':
                content=re.sub(pattern,'',content)
                if content =='':
                    content='未命名'+ ('' if i==0 else str(i))
                    i+=1
            elif len(response['Data'])==1:
                content=''
            else:
                content='未命名'+ ('' if i==0 else str(i))
                i+=1
            datas[content]=imgs
        return datas
    else:
        return -1


def download(id, imgs):
    folder = os.path.join('/storage/emulated/0/programming/Python3', 'download' ,str(id))
    if not os.path.exists(folder):
        os.makedirs(folder)
    for item in imgs:
        if item:
            itemfolder = os.path.join(folder,item[:15])
        else:
            itemfolder=folder
        if not os.path.exists(itemfolder):
            os.makedirs(itemfolder)
        i=0
        for img in imgs[item]:
            ext=os.path.splitext(img)[-1]
            imgpath = os.path.join(itemfolder,str(i))+ext
            try:
                urlretrieve(img, imgpath)
            except:
                os.remove(imgpath)
            i+=1
    print("ID：[%d] 爬取完成" % id)

def redownload():
    ids=[]
    with open('/storage/emulated/0/programming/Python3/download/data.txt','r+')as f:
        for line in f:
            ids.append(int(line))
        f.seek(0,0)
        f.truncate()
    for id in ids:
        bixin(id,id)

if __name__ == '__main__':
    redownload()
    #主要内容集中在ID：0-35000
    for i in range(0,6):
        p=Process(target=bixin,args=(i*5000,(i+1)*5000))
        p.start()