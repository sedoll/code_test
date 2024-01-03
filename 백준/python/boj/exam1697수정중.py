#숨바꼭질
n, k = map(int, input().split())
a, b = 0, 0
t = 0
temp = k % n
temp2 = k // n
if n - temp > temp:
    r = temp2 -1 + temp
else:
    r = temp2 + (n - temp)
print(r)