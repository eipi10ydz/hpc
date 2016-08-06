#!/usr/bin/python3

import sys
import re
import numpy as np
import matplotlib.pyplot as plt

def draw_time(data, filename = 'computation_and_communication_runtime_along_the_iterations'):
    color_index = ['r', 'g']
    fig, ax = plt.subplots(1, 1, figsize = (10, 10))
    labels = ['computation', 'communication']
    axs = []
    for i in range(2):
        axs.append(ax.bar(np.arange(10) + .75, data[i], width = .5, color = color_index[i], bottom = np.sum(data[:i], axis = 0), alpha = 0.7))
    ax.legend(axs, labels)
    plt.xlabel('iteration')
    plt.ylabel('time/s')
    plt.title("communication versus computation")
    plt.show()
    plt.savefig(filename)
    plt.close()

def draw_tuples(data, filename = "tuples"):
    x = np.arange(len(data))
    plt.plot(x, data[:, 0], '-*', color = 'r')
    plt.plot(x, data[:, 1], '-.', color = 'g')
    plt.plot(x, data[:, 2], '-x', color = 'b')
    plt.xlabel('Iterations')
    plt.ylabel('Count of tuples/million')
    plt.title('Balance of work across processors along the iterations')
    plt.legend(['min', 'mean', 'max'])
    plt.show()
    plt.savefig(filename)
    plt.close()

def count(f):
    cnt = 1
    communicate_res = []
    compute_res = []
    for line in f:
        if 'Algorithm took ' + str(cnt - 1) + ' iterations' in line:
            break
        elif '#' + str(cnt) in line:
            if cnt > 1:
                communicate_res.append(communicate_time)
                compute_res.append(compute_time)
            cnt += 1    
            communicate_time = 0
            compute_time = 0
        else:
            if 'get_splitters' in line or 'all2all' in line:
                communicate_time += float(re.findall(r'(\S+)', line, re.M)[3])
            elif 'TIMER' in line:
                compute_time += float(re.findall(r'(\S+)', line, re.M)[3])
    communicate_res.append(communicate_time)
    compute_res.append(compute_time)
    return communicate_res, compute_res

def draw_pic():
    input_filename = ''
    if len(sys.argv) > 1:
        input_filename = sys.argv[1]
    else:
        input_filename  = input('Please input file name: ')
    f = open(input_filename, 'r')
    res = count(f)
    if len(sys.argv) < 3:
        filename = input('Please input png file name: ')
    else:
        filename = sys.argv[2]
    data = np.array([res[1], res[0]]) / 1000
    draw_time(data, filename)
    f.seek(0)
    s = f.read()
    res = re.findall('Load distribution of active tuples min-mean-max : (\d+),(\d+),(\d+)', s, re.M)
    data =  np.array(list(map(lambda x : [int(y) for y in x], res))) / 1000000
    if len(sys.argv) < 4:
        filename = input('Please input png file name: ')
    else:
        filename = sys.argv[3]
    draw_tuples(data, filename)

if __name__ == '__main__':
    draw_pic()
#    print(sum(res[0]), sum(res[1]))
#6:57.55