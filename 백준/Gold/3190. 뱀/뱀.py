from collections import deque

N = int(input())
K = int(input())
G = [[0] * N for _ in range(N)]
visited = [[False] * N for _ in range(N)]
q = deque()
dxs = [1, 0, -1, 0] # 위, 오, 아래, 왼
dys = [0, 1, 0, -1]
d, t = 1, 0
snake_loc = deque([(0, 0)])

for _ in range(K):
    ax, ay = map(int, input().split())
    G[ax - 1][ay - 1] = 1

L = int(input())
for _ in range(L):
    x, c = input().split()
    q.append((int(x), c))

def in_boundary(nx, ny):
    return 0 <= nx < N and 0 <= ny < N

def rotate_left():
    global d
    d = (d + 1) % 4

def rotate_right():
    global d
    d -= 1
    if d < 0:
        d = 3

sx, sy = 0, 0
visited[sx][sy] = True
time = 0
while True:
    time += 1
    sx += dxs[d]
    sy += dys[d]
    if not in_boundary(sx, sy) or visited[sx][sy]:
        print(time)
        break
    visited[sx][sy] = True
    snake_loc.append((sx, sy))
    if G[sx][sy] == 0:
        x, y = snake_loc.popleft()
        visited[x][y] = False
    else:
        G[sx][sy] = 0
    if q and q[0][0] == time:
        nt, nd = q.popleft()
        if nd == 'L':
            rotate_left()
        else:
            rotate_right()
