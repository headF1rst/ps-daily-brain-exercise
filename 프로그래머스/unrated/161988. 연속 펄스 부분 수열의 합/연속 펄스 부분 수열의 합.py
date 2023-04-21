def solution(sequence):
    total_a, total_b = 0, 0
    min_a, min_b = 0, 0
    pulse = 1
    answer = -1
    
    for s in sequence:
        total_a += (s * pulse)
        total_b += (s * -(pulse))
        
        answer = max(answer, total_a - min_a, total_b - min_b)
        
        min_a = min(min_a, total_a)
        min_b = min(min_b, total_b)
        pulse *= -1
    
    return answer