def solution(sizes):
    left_max, right_max = 0, 0
    
    for size in sizes:
        size.sort()
        a, b = size
        if a > left_max:
            left_max = a
        if b > right_max:
            right_max = b
        
    return left_max * right_max
    