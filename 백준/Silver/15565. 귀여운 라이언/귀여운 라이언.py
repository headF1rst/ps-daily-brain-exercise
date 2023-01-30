import math

n, k = map(int, input().split())
nums = list(map(int, input().split()))
s, e = 0, 0
cnt = 0
INF = math.inf
answer = INF

if nums[s] == 1:
    cnt += 1
while e < n:
    if cnt == k:
        answer = min(answer, e - s + 1)
        if nums[s] == 1:
            cnt -= 1
        s += 1
    else:
        e += 1
        if e < n and nums[e] == 1:
            cnt += 1

if answer == INF:
    print(-1)
else:
    print(answer)
