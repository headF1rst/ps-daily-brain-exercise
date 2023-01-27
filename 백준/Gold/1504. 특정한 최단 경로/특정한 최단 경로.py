import math
from heapq import heappush, heappop
import math

n, e = map(int, input().split())
INF = math.inf
G = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    G[a][b] = c
    G[b][a] = c
v1, v2 = map(int, input().split())

def dijk(source, target1, target2):
    dist = [INF] * (n + 1)
    dist[source] = 0
    pq = [(0, source)]
    while pq:
        cost, cur = heappop(pq)
        for i in range(1, n + 1):
            next_cost = dist[cur] + G[cur][i]
            if next_cost < dist[i]:
                dist[i] = next_cost
                heappush(pq, (next_cost, i))
    return dist[target1], dist[target2]

a, d = dijk(1, v1, v2)
b, f = dijk(v1, v2, n)
c, e = dijk(v2, n, v1)
answer = min(a + b + c, d + e + f)
if answer == INF:
    print(-1)
else:
    print(answer)