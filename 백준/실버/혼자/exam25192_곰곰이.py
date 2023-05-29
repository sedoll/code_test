# 인사성 밝은 곰곰이

import sys
input = sys.stdin.readline

n = int(input()) # 개수
l = set() # 이모티콘 사용한 이름 저장 set
r = 0 # 이모티콘 개수

# n번 반복
for i in range(n):
    s = input().rstrip()
    if s == 'ENTER': # ENTER인 경우 지금까지 사용한 이모티콘 개수 덧셈
        r += len(l)
        l.clear() # set 초기화
        continue
    l.add(s) # set에 값 대입
r += len(l) # 마지막 부분 덧 셈
print(r)