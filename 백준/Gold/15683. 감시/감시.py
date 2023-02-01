from copy import deepcopy

n, m = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(n)]
direction = [[], [[0], [1], [2], [3]], [[0, 2], [1, 3]], [[0, 1], [1, 2], [2, 3], [3, 0]],
             [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]], [[0, 1, 2, 3]]]
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]
cctvs = []
cctv_cnt = 0
answer = int(1e9)

for i in range(n):
    for j in range(m):
        if 0 < G[i][j] < 6:
            cctvs.append((i, j, G[i][j]))
            cctv_cnt += 1

def in_boundary(nx, ny):
    return 0 <= nx < n and 0 <= ny < m

def watch(x, y, direct, graph):
    for d in direct:
        nx, ny = x, y
        while True:
            nx += dxs[d]
            ny += dys[d]
            if not in_boundary(nx, ny) or graph[nx][ny] == 6:
                break
            if graph[nx][ny] == 0:
                graph[nx][ny] = '#'

def dfs(depth, graph):
    global answer
    if depth == cctv_cnt:
        c = 0
        for i in graph:
            c += i.count(0)
        answer = min(answer, c)
        return

    x, y, num = cctvs[depth]
    tmp_G = deepcopy(graph)
    for direct in direction[num]:
        watch(x, y, direct, tmp_G)
        dfs(depth + 1, tmp_G)
        tmp_G = deepcopy(graph)

dfs(0, G)
print(answer)