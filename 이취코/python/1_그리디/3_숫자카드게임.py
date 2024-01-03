# 각각의 행에서 제일 작은 숫자를 뽑고
# 그 중에서 제일 큰 숫자를 찾아라

n, m = map(int, input().split())
l = []
r = []

# 리스트에 값을 넣고
# 입력된 행의 최솟값을 결과 리스트에 저장
for i in range(n):
    l.append(list(map(int, input().split())))
    r.append(min(l[i]))
    
# 결과 리스트에서 제일 큰 값을 출력
print(max(r))