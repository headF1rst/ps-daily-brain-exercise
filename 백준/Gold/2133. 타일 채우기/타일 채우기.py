n = int(input())
dp = [0] * 31
dp[1], dp[2], dp[3], dp[4] = 0, 3, 0, 11

for i in range(4, n + 1):
    if i % 2 != 0:
        continue
    dp[i] = dp[i - 2] * 3 + sum(dp[:i - 2]) * 2 + 2

print(dp[n])