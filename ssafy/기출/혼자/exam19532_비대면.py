# 수학은 비대면입니다.

a, b, c, d, e, f = map(int, input().split())

# y
b1 = -(b*d)
c1 = -(c*d)
e1 = e*a
f1 = f*a
y1 = b1+e1
r1 = c1+f1
ry = 0
if y1 != 0 and r1 != 0: 
    ry = r1//y1

# x
a1 = -(b*e)
c1 = -(c*e)
d1 = d*b
f1 = f*b
x1 = a1+d1
r2 = c1+f1
rx = 0
if r2 != 0 and x1 != 0:
    rx = r2//x1

print(rx, ry)