# 스택
# FILO

# -1 위치가 pop
l = [5, 2, 3, 7, -1, 1, 4, -1]
r = []

for i in range(len(l)):
    if l[i] == -1:
        r.pop() # 맨 뒤의 인덱스 값 추출
        print('pop  | ', end='')
    else:
        r.append(l[i])
        print('push | ', end='')
    print('{} 번째 stack 결과'.format(i+1), r)