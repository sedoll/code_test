# 나는야 포켓몬 마스터 이다솜

n, m = map(int, input().split())
d = {}
d2 = {}
for i in range(1, n+1):
    s = input()
    d[s] = i
    d2[i] = s

for _ in range(m):
    s = input()
    if s.isalpha():
        print(d.get(s))
    else:
        print(d2.get(int(s)))