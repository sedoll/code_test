# 좌표 압축

n = int(input())
l = list(map(int, input().split()))
s = set(l)
s = sorted(s)
d = {}
r = 0
for i in s:
    d[i] = r
    r+=1
for i in l:
    print(d.get(i), end=' ')