n = int(input())
arr = list(map(int, input().split()))
arr.sort()
start, end = 0, n - 1
answer = (start, end)
Min = int(1e9) * 2

while start < end:
    total = arr[start] + arr[end]
    if Min > abs(total):
        answer = (arr[start], arr[end])
        Min = abs(total)

    if total < 0:
        start += 1
    else:
        end -= 1

sorted(answer)
print(answer[0], answer[1])