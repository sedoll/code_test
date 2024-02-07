def solution(brown, yellow):
    answer = []
    n = brown+yellow
    div = []
    
    # 약수 찾기
    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            div.append(i) 
            if ( (i**2) != n) : 
                div.append(n // i)
    div.sort()
    
    # 가로, 세로 크기 구하기
    i = len(div)//2 # 약수의 중앙값 산출
    if len(div) % 2 == 0: # 약수의 개수가 짝 수 인 경우
        if (div[i]-2) * (div[i-1]-2) == yellow: # 가로, 세로 크기가 중앙에 있으면
            answer = [div[i], div[i-1]] # 가로, 세로
        else: # 가로, 세로 크기가 중앙에 없으면 비교하며 찾는다.
            for j in range(i):
                if ((div[j]-2) * (div[-j-1]-2)) == yellow:
                    answer = [div[-j-1], div[j]] # 가로, 세로
                    break
    else: # 약수의 개수가 홀 수 인 경우 중앙 값 출력
        answer = [div[i], div[i]]
    return answer