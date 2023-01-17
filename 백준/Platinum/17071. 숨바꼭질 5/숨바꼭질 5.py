from collections import deque

n, k = map(int, input().split())
Max = 500000
visited = [[-1] * 2 for _ in range(Max + 1)]

def in_boundary(nx):
    return 0 <= nx <= Max

def bfs():
    q = deque([(n, 0)])
    visited[n][0] = 0
    while q:
        x, cnt = q.popleft()
        flag = cnt % 2
        for nx in [x + 1, x - 1, x * 2]:
            if in_boundary(nx) and visited[nx][1 - flag] == -1:
                visited[nx][1 - flag] = cnt + 1
                q.append((nx, cnt + 1))

bfs()
time, flag, answer = 0, 0, -1
while k <= Max:
    if visited[k][flag] != -1 and visited[k][flag] <= time:
        answer = time
        break
    time += 1
    k += time
    flag = 1 - flag
print(answer)