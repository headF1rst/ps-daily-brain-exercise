def solution(sequence):
    answer = -1
    total_a, total_b = 0, 0
    a_min, b_min = 0, 0
    pulse = 1
    
    for s in sequence:
        total_a += (s * pulse)
        total_b += (s * -(pulse))
        
        answer = max(answer, total_a - a_min, total_b - b_min)
        
        a_min = min(a_min, total_a)
        b_min = min(b_min, total_b)
    
        pulse *= -1
        
    return answer