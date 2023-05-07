# 시험감독

import math
n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
r = 0
for i in range(n):
    a[i] -= b
    r += 1
    if a[i] >= 1:
        r += math.ceil(a[i]/c)
print(r)