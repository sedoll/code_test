def solution(elements):
    answer = 0
    s = set(elements)
    size = len(elements)
    l = 1
    while l < size:
        for i in range(size):
            if l+i < size:
                v = sum(elements[i:l+i])
                s.add(v)
            else:
                v = sum(elements[i:]) + sum(elements[:(l+i)%size])
                s.add(v)
        l+=1
    s = list(s)
    answer = len(s)
    return answer+1