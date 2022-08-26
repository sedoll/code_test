#AC

import sys 
from collections import deque as dq
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    flag = 0
    p = input().strip()
    n = int(input())
    arr = input().strip()[1:-1].split(',')
    d = dq(arr)
    s = True
    for i in p:
        if len(d) == 0 or p.count('D') > n:
            s = False
            break
        elif i == 'R':
            flag += 1
        elif i == 'D':
            if flag % 2 == 0:
                d.popleft()
            else:
                d.pop()
    if flag % 2 == 1:
        d.reverse()
    if s == True:
        print("[" + ",".join(d) + "]")
    if s == False:
           print("error")