from collections import deque

def solution(maps):
    dxs = [1, -1, 0, 0]
    dys = [0, 0, 1, -1]
    n, m = len(maps), len(maps[0])
    to_lavor = 0
    
    def in_boundary(nx, ny):
        return 0 <= nx < n and 0 <= ny < m
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                sx, sy = i, j
    
    q = deque([(sx, sy, 0)])
    flag = False
    visited = [[False] * m for _ in range(n)]
    visited[sx][sy] = True
    while q:
        x, y, cnt = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if in_boundary(nx, ny) and not visited[nx][ny] and maps[nx][ny] != 'X':
                if maps[nx][ny] == 'L':
                    lx, ly = nx, ny
                    to_lavor = cnt + 1
                    flag = True
                    break
                q.append((nx, ny, cnt + 1))
                visited[nx][ny] = True
        if flag:
            break
    
    if not flag:
        return -1
    
    q = deque([(lx, ly, to_lavor)])
    visited = [[False] * m for _ in range(n)]
    visited[lx][ly] = True
    while q:
        x, y, cnt = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if in_boundary(nx, ny) and not visited[nx][ny] and maps[nx][ny] != 'X':
                if maps[nx][ny] == 'E':
                    return cnt + 1
                q.append((nx, ny, cnt + 1))
                visited[nx][ny] = True
    
    return -1
    
                