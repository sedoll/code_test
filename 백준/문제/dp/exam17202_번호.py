# 핸드폰 번호 궁합
a = list(map(int, input()))
b = list(map(int, input()))

dp = []

for i in range(16):
    if i%2 == 0:
        dp.append(a[i//2])
    else:
        dp.append(b[i//2])

for i in range(16, 2, -1):
    tmp = []
    for j in range(i-1):
        tmp.append((dp[j] + dp[j+1])%10)
    dp = tmp
print(''.join(map(str, dp)))
