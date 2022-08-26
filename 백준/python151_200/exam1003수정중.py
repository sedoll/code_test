#피보나치 함수

def fn(n):
    global l
    if n == 0:
        l.append(0)
    elif n == 1:
        l.append(1)
    elif n > 1:
        fn(n-1)
        fn(n-2)

t = int(input())
for _ in range(t):
    l = []
    fn(int(input()))
    print(l.count(0), l.count(1))