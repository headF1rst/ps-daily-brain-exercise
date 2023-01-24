n, m = map(int, input().split())
G = [[0] * (m + 1)]

for _ in range(n):
    tmp = [0] + list(map(int, input()))
    G.append(tmp)

answer = 0
s = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + G[i][j]

def sum_cal(x1, y1, x2, y2):
    return s[x2][y2] - s[x2][y1 - 1] - s[x1 - 1][y2] + s[x1 - 1][y1 - 1]

for i in range(1, m - 1):
    for j in range(i + 1, m):
        r1 = sum_cal(1, 1, n, i)
        r2 = sum_cal(1, i + 1, n, j)
        r3 = sum_cal(1, j + 1, n, m)
        if answer < r1 * r2 * r3:
            answer = r1 * r2 * r3

for i in range(1, n - 1):
    for j in range(i + 1, n):
        r1 = sum_cal(1, 1, i, m)
        r2 = sum_cal(i + 1, 1, j, m)
        r3 = sum_cal(j + 1, 1, n, m)
        if answer < r1 * r2 * r3:
            answer = r1 * r2 * r3

for i in range(1, m):
    for j in range(1, n):
        r1 = sum_cal(1, 1, n, i)
        r2 = sum_cal(1, i + 1, j, m)
        r3 = sum_cal(j + 1, i + 1, n, m)
        if answer < r1 * r2 * r3:
            answer = r1 * r2 * r3

for i in range(1, n):
    for j in range(1, m):
        r1 = sum_cal(1, 1, i, j)
        r2 = sum_cal(i + 1, 1, n, j)
        r3 = sum_cal(1, j + 1, n, m)
        if answer < r1 * r2 * r3:
            answer = r1 * r2 * r3

for i in range(1, n):
    for j in range(1, m):
        r1 = sum_cal(1, 1, i, m)
        r2 = sum_cal(i + 1, 1, n, j)
        r3 = sum_cal(i + 1, j + 1, n, m)
        if answer < r1 * r2 * r3:
            answer = r1 * r2 * r3

for i in range(1, n):
    for j in range(1, m):
        r1 = sum_cal(1, 1, i, j)
        r2 = sum_cal(1, j + 1, i, m)
        r3 = sum_cal(i + 1, 1, n, m)
        if answer < r1 * r2 * r3:
            answer = r1 * r2 * r3

print(answer)