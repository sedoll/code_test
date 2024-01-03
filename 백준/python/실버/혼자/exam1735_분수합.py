x1, x2 = map(int, input().split())
y1, y2 = map(int, input().split())
r2 = x2*y2
r1 = (x1*y2) + (y1*x2)
l = []

# 최대공약수
def gcd(a, b):
    while (b != 0):
        temp = a % b
        a = b
        b = temp
    return abs(a)

# 기약분수 만들기
def reduce(bunja, bunmo):
    if (bunmo == 0): # 분모가 0일 경우에 에러 반환
        bunja = 0
        bunmo = 0
        return [bunja, bunmo]
    gcd_result = gcd(bunja, bunmo)
    bunja = bunja // gcd_result
    bunmo = bunmo // gcd_result
    return [bunja, bunmo]
l = reduce(r1, r2)
for i in l:
    print(i, end=' ')

# 더 좋은 풀이
# x1, x2 = map(int, input().split())
# y1, y2 = map(int, input().split())
# r2 = x2*y2
# r1 = (x1*y2) + (y1*x2)

# # 기약분수 만들기
# def reduce(bunja, bunmo):
#     if bunja%bunmo == 0:
#         return bunmo
#     return reduce(bunmo, bunja%bunmo)

# k = reduce(r1, r2)
# print(r1//k, r2//k)