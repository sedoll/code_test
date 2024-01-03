# 큐
# FIFO
# deque를 이용하지 않고 list를 이용해 구현한 경우

l = [5, 2, 3, 7, -1, 1, 4, -1]
r = []

for i in range(len(l)):
    if l[i] == -1:
        r.pop(0) # 첫번째 인덱스 값 추출
        print('pop  | ', end='')
    else:
        r.append(l[i])
        print('push | ', end='')
    print('{} 번째 queue 결과'.format(i+1), r)