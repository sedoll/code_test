# 숨바꼭질

from collections import deque
import sys
input = sys.stdin.readline

MAX = 100000
n, k = map(int, input().split())
visit = [0] * (MAX+1)

def bfs(s, visit):
    q = deque([s])
    
    while q:
        v = q.popleft()
        if v == k:
            return visit[v]
        
        for i in (v-1, v+1, v*2):
            if 0 <= i <= MAX and not visit[i]:
                visit[i] = visit[v]+1
                q.append(i)
print(bfs(n, visit))