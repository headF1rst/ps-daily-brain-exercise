from collections import deque

n = int(input())
G = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    G[i] = list(map(int, input().split()))
m = int(input())
starts = list(map(int, input().split()))
answer = [-1] * (n + 1)
turn = [0] * (n + 1)
q = deque()
t = 0

for start in starts:
    answer[start] = 0
    q.append(start)

for i in range(1, n + 1):
    turn[i] += len(G[i]) // 2

while q:
    cur = q.popleft()
    for next_node in G[cur]:
        turn[next_node] -= 1
        if answer[next_node] == -1 and turn[next_node] <= 0:
            answer[next_node] = answer[cur] + 1
            q.append(next_node)

for i in range(1, n + 1):
    print(answer[i], end=' ')