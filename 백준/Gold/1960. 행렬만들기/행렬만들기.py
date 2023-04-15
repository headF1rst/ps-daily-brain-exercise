from heapq import heappush, heappop
from collections import deque

n = int(input())
rows = list(map(int, input().split()))
cols = list(map(int, input().split()))
G = [[0] * n for _ in range(n)]
pq = []

def is_valid():
    for j in range(n):
        total = 0
        for i in range(n):
            total += G[i][j]
        if total != cols[j]:
            return False
    return True

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

if is_valid():
    print(1)
    for i in range(n):
        for j in range(n):
            print(G[i][j], end='')
        print()
else:
    print(-1)