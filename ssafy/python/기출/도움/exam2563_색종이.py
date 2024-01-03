# 색종이

d = [[0 for i in range(101)] for j in range(101)]

t = int(input())
cnt = 0
for _ in range(t):
    x, y = map(int, input().split())
    
    for i in range(x, x+10):
        for j in range(y, y+10):
            if not d[i][j]:
                d[i][j] = 1
                cnt += 1
print(cnt)