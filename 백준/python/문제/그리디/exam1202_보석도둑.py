
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
l = []
bag = []
result = []
for _ in range(n):
    a, b = map(int, input().split())
    l.append((a, b))
    
for _ in range(k):
    bag.append(int(input()))
    
l.sort(key=lambda x: x[1], reverse=True)

for v in bag:
    weight = v
    r = []
    for a, b in l:
        if weight > a:
            r.append(b)
    result.append(max(r))
print(sum(result))