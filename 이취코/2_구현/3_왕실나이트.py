# 왕실의 나이트
# 특정칸에서 나이트가 이동할 수 있는 경우의 수

n = input()
x, y = n[0], n[1]
nMax = 8
r = 0

x = ord(x)-97
y = int(y)-1

dx = [2, -2]
dy = [1, -1]

for i in dx:
    for j in dy:
        r1 = i + x
        r2 = j + y
        if 0 <= r1 < nMax and 0 <= r2 < nMax:
            r += 1

dx = [1, -1]
dy = [2, -2]

for i in dx:
    for j in dy:
        r1 = i + x
        r2 = j + y
        if 0 <= r1 < nMax and 0 <= r2 < nMax:
            r += 1
print(r)