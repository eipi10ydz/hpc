#!/usr/bin/python3

import re
import os
from multiprocessing import Process

if __name__ == '__main__':
    file = next(os.walk('.'))[2]
    file_need = [x for x in file if re.findall(r'([(AP_LB_)(AP_)(Naive_)]\d{2,3}?)[^(.png)]$', x)]
    list(map(lambda x : Process(target = os.execlp, args = ('python3', 'python3',  'figure2_figure3_impl.py', x, x + '_2', x + '_3')).start(), file_need))
