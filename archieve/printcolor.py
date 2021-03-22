#!/usr/bin/env python
# -*- coding: utf-8 -*-
'命令行输出颜色设置'

__author__ = 'WH-2099'

class Color(object):
    '''
格式：\\033[显示方式;前景色;背景色m  
说明：
前景色            背景色           颜色
---------------------------------------
30                40              黑色
31                41              红色
32                42              绿色
33                43              黃色
34                44              蓝色
35                45              紫红色
36                46              青蓝色
37                47              白色
显示方式           意义
-------------------------
0                终端默认设置
1                高亮显示
4                使用下划线
5                闪烁
7                反白显示
8                不可见
'''
    def set(displayType='',frontColor='',backColor=''):
        print('\033[' + displayType + ';' + frontColor + ';' + backColor + 'm')


    def reset():
        print('\033[0m')


    class Type(object):
        default = '0'
        highLight = '1'
        underline = '4'
        twinkle = '5'
        antiWhite = '7'
        invisible = '8'


    class Front(object):
        black = '30'
        red = '31'
        green = '32'
        yellow = '33'
        blue = '34'
        purple = '35'
        cyan = '36'
        white = '37'

    class Back(object):
        black = '40'
        red = '41'
        green = '42'
        yellow = '43'
        blue = '44'
        purple = '45'
        cyan = '46'
        white = '47'
