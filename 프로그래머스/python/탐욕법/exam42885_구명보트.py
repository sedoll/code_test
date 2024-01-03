people = [70, 50, 80, 50]
limit = 100

answer = 0
r = 0
people.sort()
while len(people) > -1:
    v = people.pop()
    r += v
    if r > limit:
        answer += 1
        r = 0
        people.append(v)
    if len(people) == 0:
        answer += 1
        break
print(answer)