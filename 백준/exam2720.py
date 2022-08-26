#돈계산

n = int(input())
for _ in range(n):
    m = [25, 10, 5, 1]
    k = int(input())
    for i in m:
        print(k // i, end=' ')
        k = k % i
    print()