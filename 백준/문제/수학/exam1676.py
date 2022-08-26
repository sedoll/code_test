# 팩토리얼 0의 개수

from math import factorial as fa
n = int(input())
r = fa(n)
cnt = 0
while r % 10 == 0:
    cnt += 1
    r = r // 10
print(cnt)