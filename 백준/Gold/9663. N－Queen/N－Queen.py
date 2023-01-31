n = int(input())
answer = 0
row = [0] * n

def is_promising(depth, i):
    for k in range(depth):
        if row[depth] == row[k] or abs(row[k] - i) == depth - k:
            return False
    return True

def dfs(depth):
    global answer

    if depth == n:
        answer += 1
        return

    for i in range(n):
        row[depth] = i
        if is_promising(depth, i):
            dfs(depth + 1)

dfs(0)
print(answer)