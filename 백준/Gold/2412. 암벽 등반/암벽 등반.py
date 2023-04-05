from collections import deque

n, T = map(int, input().split())
halls = set()
flag = False

for _ in range(n):
    x, y = map(int, input().split())
    halls.add((x, y))

q = deque([(0, 0, 0)])
while q:
    x, y, cnt = q.popleft()
    if y == T:
        flag = True
        print(cnt)
        break

    for dx in range(-2, 3):
        for dy in range(-2, 3):
            nx = x + dx
            ny = y + dy
            if (nx, ny) in halls:
                q.append((nx, ny, cnt + 1))
                halls.remove((nx, ny))

if not flag:
    print(-1)