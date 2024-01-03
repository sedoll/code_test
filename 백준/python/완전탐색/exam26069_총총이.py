# 붙임성 좋은 총총이

s = set() # 춤추는 사람을 넣을 set
n = int(input()) # 입력 개수

for i in range(n):
    a, b = input().split()
    if a == 'ChongChong': # a에 총총이가 있는 경우 넣음
        s.add(a)
    if b == 'ChongChong': # b에 총총이가 있는 경우 넣음
        s.add(b)
    l = list(s)
    
    # 총총이 혹은 춤추는 사람이 a에 있는 경우 b의 사람 추가
    if len(s) >= 1 and l.count(a) == 1:
        s.add(b)
    # 총총이 혹은 춤추는 사람이 b에 있는 경우 a의 사람 추가
    if len(s) >= 1 and l.count(b) == 1:
        s.add(a)

print(len(s)) # 춤추는 사람의 수 출력