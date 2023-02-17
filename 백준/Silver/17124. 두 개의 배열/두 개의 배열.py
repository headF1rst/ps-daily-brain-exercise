import bisect

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    B.sort()
    answer = 0

    for i in range(n):
        idx = bisect.bisect_left(B, A[i])
        if (idx != m and B[idx] == A[i]) or idx == 0:
            answer += B[idx]
            continue
        if idx == m:
            answer += B[idx - 1]
            continue
        left, right = idx - 1, idx
        if abs(B[left] - A[i]) <= abs(B[right] - A[i]):
            answer += B[left]
        else:
            answer += B[right]

    print(answer)

