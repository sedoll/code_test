def solution(s):
    sum = 0
    cnt = 0
    
    while True:
        one = 0
        zero = 0
        cnt += 1
        for i in s:
            if i == '1':
                one += 1
            else:
                zero += 1
        sum += zero
        
        s = bin(one)
        s = s[2:]
        if '1' == str(s):
            break
        
    return [cnt, sum]