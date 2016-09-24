#!/usr/bin/python3

import sys
import os
import re
import numpy as np
import matplotlib.pyplot as plt

def draw_time(x, data, filename = "time"):
    plt.plot(x, data[:, 0], '-*', color = 'r')
    plt.plot(x, data[:, 1], '-.', color = 'g')
    plt.plot(x, data[:, 2], '-.', color = 'b')
    plt.xlabel('Number of cores')
    plt.ylabel('Time/sec')
    plt.title('Performance of the three algorithm variants for data D1')
    plt.legend(['AP_LB', 'AP', 'Naive'])
    #plt.show()
    plt.savefig(filename)
    plt.close()
"""
only deal with AP_LB_xxx, AP_LB_xxx, Naive_xxx, etc.
"""
if __name__ == '__main__':
    file = next(os.walk('.'))[2]
    AP = list(map(lambda x : (float(re.findall(r'Time \(ms\) -> (\S+)', open(x, 'r').read())[0]), x[3:]) , [x for x in file if len(re.findall(r'AP_\d{2,3}[^(.png)]$', x))]))
    AP_LB = list(map(lambda x : (float(re.findall(r'Time \(ms\) -> (\S+)', open(x, 'r').read())[0]), x[6:]) , [x for x in file if len(re.findall(r'AP_LB_\d{2,3}[^(.png)]$', x))]))
    Naive = list(map(lambda x : (float(re.findall(r'Time \(ms\) -> (\S+)', open(x, 'r').read())[0]), x[6:]) , [x for x in file if len(re.findall(r'Naive_\d{2,3}[^(.png)]$', x))]))
    AP = sorted(AP, key = lambda x : int(x[1]))
    AP_LB = sorted(AP_LB, key = lambda x : int(x[1]))
    Naive = sorted(Naive, key = lambda x : int(x[1]))
    x = [int(item[1]) for item in AP]
    AP = [item[0] for item in AP]
    AP_LB = [item[0] for item in AP_LB]
    Naive = [item[0] for item in Naive]

    data = np.array(list(zip(AP_LB, AP, Naive)))
    if len(AP) == len(AP_LB) and len(AP_LB) == len(Naive) and len(AP) == len(Naive):
        pass
    else:
        print("data not match!!!")
        print(x)
        print(data)
    if len(sys.argv) > 1:
        draw_time(x, data, sys.argv[1])
    else:
        draw_time(x, data, input('Please input file name: '))
    
