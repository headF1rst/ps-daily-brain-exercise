def solution(r1, r2):
    y_min, y_max = r1, r2
    total_cnt = 0
    
    for x in range(r2):
        while r2 ** 2 < y_max ** 2 + x ** 2:
            y_max -= 1
        
        while y_min - 1 and r1 ** 2 <= (y_min - 1) ** 2 + x ** 2:
            y_min -= 1
        
        total_cnt += (y_max - y_min + 1)
    
    return total_cnt * 4