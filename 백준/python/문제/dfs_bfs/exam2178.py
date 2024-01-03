from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nx = [-1, 1, 0, 0]
ny = [0, 0, -1, 1]

g = []
for _ in range(n):
    g.append(list(map(int, input().rstrip())))

def bfs(g, x, y):
    q = deque()
    q.append((x, y))
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            dx = nx[i] + x
            dy = ny[i] + y
            if 0 <= dx < n and 0 <= dy < m and g[dx][dy] == 1:
                g[dx][dy] = g[x][y] + 1
                q.append((dx, dy))

bfs(g, 0, 0)
print(g[-1][-1])