N, M, H = map(int, input().split())
Min = 4
G = [[0] * N for _ in range(H)]

for _ in range(M):
    a, b = map(int, input().split())
    G[a - 1][b - 1] = 1

def check():
    for i in range(N):
        tmp = i
        for j in range(H):
            if G[j][tmp]:
                tmp += 1
            elif tmp > 0 and G[j][tmp - 1]:
                tmp -= 1
        if tmp != i:
            return False
    return True

def dfs(x, y, cnt):
    global Min

    if Min <= cnt:
        return
    if check():
        Min = min(Min, cnt)
        return
    if cnt == 3:
        return

    for i in range(x, H):
        if x == i:
            k = y
        else:
            k = 0
        for j in range(k, N - 1):
            if G[i][j] == 0:
                G[i][j] = 1
                dfs(i, j + 2, cnt + 1)
                G[i][j] = 0

dfs(0, 0, 0)
print(Min if Min <= 3 else -1)