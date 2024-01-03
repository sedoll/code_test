run = True
while run:
    l = list(map(int, input().split()))
    l.sort()
    if l[0] == l[1] == l[2] == 0:
        break
    if l[2] >= l[1] + l[0]:
        print('Invalid')
    elif l[0] == l[1] == l[2]:
        print('Equilateral')
    elif l[0] == l[1] or l[1] == l[2] or l[0] == l[2]:
        print('Isosceles')
    else:
        print('Scalene')