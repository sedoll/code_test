def solution(n):
    dp = [0] * 2001
    answer = 0
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    answer = dp[n] % 1234567
    return answer