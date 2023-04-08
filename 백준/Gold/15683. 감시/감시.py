import math
from copy import deepcopy

n, m = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(n)]
cctvs = []
cctv_cnt = 0
INF = math.inf
answer = INF

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]
directions = [[], [[0], [1], [2], [3]], [[0, 2], [1, 3]], [[0, 1], [1, 2], [2, 3], [3, 0]],
              [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]], [[0, 1, 2, 3]]]

for i in range(n):
    for j in range(m):
        if 1 <= G[i][j] <= 5:
            cctvs.append((i, j, G[i][j]))
            cctv_cnt += 1

def in_boundary(nx, ny):
    return 0 <= nx < n and 0 <= ny < m

def watch(x, y, graph, direction):
    for d in direction:
        nx = x
        ny = y
        while True:
            nx += dxs[d]
            ny += dys[d]
            if not in_boundary(nx, ny) or graph[nx][ny] == 6:
                break
            graph[nx][ny] = '#'

def dfs(depth, graph):
    global answer

    if depth == cctv_cnt:
        cnt = 0
        for i in graph:
            cnt += i.count(0)
        answer = min(answer, cnt)
        return

    x, y, num = cctvs[depth]
    copy_graph = deepcopy(graph)
    for direction in directions[num]:
        watch(x, y, copy_graph, direction)
        dfs(depth + 1, copy_graph)
        copy_graph = deepcopy(graph)

dfs(0, G)
print(answer)
