#분수 찾기

x = int(input())
col = 1
tot = 1
m, j = 1, 1
while x > tot:
    col += 1
    tot += col
if col % 2 == 1:
    print("/".join([str(tot-x+1), str(col-(tot-x))]))
else:
    print("/".join([str(col-(tot-x)), str(tot-x+1)]))