from math import factorial

T = int(input())

for tc in (1, T+1):
    n = int(input())
    print('#{}'.format(tc))
    for i in range(n):
        factorial(tc-1)//(factorial(i)*factorial(tc-i-1))