from collections import deque

r, c = map(int, input().split())
G = [list(input()) for _ in range(r)]
INF = int(1e9)
fires = [[INF] * c for _ in range(r)]
px, py = 0, 0
answer = -1
q = deque()
dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

for i in range(r):
    for j in range(c):
        if G[i][j] == 'J':
            px, py = i, j
            G[i][j] = '.'
        if G[i][j] == 'F':
            fires[i][j] = 0
            q.append((i, j))

def in_boundary(nx, ny):
    return 0 <= nx < r and 0 <= ny < c

def bfs():
    visited = [[False] * c for _ in range(r)]
    q.append((px, py, 0))
    visited[px][py] = True
    while q:
        x, y, cnt = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if not in_boundary(nx, ny):
                return cnt + 1
            if not visited[nx][ny] and G[nx][ny] != '#' and fires[nx][ny] > cnt + 1:
                q.append((nx, ny, cnt + 1))
                visited[nx][ny] = True
    return -1

while q:
    x, y = q.popleft()
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if in_boundary(nx, ny) and G[nx][ny] == '.':
            if fires[nx][ny] > fires[x][y] + 1:
                fires[nx][ny] = fires[x][y] + 1
                q.append((nx, ny))

answer = bfs()
if answer == -1:
    print("IMPOSSIBLE")
else:
    print(answer)