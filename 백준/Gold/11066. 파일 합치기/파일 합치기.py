import math

T = int(input())
INF = math.inf

for _ in range(T):
    n = int(input())
    files = list(map(int, input().split()))
    result = [[0] * n for _ in range(n)]
    for j in range(1, n):
        for i in range(j - 1, -1, -1):
            small = INF
            for k in range(j - i):
                small = min(small, result[i][i + k] + result[i + k + 1][j])
            result[i][j] = small + sum(files[i: j + 1])
    print(result[0][n - 1])
