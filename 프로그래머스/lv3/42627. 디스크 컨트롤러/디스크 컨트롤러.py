from heapq import heappush, heappop

def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    pq = []
    
    while i < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heappush(pq, (job[1], job[0]))
        if pq:
            cur = heappop(pq)
            start = now
            now += cur[0]
            answer += (now - cur[1])
            i += 1
        else:
            now += 1
    
    return int(answer / len(jobs))