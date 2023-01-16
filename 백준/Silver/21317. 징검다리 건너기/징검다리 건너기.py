INF = int(1e9)
dp = [[INF] * 2 for _ in range(21)]
stones = [0]

n = int(input())
for _ in range(n - 1):
    a, b = map(int, input().split())
    stones.append((a, b))
k = int(input())

if n == 1:
    print(0)
elif n == 2:
    print(stones[1][0])
else:
    dp[1][0] = 0
    dp[2][0] = stones[1][0]
    dp[3][0] = min(stones[1][0] + stones[2][0], stones[1][1])
    for i in range(4, n + 1):
        dp[i][0] = min(stones[i - 1][0] + dp[i - 1][0], stones[i - 2][1] + dp[i - 2][0])
        dp[i][1] = min(stones[i - 1][0] + dp[i - 1][1], stones[i - 2][1] + dp[i - 2][1], dp[i - 3][0] + k)

    print(min(dp[n][0], dp[n][1]))