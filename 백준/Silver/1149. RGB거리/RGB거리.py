n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * 3 for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(3):
        a, b = (j + 1) % 3, (j + 2) % 3
        dp[i][j] = cost[i - 1][j] + min(dp[i - 1][a], dp[i - 1][b])

print(min(dp[n]))