from heapq import heappop, heappush
from copy import deepcopy

def solution(operations):
    pq = []
    is_desc = False
    
    for operation in operations:
        cmd, num = operation.split()
        num = int(num)
        if cmd == 'I':
            if is_desc:
                heappush(pq, -num)
            else:
                heappush(pq, num)
            continue
        if num == -1 and pq:
            if is_desc:
                tmp = deepcopy(pq)
                pq = []
                for t in tmp:
                    heappush(pq, -t)
            heappop(pq)
            is_desc = False
            continue
        if pq:
            if not is_desc:
                tmp = deepcopy(pq)
                pq = []
                for t in tmp:
                    heappush(pq, -t)
            heappop(pq)
            is_desc = True
    
    if not pq:
        return [0, 0]
    if is_desc:
        b = -heappop(pq)
        tmp = deepcopy(pq)
        pq = []
        for t in tmp:
            heappush(pq, t)
        a = heappop(pq)
        return [b, a]
    else:
        a = heappop(pq)
        tmp = deepcopy(pq)
        pq = []
        for t in tmp:
            heappush(pq, -t)
        b = -heappop(pq)
        return [b, a]
    