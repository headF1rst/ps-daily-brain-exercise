from heapq import heappop, heappush

def solution(scoville, K):
    pq = []
    answer = 0
    
    for s in scoville:
        heappush(pq, s)
    
    if pq[0] >= K:
        return 0
    
    while len(pq) >= 2:
        a = heappop(pq)
        b = heappop(pq)
        
        if a >= K:
            return answer
        
        point = a + (b * 2)
        answer += 1
        heappush(pq, point)
    
    if pq[0] >= K:
        return answer
    
    return -1