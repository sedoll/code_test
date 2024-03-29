# 방 번호

# 0~9 까지 cnt 넣을 리스트
cnt = [0] * 10

# 입력
n = int(input())

# 0 이 될 때까지 반복
while n > 0:
    r = n%10 # 나온 수 확인
    n //= 10 # 나온 수 없앰
    cnt[r] += 1 # 나온 수 카운트

# 6과 9를 같이 카운트 하기 위한 연산
r = cnt[6] + cnt[9] 
r = (r//2) + (r%2)
cnt[6], cnt[9] = r, r

# 카운트 된 것중 최대값 출력
print(max(cnt))