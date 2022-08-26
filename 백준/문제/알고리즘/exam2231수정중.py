#분해합

n = int(input())
t = 0
for i in range(10, 1000001):
    # if n < i:
    #     print(n)
    # else:
    a = i
    t = 0
    t += a
    while a > 0:
        t += a % 10
        a = a // 10
    if t == n:
        break
print(t)