n = int(input())
days = []
for _ in range(n):
    d = int(input())
    days.append(d)

ships = []
for i in range(1, n):
    ships.append(days[i] - 1)

visited = [False] * (n - 1)
cnt, checked = 0, 0
for i in range(n - 1):
    if not visited[i]:
        if checked == n - 1:
            break
        cnt += 1
        for j in range(n - 1):
            if not visited[j] and ships[j] % ships[i] == 0:
                visited[j] = True
                checked += 1
print(cnt)