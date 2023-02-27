N, M, K = map(int, input().split())
add_minerals = [list(map(int, input().split())) for _ in range(N)]
minerals = [[5] * N for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x - 1][y - 1].append(z)

dxs = [1, 0, -1, 0, 1, 1, -1, -1]
dys = [0, 1, 0, -1, -1, 1, -1, 1]

def in_boundary(nx, ny):
    return 0 <= nx < N and 0 <= ny < N

for _ in range(K):
    for i in range(N):
        for j in range(N):
            if trees[i][j]:
                total_mineral, dead_tree = 0, 0
                tmp_trees = []
                trees[i][j].sort()
                for age in trees[i][j]:
                    if age <= minerals[i][j]:
                        minerals[i][j] -= age
                        age += 1
                        tmp_trees.append(age)
                    else:
                        dead_tree += 1
                        total_mineral += (age // 2)

                minerals[i][j] += total_mineral
                trees[i][j] = []
                trees[i][j].extend(tmp_trees)

    for i in range(N):
        for j in range(N):
            if trees[i][j]:
                for age in trees[i][j]:
                    if age % 5 == 0:
                        for dx, dy in zip(dxs, dys):
                            nx = i + dx
                            ny = j + dy
                            if in_boundary(nx, ny):
                                trees[nx][ny].append(1)

    for i in range(N):
        for j in range(N):
            minerals[i][j] += add_minerals[i][j]

answer = 0
for i in range(N):
    for j in range(N):
        if trees[i][j]:
            answer += len(trees[i][j])
print(answer)