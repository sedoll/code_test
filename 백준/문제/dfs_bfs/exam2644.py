# 촌수 계산
# bfs
# visit를 -1로 초기화 해서 a, b가 연결이 되있으면 -1이 아니고
# 연결이 안되있으면 -1이 되도록 코드 작성

from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())
g = [[] for _ in range(n+1)]
visit = [-1] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)

def bfs(g, s, visit):
    q = deque()
    q.append(s)
    visit[s] = 0
    while q:
        s = q.popleft()
        for i in g[s]:
            if visit[i] == -1:
                q.append(i)
                visit[i] = visit[s] + 1

bfs(g, a, visit)
print(visit[b])