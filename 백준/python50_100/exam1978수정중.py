#소수 찾기
cnt = 0
def pn(num):
    global cnt
    if num != 1:
        for j in (2, num):
            if i % j == 0:
                cnt += 1            
run = int(input())
n = list(map(int, input().split()))
if len(n) == run:
    for i in n:
        pn(i)
print(cnt)