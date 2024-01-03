# 파리퇴치

T = int(input())

for i in range(1, T+1):
    n, m = map(int, input().split())
    l = []
    for _ in range(n):
        l.append(list(map(int, input().split())))
    
    for i in range(n-1):
        c = []
        for j in range(n-1):
            r = 0
            for k in range(m):
                r += l[i+k][j]
            for k in range(n-1):
                r += l[i][j+k]
            c.append(r)
        print(max(c))