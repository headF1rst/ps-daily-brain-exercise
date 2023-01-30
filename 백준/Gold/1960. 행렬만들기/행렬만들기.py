from collections import deque
from heapq import heappush, heappop

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
        cnt, idx = heappop(pq)
        cnt = -cnt
        G[i][idx] = 1
        q.append((cnt - 1, idx))
    while q:
        cnt, idx = q.popleft()
        heappush(pq, (-cnt, idx))

def is_valid():
    for j in range(n):
        col_sum = 0
        for i in range(n):
            col_sum += G[i][j]
        if col_sum != cols[j]:
            return False
    return True

if is_valid():
    print(1)
    for i in range(n):
        for j in range(n):
            print(G[i][j], end='')
        print()
else:
    print(-1)