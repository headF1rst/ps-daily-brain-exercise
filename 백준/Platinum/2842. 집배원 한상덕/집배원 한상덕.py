import math
from collections import deque

n = int(input())
G = [list(input()) for _ in range(n)]
h = [list(map(int, input().split())) for _ in range(n)]
INF = math.inf
answer = INF
dxs = [1, -1, 0, 0, 1, -1, 1, -1]
dys = [0, 0, 1, -1, 1, -1, -1, 1]
fatigues = set()
s, e = 0, 0
houses = 0

for i in range(n):
    for j in range(n):
        if G[i][j] == 'P':
            sx, sy = i, j
        if G[i][j] == 'K':
            houses += 1
        fatigues.add(h[i][j])

fatigues = sorted(fatigues)
len_f = len(fatigues)

def in_boundary(nx, ny):
    return 0 <= nx < n and 0 <= ny < n

def bfs(i, j):
    q = deque([(i, j)])
    visited = [[False] * n for _ in range(n)]
    visited[i][j] = True
    cnt = 0
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if in_boundary(nx, ny) and not visited[nx][ny]:
                if fatigues[s] <= h[nx][ny] <= fatigues[e]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    if G[nx][ny] == 'K':
                        cnt += 1
    return cnt


while s < len_f:
    cnt = 0
    if fatigues[s] <= h[sx][sy] <= fatigues[e]:
        cnt = bfs(sx, sy)
    if cnt == houses:
        answer = min(answer, fatigues[e] - fatigues[s])
        s += 1
    elif e + 1 < len_f:
        e += 1
    else:
        break

print(answer)