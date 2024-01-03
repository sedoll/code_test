# 대지

n = int(input())
x = []
y = []

for i in range(n):
    nx, ny = map(int, input().split())
    x.append(nx)
    y.append(ny)

r = (max(x)-min(x)) * (max(y)-min(y))
print(r)