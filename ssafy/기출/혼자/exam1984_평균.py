T = int(input())

for test_case in range(1, T+1):
    q = sorted(list(map(int, input().split())))
    q.remove(q[0])
    q.remove(q[-1])
    r = round(sum(q)/8)
    print('#{} {}'.format(test_case, r))