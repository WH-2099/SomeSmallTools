#!/usr/bin/env python
# -*- coding: utf-8 -*-
'N皇后问题求解'

__author__ = 'WH-2099'


def resultprint(result):
    n=len(result)
    for i in range(n):
        print("-"*result[i]+"+"+"-"*(n-result[i]-1))
        	
def posok(state,x):
    """
    检测目标位置是否符合要求
    """
    y=len(state)
    for i in range(y):
        if abs(x-state[i]) in (0,y-i):
            return False
    else:
        return True
    


def findnextpos(n,state):
    """
    寻找下一个符合要求的位置
    """
    for x in range(n):
        if posok(state,x):
            if len(state)==n-1:
                yield (x,)
            else:
                for result in findnextpos(n,state+(x,)):
                    yield (x,)+result

def main1():
    """
    采用生成器
    """
    n=int(input("How many queens?\n"))
    for index,result in enumerate(findnextpos(n,())):
        print(repr(index)+":")
        resultprint(result)
        print("\n")


def findallpos(n,state,results):
    """
    采用递归方式
    """
    for x in range(n):
        if posok(state,x):
            if len(state)==n-1:
                results.append(state+(x,))
            else:
                findallpos(n,state+(x,),results)
                    


def main2():
    """
    递归方式
    """
    n=int(input("How many queens?\n"))
    results=[]
    findallpos(n,(),results)
    for i in range(len(results)):
        print(repr(i)+":")
        resultprint(results[i])
        print("\n")


if __name__=="__main__":main1()




