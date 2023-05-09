# 시각

h = int(input())
m, s = 60, 60
cnt = 0
for j in range(m):
    for k in range(s):
        r = str(j)+str(k)
        if '3' in r:
            cnt += 1
print((cnt * (h+1)) + 2025 if h>=3 else cnt * (h+1))