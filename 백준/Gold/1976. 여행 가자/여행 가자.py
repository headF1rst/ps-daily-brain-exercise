N = int(input())
M = int(input())
parents = [i for i in range(N)]

def find_parent(a):
    if parents[a] != a:
        parents[a] = find_parent(parents[a])
    return parents[a]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

for i in range(N):
    G = list(map(int, input().split()))
    for j in range(N):
        if G[j] == 1:
            union(i, j)

paths = list(map(int, input().split()))
parents = [-1] + parents
start = parents[paths[0]]

for i in range(1, M):
    if parents[paths[i]] != start:
        print("NO")
        break
else:
    print("YES")