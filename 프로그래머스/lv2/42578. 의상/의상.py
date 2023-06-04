from collections import defaultdict

def solution(clothes):
    answer = 1
    dic = defaultdict(int)
    
    for cloth in clothes:
        _, k = cloth
        dic[k] += 1
    
    for num in dic.values():
        answer *= (num + 1)
    
    return answer - 1