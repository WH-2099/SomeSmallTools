#!/usr/bin/env python
# -*- coding: utf-8 -*-

'利用正则表达式进行批量文件重命名'

__author__ = 'WH-2099'

import sys
import os
import re

def printAbout():
    '显示程序有关信息'
    print('文件批量重命名工具'.center(50,'*'))
    print('作者：WH-2099'.center(55))

def inputMenuNumber(min,max):
    '输入菜单选项'
    n = input('请输入对应数字以选择操作：')
    while True:
        try:
            n = int(n)
            if n not in range(min,max + 1):
                raise ValueError
        except ValueError:
            n = input('!!!!!输入无效，请重新输入：')
        else:
            break
    return n

def setPath():
    '设置执行目录'
    print('#当前目录：' + os.getcwd() + '\n')
    path = input('请输入目标所在目录：')
    while True:
        if os.path.exists(path):
            break
        else:
            path = input('!!!!!路径不存在，请重新输入：')
    os.chdir(path)
    print('#当前目录：' + os.getcwd() + '\n')



def menuMain():
    '主菜单'
    print('''

[0]----------退出程序
[1]----------删除指定内容
[2]----------替换指定内容
[3]----------插入指定内容

                                  ###以上操作均使用正则表达式###


''')
    mode = inputMenuNumber(0,3)
    if mode == 0:
        sys.exit(0)
    elif mode == 1:
        deleteRename()
    elif mode == 2:
        replaceRename()
    elif mode == 3:
        insertRename()

    


def deleteRename():
    '删除指定内容'
    setPath()
    deleteTarget = re.compile(input('请输入要删除的内容：'))
    fileNames = os.listdir(os.path.curdir)
    for fileName in fileNames:
        os.rename(fileName,re.sub(deleteTarget,'',fileName))
    else:
        print('操作已成功完成'.center(30,'!'))

def replaceRename():
    '替换指定内容'
    setPath()
    target = re.compile(input('请输入要替换的目标：'))
    replace = input('请输入要替换的内容：')
    fileNames = os.listdir(os.path.curdir)
    for fileName in fileNames:
        os.rename(fileName,re.sub(target,replace,fileName))
    else:
        print('操作已成功完成'.center(30,'!'))

def insertRename():
    '插入指定内容'
    setPath()
    target = re.compile(input('请输入要插入的目标：'))
    print('''
[0]-----在目标前插入
[1]-----在目标后插入
''')
    position = inputMenuNumber(0,1)
    insert = input('请输入要插入的内容：')
    fileNames = os.listdir(os.path.curdir)
    for fileName in fileNames:
        result = re.search(target,fileName)
        if result:
            if position == 0:
                x = result.start()
            elif position == 1:
                x = result.end()
            l = list(fileName)
            l.insert(x,insert)
            os.rename(fileName,''.join(l))
        else:
            print('未找到匹配的插入目标'.center(30,'!'))
            insertRename()
            break
    else:
        print('操作已成功完成'.center(30,'!'))    



def main():
    '主执行流程'
    printAbout()
    menuMain()
    

if __name__ == '__main__':
        main()


