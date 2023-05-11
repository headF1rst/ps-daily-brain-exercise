from collections import defaultdict
def solution(name, yearning, photo):
    answer = []
    dic = defaultdict(int)
    
    for n, y in zip(name, yearning):
        dic[n] = y
        
    for p in photo:
        point = 0
        for n in p:
            point += dic[n]
        
        answer.append(point)
    
    return answer