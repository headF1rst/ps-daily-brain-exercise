def solution(scores):
    answer = 1
    target = scores[0]
    target_score = sum(target)
    scores.sort(key=lambda x: (-x[0], x[1]))
    throughput = 0
    
    for score in scores:
        if target[0] < score[0] and target[1] < score[1]:
            return -1
        if throughput <= score[1]:
            if target_score < score[0] + score[1]:
                answer += 1
            throughput = score[1]
    
    return answer