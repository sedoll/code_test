T = int(input())
for test_case in range(1, T + 1):
    r = 0
    l = list(map(int, input().split()))
    for i in l:
        if i % 2 != 0:
            r += i
    print(r)