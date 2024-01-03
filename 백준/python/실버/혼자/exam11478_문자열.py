# 서로 다른 문자열 개수

n = 1 # 처음 slice 범위
st = input() # 입력 문자열
l = set() # 결과값 저장 set

while n < len(st):
    for i in range(len(st)):
        c = st[i:i+n] # 문자열은 범위 벗어나도 오류 안뜸
        l.add(c)
    n += 1
    
# 결과값 출력
# 원래 입력값도 만들 수 있는 문자열 포함이기에 +1 해줌
print(len(l)+1)