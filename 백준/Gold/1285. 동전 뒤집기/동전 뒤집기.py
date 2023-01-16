n = int(input())
G = [list(input()) for _ in range(n)]
INF = int(1e9)
answer = INF

for bit in range(1 << n):
    tmp = [G[i][:] for i in range(n)]
    for i in range(n):
        if bit & (1 << i):
            for j in range(n):
                if tmp[i][j] == 'T':
                    tmp[i][j] = 'H'
                else:
                    tmp[i][j] = 'T'

    total = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if tmp[j][i] == 'T':
                cnt += 1
        total += min(cnt, n - cnt)
    answer = min(answer, total)

print(answer)