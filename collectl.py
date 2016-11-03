#!/usr/bin/python3

from subprocess import check_output as co
from multiprocessing import Process
import os
import time
from sys import argv

def get_mem_used():
    return os.popen('free -h').read().split()[8][:-1]

def check(pname):
    time_x = []
    mem_used = []
    start = time.time()
    mem_info = os.popen('free -h').read().split()
    mem_all = mem_info[7][:-1]
    result = os.popen('ps ax | grep ' + pname + ' | grep -v grep | grep -v python').read().split()
    while True:
        time_x.append(time.time() - start)
        mem_used.append(get_mem_used())
        result = os.popen('ps ax | grep ' + pname + ' | grep -v grep | grep -v python').read().split()
        if not len(result):
            break
        time.sleep(1)
    os.system('kill ' + co('ps -ax | grep "/usr/bin/collectl" | grep -v grep | grep -v python', shell =
        True).decode().lstrip().split(' ')[0])
    with open("mem" + os.getenv("HOSTNAME")[-1]  + ".log", "w") as f:
        for i in range(len(mem_used)):
            f.write(str(mem_all) + ", " + str(time_x[i]) + ", " + str(mem_used[i]) + "\n")

if __name__ == '__main__':
    res = ''
    Process(target = check, args = ('benchmark_parconnect',)).start()
    try:
        res = co('collectl ', shell=True).decode()
    except Exception:
        pass
    print(res)
    with open("infiniband" + os.getenv("HOSTNAME")[-1]  + ".log", "w") as f:
        f.write(res)
