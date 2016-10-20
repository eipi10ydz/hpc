#!/usr/bin/python3

import sys
import re
import matplotlib.pyplot as plt
import numpy as np

def get_data(argv):
    data = []
    if len(argv) > 1:
        with open(argv[1], 'r') as f:
            for line in f:
                if line[0] != '#':
                    raw_data = re.findall(r'\s+(\d+)\s+\S+\s+(\d+)\s+', line, re.M)
                    if len(raw_data):
                        data.append(raw_data[0])
    filename = argv[1]
    if len(argv) > 2:
        filename = argv[2]
    return data, filename

def draw_pic(data, filename = 'Infiniband'):
    sec = np.arange(1, len(data) + 1)
    plt.plot(sec, data[:, 0], '-*', color = 'k')
    plt.plot(sec, data[:, 1], '-.', color = 'g')
    plt.plot(sec, data[:, 2], '-x', color = 'b')
    plt.plot(sec, data[:, 3], '--', color = 'r')
    plt.xlabel('time/sec')
    plt.ylabel('Infiniband/KB')
    plt.title('Infiniband')
    plt.legend(['KBIn', 'KBOut', 'KBAll'])
    plt.savefig(filename)
    plt.close()

if __name__ == '__main__':
    data, filename = get_data(sys.argv)
    data = np.array(list(map(lambda x : [int(x[0]), int(x[1]), int(x[0]) + int(x[1]), 7 * 1024 * 1024], data)))
    draw_pic(data, filename)
