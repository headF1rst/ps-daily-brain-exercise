from collections import defaultdict

def solution(weights):
    answer = 0
    pos = [(2, 3), (2, 4), (3, 4), (3, 2), (4, 2), (4, 3)]
    dic = defaultdict(int)
    for weight in weights:
        dic[weight] += 1
    
    for w in dic:
        if dic[w] > 1:
            answer += dic[w] * (dic[w] - 1) // 2
        
        for mp, fp in pos:
            fw = w * mp / fp
            if fw in dic:
                answer += dic[fw] * dic[w]
        dic[w] = 0
    
    return answer
    