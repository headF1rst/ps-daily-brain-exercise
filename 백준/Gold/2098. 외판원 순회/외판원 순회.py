import math

n = int(input())
W = [list(map(int, input().split())) for _ in range(n)]
INF = math.inf
dp = [[INF] * (1 << n) for _ in range(n)]

def dfs(cur, visited):
    if visited == (1 << n) - 1:
        if W[cur][0]:
            return W[cur][0]
        else:
            return INF

    if dp[cur][visited] != INF:
        return dp[cur][visited]
    dp[cur][visited] = int(1e9)

    for i in range(1, n):
        if visited & (1 << i) or not W[cur][i]:
            continue
        dp[cur][visited] = min(dp[cur][visited], dfs(i, visited | (1 << i)) + W[cur][i])
    return dp[cur][visited]

print(dfs(0, 1))
