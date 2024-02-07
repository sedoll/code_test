def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(i+1):
            if j == 0 :
                triangle[i][0] += triangle[i-1][0]              # 0열끼리 더하기
            elif j == i :
                triangle[i][j] += triangle[i-1][j-1]            # 마지막 열끼리 더하기
            else :
                triangle[i][j] += max(triangle[i-1][j-1],triangle[i-1][j])    # 두 화살표중 더 큰 경우 받아들이기
    answer = max(triangle[-1])
    return answer