
n = int(input())
n2 = int(input())

# 하우상좌
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

x, y = 0, 0
dist = 0
r1, r2 = 0 ,0

arr = [[0]*n for _ in range(n)]

for i in range(n*n, 0, -1):
    arr[x][y] = i
    if i == n2:
        r1, r2 = x, y
    x += dx[dist]
    y += dy[dist]
    
    if x < 0 or y < 0 or x >= n or y >= n or arr[x][y] != 0:
        x -= dx[dist]
        y -= dy[dist]
        dist = dist + 1 if dist < 3 else 0
        x += dx[dist]
        y += dy[dist]

for i in range(len(arr)):
    for j in range(len(arr)):
        print(arr[i][j], end=' ')
    print()
print(r1+1, r2+1)