def solution(n, words):
    dic = {} # 단어 저장 dic
    answer = [] # 결과값 저장 list
    cnt = 2 # 처음에 한 번 미리 넣기 때문에 +1 추가
    c = 1 # 시작 1 턴
    r = True # 겹치거나 중복된게 있는지 없는 지 확인 변수
    dic[words[0]] = 1 # dic에 처음에 나온 글자 입력
    for i in range(1, len(words)):
        # 턴 횟수 카운트
        if cnt > n:
            c += 1
            cnt = 1
            
        # 끝말일치 비교 변수
        s1 = words[i-1]
        s2 = words[i]
        
        # 새로운 글자 and 끝말 일치
        if dic.get(s2) == None and s1[-1] == s2[0]:
            dic[s2] = 1
            cnt += 1
        # 중복된 글자 or 끝말이 일치하지 않는경우
        else:
            r = False # 일치하지 않는 걸 저장 후 반복문 종료
            break 
    # 잘 못 된게 있으면 번호, 차례 반환
    if not r:
        answer = [cnt, c]
    else: # 없으면 0 ,0 출력
        answer = [0, 0]
    return answer