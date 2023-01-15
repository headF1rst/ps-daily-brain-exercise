from collections import deque
n, T = map(int, input().split())
dots = set()
answer = -1

for _ in range(n):
    x, y = map(int, input().split())
    dots.add((x, y))

q = deque([(0, 0, 0)])
while q:
    x, y, cnt = q.popleft()
    if y == T:
        answer = cnt
        break
    for dx in range(-2, 3):
        for dy in range(-2, 3):
            nx = x + dx
            ny = y + dy
            if (nx, ny) in dots:
                q.append((nx, ny, cnt + 1))
                dots.remove((nx, ny))

print(answer)