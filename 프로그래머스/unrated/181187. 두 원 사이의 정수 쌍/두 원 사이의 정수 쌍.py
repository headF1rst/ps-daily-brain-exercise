def solution(r1, r2):
    answer = 0
    y_min, y_max = r1, r2
    for x in range(r2):
        while r2 ** 2 < y_max ** 2 + x ** 2:
            y_max -= 1
        
        while y_min - 1 and r1 ** 2 <= (y_min - 1) ** 2 + x ** 2:
            y_min -= 1
        
        answer += y_max - y_min + 1
    return answer * 4