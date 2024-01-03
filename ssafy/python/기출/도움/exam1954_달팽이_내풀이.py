# 달팽이

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    snail = [[0]*n for _ in range(n)]
    x, y = 0, 0
    dist = 0
    
    for i in range(1, n*n+1):
        snail[x][y] = i
        x += dx[dist]
        y += dy[dist]
        
        if x<0 or y<0 or x>=n or y>=n or snail[x][y] != 0:
            x -= dx[dist]
            y -= dy[dist]
            dist = dist + 1 if dist < 3 else 0
            x += dx[dist]
            y += dy[dist]
    print('#{}'.format(tc))
    for i in range(len(snail)):
        for j in range(len(snail)):
            print(snail[i][j], end=' ')
        print()