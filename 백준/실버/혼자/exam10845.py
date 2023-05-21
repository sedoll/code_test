# 큐

from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
d = deque()
for _ in range(n):
    l = list(map(str, input().split()))
    if l[0] == 'push':
        d.appendleft(int(l[1]))
    elif l[0] == 'pop':
        print(-1 if len(d) == 0 else d.pop())
    elif l[0] == 'front':
        print(-1 if len(d) == 0 else d[-1])
    elif l[0] == 'back':
        print(-1 if len(d) == 0 else d[0])
    elif l[0] == 'size':
        print(len(d))
    elif l[0] == 'empty':
        print(1 if len(d) == 0 else 0)