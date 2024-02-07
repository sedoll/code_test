def solution(targets):
    answer = 1
    targets.sort(key=lambda x:x[1])
    e_t = targets[0][1]
    for s, e in targets:
        if s >= e_t:
            answer += 1
            e_t = e
    return answer