import math

x = int(input())
if x == 1:
    print(0)
else:
    dp = [0] * (x + 1)
    dp[2] = 1
    INF = math.inf

    for i in range(3, x + 1):
        a, b, c = INF, INF, INF
        if i % 3 == 0:
            a = dp[i // 3] + 1
        if i % 2 == 0:
            b = dp[i // 2] + 1
        c = dp[i - 1] + 1
        dp[i] = min(a, b, c)

    print(dp[x])
