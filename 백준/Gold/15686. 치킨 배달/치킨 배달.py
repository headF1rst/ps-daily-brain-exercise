from itertools import combinations

N, M = map(int, input().split())
chickens = []
houses = []
Min = int(1e9)

def calc_dist(comb):
    total = 0
    for house in houses:
        x1, y1 = house
        dist = int(1e9)
        for x2, y2 in comb:
            dist = min(dist, abs(x1 - x2) + abs(y1 - y2))
        total += dist
    return total

for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] == 2:
            chickens.append((i, j))
        if tmp[j] == 1:
            houses.append((i, j))

combs = combinations(chickens, M)

for comb in combs:
    Min = min(Min, calc_dist(comb))

print(Min)