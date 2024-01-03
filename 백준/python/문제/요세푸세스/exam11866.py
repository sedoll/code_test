# 요세푸세스 0

from collections import deque
n, k = map(int, input().split())
queue = deque([i+1 for i in range(n)])
print('<', end='')
for _ in range(n-1):
    for _ in range(k-1):
        queue.append(queue.popleft())
    print(queue.popleft(), end=', ')
print(queue.popleft(), end='>')