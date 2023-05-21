from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque()

for i in range(n):
    a, b = input().split()
    if b == 'enter':
        q.append(a)
    else:
        q.remove(a)
sorted(q, reverse=True)
print('\n'.join(q))