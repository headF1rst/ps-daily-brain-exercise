from heapq import heappush, heappop
import math

INF = math.inf

def dijk(n, src, dst, G, traps):
    visited = [[False] * (1 << len(traps)) for _ in range(n + 1)]
    pq = [(0, src, 0)]
    
    while pq:
        cost, cur, state = heappop(pq)
        if cur == dst:
            return cost
        
        if not visited[cur][state]:
            visited[cur][state] = True
            trapped = {}
            cur_trapped = False
            
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
                        cur_trapped = True
            
            for next_node in range(1, n + 1):
                if next_node == cur:
                    continue
                next_trapped = True if next_node in trapped else False
                
                if cur_trapped == next_trapped:
                    if G[cur][next_node] != INF:
                        heappush(pq, (cost + G[cur][next_node], next_node, state))
                else:
                    if G[next_node][cur] != INF:
                        heappush(pq, (cost + G[next_node][cur], next_node, state))
                    

def solution(n, start, end, roads, traps):
    G = [[INF] * (n + 1) for _ in range(n + 1)]
    for road in roads:
        a, b, c = road
        G[a][b] = min(G[a][b], c)
    
    return dijk(n, start, end, G, traps)