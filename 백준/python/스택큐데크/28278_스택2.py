# 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
# 명령은 총 다섯 가지이다.

# 1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
# 2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
# 3: 스택에 들어있는 정수의 개수를 출력한다.
# 4: 스택이 비어있으면 1, 아니면 0을 출력한다.
# 5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.

import sys
input = sys.stdin.readline

n = int(input())
s = []
for _ in range(n):
    n2 = list(map(int, input().split()))
    i = n2[0]
    if i == 1:
        s.append(n2[1])
    elif i == 2:
        if len(s) == 0:
            print(-1)
        else:
            print(s.pop())
    elif i == 3:
        print(len(s))
    elif i == 4:
        print(1 if len(s) == 0 else 0)
    elif i == 5:
        print(s[-1] if len(s) > 0 else -1)