# 큰 수의 법칙
# 연속으로 입력된 수를 합하여 제일 큰 수를 만들어라

n, m, k = map(int, input().split())

l = list(map(int, input().split()))
l.sort() # 정렬
cnt = 0 # k 번 반복
r = 0 # 결과값

for _ in range(m):
    if cnt == k:
        r += l[-2] # 두 번째로 큰 값
        cnt = 0 # 반복횟수 초기화
    else:
        r += l[-1] # 제일 큰 값
        cnt += 1
print(r)