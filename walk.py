#!/usr/bin/python3.4

import os
import re
import sys

def find(pattern, dir = '.'):
    to_find = os.walk(dir)
    while True:
        try:
            found = next(to_find)
            for file in found[2]:
                file = os.path.join(found[0], file)
                with open(file, 'r', encoding = 'utf-8') as f:
                    if re.findall(pattern, f.read(), re.M):
                        print(file)
        except StopIteration:
            print("end...")
            return
        except UnicodeDecodeError:
            print("Decode error:" + file)
        except FileNotFoundError:
            print("FileNotFoundError:" + file)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        find(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 2:
        find(sys.argv[1], '.')
    else:
        find(input("pattern:"), input("dir:"))
