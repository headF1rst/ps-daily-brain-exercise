from heapq import heappush, heappop
from collections import deque

n = int(input())
rows = list(map(int, input().split()))
cols = list(map(int, input().split()))
G = [[0] * n for _ in range(n)]

pq = []
for i in range(n):
    heappush(pq, (-cols[i], i))

for i in range(n):
    q = deque()
    for j in range(rows[i]):
        a, b = heappop(pq)
        a = -a
        G[i][b] = 1
        q.append((a - 1, b))

    while q:
        a, b = q.popleft()
        heappush(pq, (-a, b))

def is_valid():
    for j in range(n):
        col_sum = 0
        for i in range(n):
            col_sum += G[i][j]
        if col_sum != cols[j]:
            return False
    return True

if not is_valid():
    print(-1)
else:
    print(1)
    for i in range(n):
        for j in range(n):
            print(G[i][j], end='')
        print()