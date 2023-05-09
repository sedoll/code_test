# 재귀함수
# 자신을 계속 호출하는 함수

def fn(v):
    global n, r
    if(v == n+1):
        print(r)
        return
    r *= v
    v += 1
    fn(v)

n = int(input('팩토리얼 : '))
r = 1
fn(1)