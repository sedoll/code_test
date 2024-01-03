# dfs
# 재귀함수 이용

g = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visit = [False] * 9

def dfs(g, v, visit): # 연결, 노드, 방문 확인
    # 노드 방문 처리
    visit[v] = True
    print(v, end=' ')
    
    for i in g[v]:
        if not visit[i]:
            dfs(g, i, visit)

dfs(g, 1, visit)