# 듣보잡

n, m = map(int, input().split())
s1 = set()
s2 = set()

for _ in range(n):
    s1.add(input())
    

for _ in range(m):
    s2.add(input())

r = sorted(list(s1 & s2))

print(len(r))
for i in r:
    print(i)