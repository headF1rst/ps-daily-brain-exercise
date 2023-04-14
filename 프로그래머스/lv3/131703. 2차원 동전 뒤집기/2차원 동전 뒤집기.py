import math

def flip_col(G, col):
    row = len(G)
    for i in range(row):
        if G[i][col] == 0:
            G[i][col] = 1
        else:
            G[i][col] = 0

def solution(beginning, target):
    n, m = len(beginning), len(beginning[0])
    flipped = [[] for _ in range(n)]
    INF = math.inf
    answer = INF
    
    for i in range(n):
        for j in range(m):
            flipped[i].append(abs(1 - beginning[i][j]))
    
    for unit in range(1 << n):
        flipped_rows = []
        flipped_cnt = 0
        for i in range(n):
            bit = 1 << i
            if unit & bit:
                flipped_rows.append(flipped[i][:])
                flipped_cnt += 1
            else:
                flipped_rows.append(beginning[i][:])
        
        for j in range(m):
            cur_col = []
            tar_col = []
            for i in range(n):
                cur_col.append(flipped_rows[i][j])
                tar_col.append(target[i][j])
            if cur_col != tar_col:
                flip_col(flipped_rows, j)
                flipped_cnt += 1
            
        if flipped_rows == target:
            answer = min(answer, flipped_cnt)
        
    if answer == INF:
        return -1
    return answer