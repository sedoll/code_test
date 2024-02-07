def solution(s):
    # 못 품
    answer = True
    stack = []
    
    for i in s:
        if i == '(':
            stack.append(i)
        elif len(stack) and i == ')':
            stack.pop()
        else:
            return False

    return False if len(stack) else True