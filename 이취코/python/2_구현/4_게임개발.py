# 게임 개발

n, m = map(int, input().split())

a, b, d = map(int, input().split())

l = []

for _ in range(n):
    l.append(list(map(int, input().split())))

l[a][b] = 2 # 방문위치

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def ewsn():
    global d
    d -= 1
    if d == -1:
        d = 3

cnt = 1
turn = 0
while True:
    ewsn()
    nx = a + dx[d]
    ny = b + dy[d]
    
    if l[nx][ny] == 0:
        l[nx][ny] = 2
        a = nx
        b = ny
        cnt += 1
        turn = 0
        continue
    else:
        turn += 1
    
    if turn == 4:
        nx = a - dx[d]
        ny = b - dy[d]
        
        if l[nx][ny] == 2 or 0:
            a = nx
            b = ny
        else:
            break
        turn = 0
print(cnt)