def solution(s):
    answer = ''
    l = s.split(" ")
    for i in l:
        if i==" ":
            i += " "
            continue
        i = i.lower()
        if i.isalpha:
            i = i.capitalize()
        answer += i+" "
    return answer[:-1]