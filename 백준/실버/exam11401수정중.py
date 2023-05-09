# 이항 계수 3

n, k = map(int, input().split())

# 조합을 이용한 것과 값이 똑같아서 해봤는데 실패
def fn(n, k):
    r1, r2 = 1, 1
    if k < 0 or k > n:
        return 0
    elif k == 0 or k == n:
        return 1
    elif k == 1 or k == n-1:
        return n
    else:
        for i in range(k, 0, -1):
            r1 *= n - (k-i)
            r2 *= i
        return r1//r2
    
print(fn(n, k))