from collections import deque

def solution(people, limit):
    people.sort()
    people = deque(people)
    answer = 0
    
    while len(people) > 1:
        r = people[0] + people[-1]
        if r <= limit:
            answer += 1
            people.pop()
            people.popleft()
        else:
            answer += 1
            people.pop()
    if len(people) == 1:
        answer += 1
    return answer