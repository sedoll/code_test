

dp = [0] * 301
stair = [0] * 301
n = int(input())

for i in range(n):
    stair[i] = int(input())

if n >= 1:
    dp[0] = stair[0]
if n>=2:
    dp[1] = max(stair[1]+stair[0], stair[1])
if n>=3:
    dp[2] = max(stair[2]+stair[0], stair[1]+stair[2])

for i in range(3, n+1):
    dp[i] = max(dp[i-2]+stair[i], stair[i-1]+stair[i]+dp[i-3])

print(dp[n-1])