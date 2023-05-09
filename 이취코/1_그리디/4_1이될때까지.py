# 1이될때까지
# 둘중에 하나의 연산 수행
# n에서 1을 뺀다
# n을 k로 나눈다

n, k = map(int, input().split())
r = 0
while n > 1:
    if n % k == 0:
        n = n//k
    else:
        n -= 1
    r+=1
print(r)