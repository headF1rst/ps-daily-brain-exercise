n = int(input())
lines = []
for _ in range(n):
    a, b = map(int, input().split())
    lines.append((a, b))
lines.sort()
target_lines = []
for _, b in lines:
    target_lines.append(b)

def lis():
    result = [1] * n
    for i in range(1, n):
        for j in range(i):
            if target_lines[j] < target_lines[i]:
                result[i] = max(result[i], result[j] + 1)
    return max(result)

print(n - lis())