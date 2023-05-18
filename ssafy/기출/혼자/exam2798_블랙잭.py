#브루트포스

n, m = map(int, input().split())
l = list(map(int, input().split()))
r = []
for i in range(len(l)):
    for j in range(len(l)):
        for k in range(len(l)):
            if i != j and j != k and i != k:
                v = l[i] + l[j] + l[k]
                if v <= m:
                    r.append(v)
print(max(r))