n, m, k = map(int, input().split())
G = [list(input()) for _ in range(k)]
blocks = list(input())
v = [[] for _ in range(26)]

s, e = 0, m - 1
answer = 0

for i in range(m - 2, -1, -1):
    idx = ord(blocks[n - 1]) - 65
    if G[idx][i] == 'U':
        s = i + 1
        break

for i in range(k):
    if not v[i]:
        for j in range(m):
            if G[i][j] == 'U':
                v[i].append(j)

answer += (e - s + 1)
for i in range(n - 2, -1, -1):
    idx = ord(blocks[i]) - 65
    if not v[idx]:
        break
    lo, hi = 0, len(v[idx]) - 1
    st, ed = -1, -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if v[idx][mid] >= s:
            st = mid
            hi = mid - 1
        else:
            lo = mid + 1

    lo = 0
    hi = len(v[idx]) - 1
    if st == -1:
        break
    while lo <= hi:
        mid = (lo + hi) // 2
        if v[idx][mid] <= e:
            ed = mid
            lo = mid + 1
        else:
            hi = mid - 1
    if ed == -1:
        break
    e = v[idx][ed]
    if st == 0:
        s = 0
    else:
        s = v[idx][st - 1] + 1
    answer += (e - s + 1)

print(answer)
