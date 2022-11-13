#!/usr/bin/env python3

import random
import datetime

def smaller(arr):
    ret = [i - 1 for i in range(len(arr), 0, -1)]
    for i in range(len(arr) - 1):
        for j in range(i + 1):
            if arr[j] <= arr[i + 1]:
                ret[j] -= 1
    return ret





print(smaller([5, 4, 7, 9, 2, 4, 1, 4, 5, 6]))
print([5, 2, 6, 6, 1, 1, 0, 0, 0, 0])

start = datetime.datetime.now()
smaller([random.randint(-500,500) for _ in range(20000)])
print(datetime.datetime.now()-start)