n = int(input())
G = [list(map(int, input().split())) for _ in range(n)]
cnt = [0, 0]

def dfs(row, col, depth):
    if depth == 1:
        cnt[G[row][col]] += 1
        return

    check = G[row][col]
    flag = False
    for r in range(row, row + depth):
        for c in range(col, col + depth):
            if check != G[r][c]:
                flag = True
                break
        if flag:
            break

    if not flag:
        cnt[check] += 1
    else:
        depth //= 2
        dfs(row, col, depth)
        dfs(row + depth, col, depth)
        dfs(row, col + depth, depth)
        dfs(row + depth, col + depth, depth)

dfs(0, 0, n)
for c in cnt:
    print(c)