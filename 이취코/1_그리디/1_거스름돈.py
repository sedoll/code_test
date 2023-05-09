# 거스름돈
# 500원, 100원, 50원, 10원 짜리 동전을 최소 개수로 거슬러준다

money = int(input())
l = [500, 100, 50, 10]
r = 0
for i in l:
    d = money // i
    r += d
    money %= i
    print(i, d)
print(r)