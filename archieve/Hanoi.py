#!/usr/bin/env python
# -*- coding: utf-8 -*-

'递归解决汉诺塔问题'

__author__ = 'WH-2099'

def move(disk,fromtower,totower):
    print("%5d  %s ==> %s" % (disk,fromtower,totower))

def hanoi(disk,fromtower,totower,acrosstower):
    if disk==1:
        move(disk,fromtower,totower)
        return
    hanoi(disk-1,fromtower,acrosstower,totower)
    move(disk,fromtower,totower)
    hanoi(disk-1,acrosstower,totower,fromtower)
        
        
        
        
def main():
    hanoi(int(input("Please input the number of the disks:")),"L","R","M")



if __name__=="__main__":
    main()