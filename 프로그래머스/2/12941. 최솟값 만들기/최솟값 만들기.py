def solution(A,B):
    dp = [0] * 1001
    
    A.sort(reverse=True)
    B.sort()
    dp[0] = A[0] * B[0]
    for i in range(1, len(A)):
        dp[i] = A[i] * B[i] + dp[i-1]

    return dp[len(A)-1]