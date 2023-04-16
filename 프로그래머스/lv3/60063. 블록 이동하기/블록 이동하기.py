from collections import deque


def can_move(cur1, cur2, G):
    x, y = 0, 1
    dxs = [1, -1, 0, 0]
    dys = [0, 0, 1, -1]
    cand = []
    for dx, dy in zip(dxs, dys):
        next_cur1 = (cur1[x] + dx, cur1[y] + dy)
        next_cur2 = (cur2[x] + dx, cur2[y] + dy)
        if G[next_cur1[x]][next_cur1[y]] == 0 and G[next_cur2[x]][next_cur2[y]] == 0:
            cand.append((next_cur1, next_cur2))

    if cur1[x] == cur2[x]:
        up, down = -1, 1
        for d in [up, down]:
            if G[cur1[x] + d][cur1[y]] == 0 and G[cur2[x] + d][cur2[y]] == 0:
                cand.append(((cur1[x] + d, cur1[y]), cur1))
                cand.append(((cur2[x] + d, cur2[y]), cur2))
    else:
        left, right = 1, -1
        for d in [left, right]:
            if G[cur1[x]][cur1[y] + d] == 0 and G[cur2[x]][cur2[y] + d] == 0:
                cand.append((cur1, (cur1[x], cur1[y] + d)))
                cand.append((cur2, (cur2[x], cur2[y] + d)))
    return cand


def solution(board):
    N = len(board)
    G = [[1] * (N + 2) for _ in range(N + 2)]
    for i in range(N):
        for j in range(N):
            G[i + 1][j + 1] = board[i][j]

    q = deque([((1, 1), (1, 2), 0)])
    visited = set([((1, 1), (1, 2))])
    while q:
        cur1, cur2, cnt = q.popleft()
        if cur1 == (N, N) or cur2 == (N, N):
            return cnt
        for next_move in can_move(cur1, cur2, G):
            if next_move not in visited:
                q.append((*next_move, cnt + 1))
                visited.add(next_move)
