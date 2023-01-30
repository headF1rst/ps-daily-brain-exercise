import sys
input = sys.stdin.readline

n, m = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
Max = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(r, c, idx, total):
    global Max
    if idx == 3:
        Max = max(Max, total)
        return

    for i in range(4):
        ny = r + dy[i]
        nx = c + dx[i]
        if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
            if idx == 1:
                visited[ny][nx] = True
                dfs(r, c, idx + 1, total + G[ny][nx])
                visited[ny][nx] = False

            visited[ny][nx] = True
            dfs(ny, nx, idx + 1, total + G[ny][nx])
            visited[ny][nx] = False

for r in range(n):
    for c in range(m):
        visited[r][c] = True
        dfs(r, c, 0, G[r][c])
        visited[r][c] = False

print(Max)