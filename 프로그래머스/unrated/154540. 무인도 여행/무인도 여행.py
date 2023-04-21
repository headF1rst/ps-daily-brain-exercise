from collections import deque

def solution(maps):
    answer = []
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]
    dxs = [1, -1, 0, 0]
    dys = [0, 0, 1, -1]
    q = deque()
    
    def in_boundary(nx, ny):
        return 0 <= nx < n and 0 <= ny < m
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                q.append((i, j))
                visited[i][j] = True
                total = int(maps[i][j])
                while q:
                    x, y = q.popleft()
                    for dx, dy in zip(dxs, dys):
                        nx = x + dx
                        ny = y + dy
                        if in_boundary(nx, ny) and not visited[nx][ny] and maps[nx][ny] != 'X':
                            q.append((nx, ny))
                            visited[nx][ny] = True
                            total += int(maps[nx][ny])
                answer.append(total)
    
    if not answer:
        return [-1]
    else:
        answer.sort()
        return answer