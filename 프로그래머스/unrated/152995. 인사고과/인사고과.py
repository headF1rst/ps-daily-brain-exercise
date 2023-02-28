def solution(scores):
    target = scores[0]
    target_score = sum(target)
    scores.sort(key=lambda x: (-x[0], x[1]))
    answer = 1
    Max = 0
    Min = int(1e9)
    
    for score in scores:
        if target[0] < score[0] and target[1] < score[1]:
            return -1
        if Max > score[1] and Min > score[0]:
            continue
            
        if target_score < score[0] + score[1]:
            answer += 1
        Max = max(Max, score[1])
        Min = min(Min, score[0])
    
    return answer