#숫자고르기
import sys

n = int(sys.stdin.readline())
l = [x for x in range(1, n+1)]
l2 = []
r = []

for i in range(n):
    k = int(sys.stdin.readline())
    l2.append(k)
setL = set(l2)
l2 = list(setL)

for i in l2:
    for j in l:
        if i==j and r not in i:
            r.append(i)
print(len(r))
print(list(r))