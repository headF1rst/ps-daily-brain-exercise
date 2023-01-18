from collections import deque

r, c = map(int, input().split())
G = [list(input()) for _ in range(r)]
q = deque()
INF = int(1e9)
fires = [[INF] * c for _ in range(r)]
px, py = 0, 0
dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

def in_boundary(nx, ny):
    return 0 <= nx < r and 0 <= ny < c

def bfs():
    q = deque([(px, py, 0)])
    visited = [[False] * c for _ in range(r)]
    visited[px][py] = True
    while q:
        x, y, cnt = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if not in_boundary(nx, ny):
                return cnt + 1
            if G[nx][ny] == '.' and not visited[nx][ny] and fires[nx][ny] > cnt + 1:
                q.append((nx, ny, cnt + 1))
                visited[nx][ny] = True
    return - 1

for i in range(r):
    for j in range(c):
        if G[i][j] == 'J':
            px, py = i, j
            G[i][j] = '.'
        if G[i][j] == 'F':
            q.append((i, j))
            fires[i][j] = 0

while q:
    x, y = q.popleft()
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if in_boundary(nx, ny) and G[nx][ny] != '#':
            if fires[nx][ny] > fires[x][y] + 1:
                fires[nx][ny] = fires[x][y] + 1
                q.append((nx, ny))

answer = bfs()
if answer == -1:
    print('IMPOSSIBLE')
else:
    print(answer)
