# 2*n타일
# 직접해결
# 규칙성이 피보나치와 동일
# 2 = 2
# 9 = 55

import sys
input = sys.stdin.readline

n = int(input())
dp = [1] * 1001
for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n]%10007)