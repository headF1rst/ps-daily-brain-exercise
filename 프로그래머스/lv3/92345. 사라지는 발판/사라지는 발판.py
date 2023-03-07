def in_boundary(nx, ny):
    return 0 <= nx < n and 0 <= ny < m

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

def solve(x, y, op_x, op_y):
    if visited[x][y]:
        return 0
    ret = 0
    
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if in_boundary(nx, ny) and block[nx][ny] == 1 and not visited[nx][ny]:
            visited[x][y] = True
            val = solve(op_x, op_y, nx, ny) + 1
            visited[x][y] = False
            
            if ret % 2 == 0 and val % 2 == 1:
                ret = val
            elif ret % 2 == 1 and val % 2 == 1:
                ret = min(ret, val)
            elif ret % 2 == 0 and val % 2 == 0:
                ret = max(ret, val)
    return ret

def solution(board, aloc, bloc):
    global n, m, visited, block
    visited = [[False] * 5 for _ in range(5)]
    block = [[0] * 5 for _ in range(5)]
    n = len(board)
    m = len(board[0])
    
    for i in range(n):
        for j in range(m):
            block[i][j] = board[i][j]
            
    return solve(aloc[0], aloc[1], bloc[0], bloc[1])