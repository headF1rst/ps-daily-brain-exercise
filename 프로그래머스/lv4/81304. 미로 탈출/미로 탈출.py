from heapq import heappush, heappop
import math
INF = math.inf

def dijk(n, G, src, dst, traps):
    pq = [(0, src, 0)]
    visited = [[False] * (1 << len(traps)) for _ in range(n + 1)]
    
    while pq:
        c, cur, state = heappop(pq)
        if cur == dst:
            return c
        if not visited[cur][state]:
            visited[cur][state] = True
            curTrapped = False
            trapped = {}
            for i in range(len(traps)):
                bit = 1 << i
                if state & bit:
                    if traps[i] == cur:
                        state &= ~bit
                    else:
                        trapped[traps[i]] = True
                else:
                    if traps[i] == cur:
                        state |= bit
                        trapped[traps[i]] = True
                        curTrapped = True
            
            for next_node in range(1, n + 1):
                if next_node == cur:
                    continue
                next_trapped = True if next_node in trapped else False
                if curTrapped == next_trapped:
                    if G[cur][next_node] != INF:
                        heappush(pq, (c + G[cur][next_node], next_node, state))
                else:
                    if G[next_node][cur] != INF:
                        heappush(pq, (c + G[next_node][cur], next_node, state))
                    

def solution(n, start, end, roads, traps):
    answer = 0
    G = [[INF] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        G[i][i] = 0
    
    for road in roads:
        a, b, c = road
        if c < G[a][b]:
            G[a][b] = c
    return dijk(n, G, start, end, traps)