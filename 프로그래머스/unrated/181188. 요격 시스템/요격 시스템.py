def solution(targets):
    answer = 0
    targets.sort(key=lambda x: x[1])
    
    s, e = 0, 0
    for target in targets:
        if e <= target[0]:
            answer += 1
            e = target[1]
    
    return answer
