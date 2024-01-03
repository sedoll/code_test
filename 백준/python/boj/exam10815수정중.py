#숫자카드 맞추기
import sys
input = sys.stdin.readline

n, nl = int(input()), list(map(int, input().split()))
m, ml = int(input()), list(map(int, input().split()))
for i in ml:
    cnt = 0
    for j in nl:
        if i == j:
            cnt = 1
            break
    print(cnt)