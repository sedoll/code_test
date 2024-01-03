# 시간 0.25초 피보나치 함수 구현
# 직접해결

import sys
input = sys.stdin.readline

n = int(input())

dp = [0, 0] * 41 # 0~40까지의 0, 1 숫자 체크 리스트 선언
dp[0] = [1, 0]
dp[1] = [0, 1]
dp[2] = [1, 1]

for i in range(3, 41): # 0, 1 값 계산, dp bottom_up
    dp[i] = [x+y for x,y in zip(dp[i-2], dp[i-1])]

for i in range(n): # 공백을 기준으로 0, 1 count 출력
    r = ' '.join(map(str, dp[int(input())]))
    print(r)