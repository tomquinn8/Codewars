#!/usr/bin/env python3

import random
import datetime

def smaller(arr):
    ret = []
    while arr:
        ret.append(len([j for j in arr if j < arr[0]]))
        arr.remove(arr[0])
    return ret






print(smaller([5, 4, 7, 9, 2, 4, 1, 4, 5, 6]))
print([5, 2, 6, 6, 1, 1, 0, 0, 0, 0])

start = datetime.datetime.now()
smaller([random.randint(-500,500) for _ in range(20000)])
print(datetime.datetime.now()-start)