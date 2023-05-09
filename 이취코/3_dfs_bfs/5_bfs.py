# bfs
# while 반복 이용

from collections import deque

g = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visit = [False] * 9

def bfs(g, s, visit): # 연결, 시작 노드, 방문 확인
    q = deque()
    
    visit[s] = True
    q.append(s)
    
    while q:
        v = q.popleft()
        print(v, end=' ')
        
        for i in g[v]:
            if not visit[i]:
                q.append(i)
                visit[i] = True

bfs(g, 1, visit)