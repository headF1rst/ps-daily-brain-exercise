dic = {'N': 0, 'S': 1, 'E': 2, 'W': 3}

def solution(park, routes):
    n, m = len(park), len(park[0])
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, 1, -1]
    
    for i in range(n):
        for j in range(m):
            if park[i][j] == 'S':
                cx, cy = i, j
    
    def in_boundary(nx, ny):
        return 0 <= nx < n and 0 <= ny < m
    
    for route in routes:
        cmd, move = route.split()
        move = int(move)
        
        nx, ny = cx, cy
        for _ in range(move):
            nx += dxs[dic[cmd]]
            ny += dys[dic[cmd]]
            if not in_boundary(nx, ny) or park[nx][ny] == 'X':
                break
        else:
            cx, cy = nx, ny
        
    return [cx, cy]
            
    
    