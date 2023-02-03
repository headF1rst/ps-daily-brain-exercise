n, m = map(int, input().split())
answer = [[i for i in range(n + 1)] for _ in range(n + 1)]
INF = int(1e9)
G = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    G[a][b] = min(G[a][b], c)
    G[b][a] = min(G[b][a], c)

for i in range(1, n + 1):
    G[i][i] = 0
    answer[i][i] = '-'

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if G[i][j] > (G[i][k] + G[k][j]):
                G[i][j] = G[i][k] + G[k][j]
                answer[i][j] = answer[i][k]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(answer[i][j], end=' ')
    print()