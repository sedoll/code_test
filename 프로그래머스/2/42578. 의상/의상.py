# 딕셔너리 value를 list로 받기 위해 사용
from collections import defaultdict

def solution(clothes):
    dic = defaultdict(list)
    answer = 0 # 결과
    p = 1 # 곱셈 연산 저장 변수
    
    # dic에 key, value 저장
    for clothe in clothes:
        dic[clothe[1]].append(clothe[0])
        answer += 1 # 종류가 하나인 경우를 위해 count
        
    # 종류가 하나인 경우에는 한 벌씩만 착용 가능하므로 배제
    if len(dic) > 1:
        # 각 종류마다 경우의수의 곱 - 1
        for key in dic:
            cnt = len(dic[key])+1 
            p *= cnt
        answer = p-1
    return answer