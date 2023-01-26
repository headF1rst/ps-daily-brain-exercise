from collections import deque

SOURCE = 0
SINK = 201
INF = int(1e9)

def bfs(flow):
    parent = [-1] * 202
    q = deque([SOURCE])
    parent[SOURCE] = SOURCE
    while q:
        item = q.popleft()
        for i in range(202):
            if parent[i] == -1 and G[item][i] - flow[item][i]:
                q.append(i)
                parent[i] = item
    return parent

def max_flow():
    flow = [[0] * 202 for _ in range(202)]
    result = 0
    while True:
        parent = bfs(flow)
        if parent[SINK] == -1:
            return result
        node = SINK
        m = INF
        while node != SOURCE:
            m = min(m, G[parent[node]][node] - flow[parent[node]][node])
            node = parent[node]
        result += m

        node = SINK
        while node != SOURCE:
            flow[parent[node]][node] += m
            flow[node][parent[node]] -= m
            node = parent[node]

n, m = map(int, input().split())
G = [[0] * 202 for _ in range(202)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a][b + 100] += 1
for i in range(1, 101):
    G[SOURCE][i] += 1
    G[i + 100][SINK] += 1
print(max_flow())