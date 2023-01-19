import sys
from collections import deque
import heapq as hq
input = sys.stdin.readline

n, k, p = map(int, input().split())
indegree_min = [0] * k
indegree_max = [0] * k
min_arr = [0] * k
max_arr = [0] * k
G_max = [[] for _ in range(k)]
G_min = [[] for _ in range(k)]
Min = 0
Max = 0
mod = 1000000007
cnt = k - 1

def power(a, b, m):
    res = 1
    while b > 0:
        if b % 2 != 0:
            res = (res * a) % m
        b //= 2
        a = (a * a) % m
    return res

def topology_sort_min():
    result = []
    q = []

    for i in range(k):
        if indegree_min[i] == 0:
            hq.heappush(q, i)

    while q:
        now = hq.heappop(q)
        result.append(now)
        for i in G_min[now]:
            indegree_min[i] -= 1
            if indegree_min[i] == 0:
                hq.heappush(q, i)

    return result

def topology_sort_max():
    result = []
    q = []

    for i in range(k):
        if indegree_max[i] == 0:
            hq.heappush(q, i)

    while q:
        now = hq.heappop(q)
        result.append(now)
        for i in G_max[now]:
            indegree_max[i] -= 1
            if indegree_max[i] == 0:
                hq.heappush(q, i)

    return result

if p:
    for _ in range(p):
        a, b = map(int, input().split())
        G_max[b].append(a)
        G_min[a].append(b)
        indegree_max[a] += 1
        indegree_min[b] += 1

    result = topology_sort_min()

    num = k - 1
    for idx in result:
        min_arr[idx] = num
        num -= 1

    for i in range(k - 1, -1, -1):
        Min += (min_arr[i] * power(n, cnt, mod)) % mod
        cnt -= 1

    result = topology_sort_max()

    num = 0
    for idx in result:
        max_arr[idx] = num
        num += 1

    if n != k:
        tmp = n - k
        for i in range(k):
            max_arr[i] += tmp

    cnt = k - 1
    for i in range(k - 1, -1, -1):
        Max += (max_arr[i] * power(n, cnt, mod)) % mod
        cnt -= 1
else:
    result = [i for i in range(n)]

    for i in range(k):
        Min += (result[i] * power(n, cnt, mod)) % mod
        cnt -= 1

    result = [i for i in range(n - 1, -1, -1)]

    cnt = k - 1
    for i in range(k):
        Max += (result[i] * power(n, cnt, mod)) % mod
        cnt -= 1

ans = (Max - Min + mod) % mod
print(ans)