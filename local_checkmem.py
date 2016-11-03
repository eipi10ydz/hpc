#!/usr/bin/python3
# -*- coding:utf-8 -*-

import os
import time
import sys
import matplotlib.pyplot as plt

def get_mem_used():
    return os.popen('free -h').read().split()[8][:-1]

def check(pname):
    print(pname)
    time_x = []
    mem_used = []
    res = os.popen('ps ax | grep ' + pname + ' | grep -v grep | grep -v python')
    start = time.time()
    mem_info = os.popen('free -h').read().split()
    mem_all = mem_info[7][:-1]
    result = res.read().split()
    print(result)
    while len(result):
        time_x.append(time.time() - start)
        mem_used.append(get_mem_used())
        res = os.popen('ps ax | grep ' + pname + ' | grep -v grep | grep -v python')
        result = res.read().split()
        print(result)
        time.sleep(1)
    return mem_all, time_x, mem_used

def plotpng(pname, mem_all, time_x, mem_used):
    plt.plot(time_x, mem_used)
    plt.xlabel('time/s')
    plt.ylabel('mem_used/GiB')
    plt.title(pname)
    plt.savefig(pname)

if __name__ == '__main__':
    #if len(sys.argv) == 2:
    #    pname = sys.argv[1]
    #    mem_all, time_x, mem_used = check(sys.argv[1])
    #else:
    #    pname = input("input the program to be checked:")
    #    mem_all, time_x, mem_used = check(pname)
    mem_all = []
    time_x = []
    mem_used = []
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            for line in f:
                l = line.split(", ")
                mem_all.append(float(l[0]))
                time_x.append(float(l[1]))
                mem_used.append(float(l[2]))
    if len(sys.argv) > 2:
        pname = sys.argv[2]
    else:
        pname = sys.argv[1]
    plotpng(pname, mem_all, time_x, mem_used)
