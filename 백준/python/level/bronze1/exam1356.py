# 유진수

l = list(map(int, input()))
cnt = 0
div = len(l) // 2
while True:
    if len(l) == 1:
        print('NO')
        break
    a = 1
    b = 1
    for i in l[0:div]:
        a *= i
    for i in l[div:]:
        b *= i
    if a == b:
        print('YES')
        break
    elif a<b:
        div = div + (div // 2)
        cnt +=1
    elif a>b:
        div = div - (div // 2)
        cnt+=1
    if cnt >= len(l) // 2:
        print('NO')
        break