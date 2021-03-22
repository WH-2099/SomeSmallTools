#!/usr/bin/env python
# -*- coding: utf-8 -*-

'利用埃式算法和生成器求素数'

__author__ = 'WH-2099'


def getNIter(max=-1):
    '返回自然数列生成器'
    n = 0
    while max == -1 or n <= max:
        yield n
        n+=1

def filt(n):
    '返回检查是否能被n整除的lambda'
    return lambda x:x % n != 0

def AiFilt(max=-1):
    '埃式筛选原理求素数，返回生成器'
    it = getNIter()
    n = next(it)
    while max == -1 or n <= max:
        if n < 2:
            if max >= 2 or max == -1:
                n = next(it)
                continue
            else:
                print("Not Find")
                return
        yield n
        it = filter(filt(n),it)
        n = next(it)
        

if __name__ == "__main__":
    print("Please input")
    n = 0
    for x in AiFilt(int(input())):
        n+=1
        print(x)
    print("Totall:%d" % n)


