# 삼성 SW 369 

n = int(input())

# def count_digits(n):
#     cnt = 0
#     tmp = n
#     while tmp > 0:
#         r = tmp % 10
#         if r == 3 or r == 6 or r == 9:
#             cnt += 1
#         tmp //= 10
    
#     if cnt > 0:
#         print('-'*cnt, end=' ')
#     else:
#         print(n, end=' ')

# for i in range(1, n+1):
#     count_digits(i)

# n = int(input())

# 백준 17614 369

def digits(n):
    global result
    cnt = 0
    tmp = n
    while tmp > 0:
        r = tmp % 10
        if r == 3 or r == 6 or r == 9:
            cnt += 1
        tmp //= 10
    result += cnt
result = 0
for i in range(1, n+1):
    digits(i)
print(result)