#!/usr/bin/env python
# -*- coding: utf-8 -*-

'提供逆波兰表达式有关转换和计算功能'

__author__ = 'WH-2099'


import re

#regex=r"((\(*)([-+]?\d+)(\)*)([-+*/]?))+"
#注意：[]中-若在字符间有特殊含义
#Python中正则表达式不支持嵌套提取


def allstrip(string):
    return re.sub(r"\s+","",string)


def midtorev(midstring):
    out=[]
    tmp=[]
    order={"+":1,"-":1,"*":2,"/":2,"(":0,}
    splitregex=r"(\(*)([-+]?\d+)(\)*)([-+*/]?)"
    splitpattern=re.compile(splitregex)
    results=splitpattern.findall(allstrip(midstring))
    for seq in results:      
        for i in range(len(seq[0])):
            tmp.append("(")
        out.append(int(seq[1]))
        for i in range(len(seq[2])):
            while tmp[-1]!="(":
            	    out.append(tmp.pop())
            else:
                tmp.pop()
        if seq[3]!="":
            if len(tmp)==0:
                tmp.append(seq[3])
            else:
                if order[seq[3]]>order[tmp[-1]]:
                    tmp.append(seq[3])
                else:
                    while len(tmp)>0:
                        out.append(tmp.pop())
                    else:
                        tmp.append(seq[3])
    else:
        while len(tmp)>0:
            out.append(tmp.pop())
    return out

def revcal(revin):
    rev=revin[:]
    tmp=[]
    while len(rev)>0:
        try:
            rev[0]+0
        except TypeError:
            r=tmp.pop()
            l=tmp.pop()
            m=rev[0]
            del rev[0]
            tmp.append(eval(repr(l)+m+repr(r)))
        else:
            tmp.append(rev[0])
            del rev[0]         
    return tmp[0]

def tostr(seq):
    out=""
    for s in seq:
        try:
            out+=s
        except TypeError:
            out+=repr(s)
    return out

def main():
    s=midtorev(input("Please input middle nanotion:\n"))
    print("Reverse: "+tostr(s))
    print("Reault:  "+repr(revcal(s)))

if __name__=="__main__":main()
    
    