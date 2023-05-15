# 구슬 탈출2
# bfs

from collections import deque

n, m = map(int, input().split())
l = []

g = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    g.append(list(input()))
    for j in range(m):
        if g[i][j] == 'R': # 빨간공의 좌표
            rx, ry = i, j
        elif g[i][j] == 'B': # 파란공의 좌표
            bx, by = i, j

def bfs(rx, ry, bx, by):
    q = deque()
    q.append((rx, ry, bx, by))
    visit = [] # 방문 여부 확인
    
    visit.append((rx, ry, bx, by))
    cnt = 0 # 구멍까지 가기위한 수
    while q:
        for _ in range(len(q)):
            rx, ry, bx, by = q.popleft()
            if cnt > 10: # 움직인 횟수가 10회 초과면 -1
                return -1
            if g[rx][ry] == 'O': # 빨간 구슬의 위치가 구멍이면
                return cnt
            for i in range(4):
                nrx, nry = rx, ry
                while True:
                    nrx += dx[i]
                    nry += dy[i]
                    if g[nrx][nry] == '#':
                        nrx -= dx[i]
                        nry -= dy[i]
                        break
                    if g[nrx][nry] == 'O':
                        break
                nbx, nby = bx, by
                
                while True:
                    nbx += dx[i]
                    nby += dy[i]
                    if g[nbx][nby] == '#':
                        nbx -= dx[i]
                        nby -= dy[i]
                        break
                    if g[nbx][nby] == 'O':
                        break
                if g[nbx][nby] == 'O':
                    continue
                if nrx == nbx and nry == nby:
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if (nrx, nry, nbx, nby) not in visit: # 방문해본적이 없는 위치라면 새로 큐에 추가 후 방문 처리
                        q.append((nrx, nry, nbx, nby))
                        visit.append((nrx, nry, nbx, nby))
        cnt += 1
    return -1
print(bfs(rx, ry, bx, by))