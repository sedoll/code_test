# 상하좌우

n = int(input())
x, y = 0, 0

l = list(map(str, input().split()))

for i in l:
    if i == 'R' and y < n-1:
        y += 1
    elif i == 'L' and y > 1:
        y -= 1
    elif i == 'U' and x > 1:
        x -= 1
    elif i == 'D' and x < n-1:
        x += 1
print(x+1, y+1)