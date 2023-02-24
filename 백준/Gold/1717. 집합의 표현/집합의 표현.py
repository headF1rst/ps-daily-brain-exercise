import sys
sys.setrecursionlimit(10 ** 5)

n, m = map(int, input().split())

parent = [i for i in range(n + 1)]

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a == b:
        return
    if a < b:
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]

for _ in range(m):
    cmd, a, b = map(int, input().split())
    if cmd == 1:
        a = find_parent(a)
        b = find_parent(b)
        if a == b:
            print("YES")
        else:
            print("NO")
    else:
        union(a, b)