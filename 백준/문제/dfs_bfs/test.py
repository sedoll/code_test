n = int(input().rstrip())
m = int(input().rstrip())

l = [[] for _ in range(n+1)]
r = 0
visit = [False] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    l[x].append(y)
    l[y].append(x)
    
for i in range(1, n):
    l[i].sort()

def dfs(g, v, visit):
    global r
    visit[v] = True
    r+=1
    
    for i in g[v]:
        if not visit[i]:
            dfs(g, i, visit)

dfs(l, 1, visit)
print(r-1)