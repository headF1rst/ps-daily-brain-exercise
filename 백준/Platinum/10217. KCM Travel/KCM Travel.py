from collections import deque

T = int(input())

def dijk(start):
    q = deque([(0, 0, start)])
    distance[start][0] = 0
    while q:
        time, cost, curNode = q.popleft()
        if distance[curNode][cost] < time:
            continue
        for nextNode, c, t in G[curNode]:
            tmp_t = time + t
            tmp_c = cost + c
            if tmp_c <= M and distance[nextNode][tmp_c] > tmp_t:
                for i in range(tmp_c, M + 1):
                    if distance[nextNode][i] > tmp_t:
                        distance[nextNode][i] = tmp_t
                    else:
                        break
                q.append((tmp_t, tmp_c, nextNode))

for _ in range(T):
    N, M, K = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    distance = [[int(1e9)] * (M + 1) for _ in range(N + 1)]

    for _ in range(K):
        u, v, c, d = map(int, input().split())
        G[u].append((v, c, d))

    dijk(1)

    if distance[N][M] == int(1e9):
        print("Poor KCM")
    else:
        print(distance[N][M])