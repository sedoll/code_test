# 대칭 차집합

# a, b = map(int, input().split())
# setA = set(list(map(int, input().split())))
# setB = set(list(map(int, input().split())))
# r1 = setA - setB
# r2 = setB - setA
# print(len(r1)+len(r2))

a, b = 1, 12
r = 1
for i in range(b, a-1, -1):
    r *= i
print(r)