# 최빈수 구하기

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    student = list(map(int, input().split()))
    r = []
    for i in range(100, -1, -1):
        r.append(student.count(i))
    cnt = r.index(max(r))
    print('#{} {}'.format(test_case, 100-cnt))
    