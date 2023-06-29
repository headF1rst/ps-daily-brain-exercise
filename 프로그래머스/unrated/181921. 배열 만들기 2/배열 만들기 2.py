from heapq import heappush, heappop

def solution(l, r):
    answer = []
    for i in range(l, r + 1):
        if i % 5 != 0:
            continue
        
        str_i = str(i)
        len_str = len(str_i)
        flag = True
        for idx in range(len_str):
            if str_i[idx] != '5' and str_i[idx] != '0':
                flag = False
                break
        if flag:
            answer.append(i)
    
    if not answer:
        answer.append(-1)
    return answer