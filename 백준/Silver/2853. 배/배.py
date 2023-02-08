n = int(input())
days = []
for _ in range(n):
    d = int(input())
    days.append(d - 1)

ships = []
for i in range(1, n):
    if not ships:
        ships.append(days[i])
        continue
    for ship in ships:
        if days[i] % ship == 0:
            break
    else:
        ships.append(days[i])

print(len(ships))