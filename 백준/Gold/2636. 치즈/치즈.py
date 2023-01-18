from collections import deque

n, m = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(n)]
dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]
q = deque([(0, 0)])
G[0][0] = -1
melted, time = 0, 0

def in_boundary(nx, ny):
    return 0 <= nx < n and 0 <= ny < m

def bfs():
    visited = [[False] * m for _ in range(n)]
    cnt = 0
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if in_boundary(nx, ny):
                if G[nx][ny] == 1:
                    G[nx][ny] = 2
                    cnt += 1
                    continue
                if G[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
    return cnt

def melts_all():
    for i in range(n):
        for j in range(m):
            if G[i][j] == 2:
                G[i][j] = 0
                if not q:
                    q.append((i, j))
                    G[i][j] = -1

while True:
    prev = melted
    melted = bfs()
    if melted == 0:
        print(time)
        print(prev)
        break
    melts_all()
    time += 1
