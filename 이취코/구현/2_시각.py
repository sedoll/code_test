# 시각

h = int(input())
m, s = 60, 60
cnt = 0
for i in range(h+1):
    for j in range(m):
        for k in range(s):
            r = str(i)+str(j)+str(k)
            if '3' in r:
                cnt += 1
print(cnt)
