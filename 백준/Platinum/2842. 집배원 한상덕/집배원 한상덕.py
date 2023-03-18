import math
from collections import deque

n = int(input())
G = [list(input()) for _ in range(n)]
costs = [list(map(int, input().split())) for _ in range(n)]
fatigues = set()
fatigue_cnt = 0
INF = math.inf
answer = INF
s, e = 0, 0

dxs = [1, -1, 0, 0, 1, -1, 1, -1]
dys = [0, 0, 1, -1, 1, -1, -1, 1]

for i in range(n):
    for j in range(n):
        if G[i][j] == 'P':
            sx, sy = i, j
        elif G[i][j] == 'K':
            fatigue_cnt += 1
        fatigues.add(costs[i][j])

len_f = len(fatigues)
fatigues = list(sorted(fatigues))

def in_boundary(nx, ny):
    return 0 <= nx < n and 0 <= ny < n

def bfs(sx, sy):
    visited = [[False] * n for _ in range(n)]
    q = deque([(sx, sy)])
    visited[sx][sy] = True
    cnt = 0
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if in_boundary(nx, ny) and not visited[nx][ny]:
                visited[nx][ny] = True
                if fatigues[s] <= costs[nx][ny] <= fatigues[e]:
                    q.append((nx, ny))
                    if G[nx][ny] == 'K':
                        cnt += 1
    return cnt

while s < len_f:
    cnt = 0
    if fatigues[s] <= costs[sx][sy] <= fatigues[e]:
        cnt = bfs(sx, sy)
    if cnt == fatigue_cnt:
        answer = min(answer, fatigues[e] - fatigues[s])
        s += 1
    elif e + 1 < len_f:
        e += 1
    else:
        break
print(answer)