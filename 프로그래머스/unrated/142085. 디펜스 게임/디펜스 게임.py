from heapq import heappush, heappop

def solution(n, k, enemy):
    answer = 0
    total_enemy = 0
    pq = []
    
    for e in enemy:
        heappush(pq, -e)
        total_enemy += e
        if total_enemy > n:
            if pq and k != 0:
                total_enemy += heappop(pq)
                k -= 1
            else:
                break
        answer += 1
    return answer