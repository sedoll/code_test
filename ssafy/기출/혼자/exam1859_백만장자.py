# 백만장자

t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    d = l[-1]
    r = 0
    for i in range(n-2, -1, -1):
        if d > l[i]:
            r += d - l[i]
        elif d < l[i]:
            d = l[i]
    print(r)