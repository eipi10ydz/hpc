#!/usr/bin/python3

import re
from sys import argv

if __name__ == '__main__':
    result = 0
    if len(argv) > 1:
        with open(argv[1], 'r') as f:
            for line in f:
                if 'fix_partition' in line:
                    res = re.findall(r'TIMER\s+\S+\s+\S+\s+\S+', line)
                    result += float(res[0].split('\t')[-1])
                if 'Time (ms)' in line:
                    res = re.findall(r'-> (\S+)', line)
        print("fix_time: " + str(result) + " total: " + res[0])
