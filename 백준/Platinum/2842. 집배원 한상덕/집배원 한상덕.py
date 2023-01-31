import math
from collections import deque

n = int(input())
G = [list(input()) for _ in range(n)]
h = [list(map(int, input().split())) for _ in range(n)]
houses = 0
fatigue = set()
INF = math.inf
answer = INF
dxs = [1, -1, 0, 0, 1, -1, 1, -1]
dys = [0, 0, 1, -1, -1, 1, 1, -1]

for i in range(n):
    for j in range(n):
        if G[i][j] == 'P':
            sx, sy = i, j
        if G[i][j] == 'K':
            houses += 1
        fatigue.add(h[i][j])

fatigue = list(sorted(fatigue))
s, e = 0, 0
len_f = len(fatigue)

def in_boundary(nx, ny):
    return 0 <= nx < n and 0 <= ny < n

def bfs(i, j):
    visited = [[False] * n for _ in range(n)]
    visited[i][j] = True
    q = deque([(i, j)])
    cnt = 0
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if in_boundary(nx, ny) and not visited[nx][ny]:
                if fatigue[s] <= h[nx][ny] <= fatigue[e]:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    if G[nx][ny] == 'K':
                        cnt += 1
    return cnt

while s < len_f:
    cnt = 0
    if fatigue[s] <= h[sx][sy] <= fatigue[e]:
        cnt = bfs(sx, sy)

    if cnt == houses:
        answer = min(answer, fatigue[e] - fatigue[s])
        s += 1
    elif e + 1 < len_f:
        e += 1
    else:
        break

print(answer)