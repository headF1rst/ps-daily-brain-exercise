import math

def flipp(G, j):
    n = len(G)
    for i in range(n):
        G[i][j] = 1 - G[i][j]

def solution(beginning, target):
    n, m = len(beginning), len(beginning[0])
    INF = math.inf
    answer = INF
    flipped = [[] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            flipped[i].append(1 - beginning[i][j])
    
    for check in range(1 << n):
        flipped_rows = []
        flipped_cnt = 0
        for i in range(n):
            on = 1 << i
            if check & on:
                flipped_rows.append(flipped[i][:])
                flipped_cnt += 1
            else:
                flipped_rows.append(beginning[i][:])
        
        for j in range(m):
            cur_col = []
            target_col = []
            for i in range(n):
                cur_col.append(flipped_rows[i][j])
                target_col.append(target[i][j])
            
            if cur_col != target_col:
                flipp(flipped_rows, j)
                flipped_cnt += 1
        
        if target == flipped_rows:
            answer = min(answer, flipped_cnt)
    
    if answer == INF:
        return -1
    return answer
            