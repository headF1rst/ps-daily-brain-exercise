n = int(input())
st_cnt = n ** 2
likes = [[] for _ in range(st_cnt + 1)]
G = [[0] * n for _ in range(n)]
dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]
students = []

for _ in range(st_cnt):
    arr = list(map(int, input().split()))
    likes[arr[0]] = arr[1:]
    students.append(arr[0])

def in_boundary(nx, ny):
    return 0 <= nx < n and 0 <= ny < n

def locate_student():
    for student in students:
        loc = ()
        for i in range(n):
            for j in range(n):
                if G[i][j] == 0:
                    x, y = i, j
                    blank = 0
                    friends = 0
                    for dx, dy in zip(dxs, dys):
                        nx = x + dx
                        ny = y + dy
                        if in_boundary(nx, ny):
                            if G[nx][ny] == 0:
                                blank += 1
                            elif G[nx][ny] in likes[student]:
                                friends += 1
                    if not loc:
                        loc = (friends, blank, x, y)
                    elif loc[0] < friends:
                        loc = (friends, blank, x, y)
                    elif loc[0] == friends and loc[1] < blank:
                        loc = (friends, blank, x, y)
        f, b, x, y = loc
        G[x][y] = student

def how_happy():
    answer = 0
    for i in range(n):
        for j in range(n):
            happy = 0
            student = G[i][j]
            x, y = i, j
            for dx, dy in zip(dxs, dys):
                nx = x + dx
                ny = y + dy
                if in_boundary(nx, ny):
                    if G[nx][ny] in likes[student]:
                        happy += 1
            if happy > 0:
                answer += (10 ** (happy - 1))
    print(answer)

locate_student()
how_happy()