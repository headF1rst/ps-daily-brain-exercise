import sys
input = sys.stdin.readline

n = int(input())
cases = list(map(int, input().split()))

memoization = [0]

for case in cases:
    if memoization[-1] < case:
        memoization.append(case)
    else:
        left = 0
        right = len(memoization)
        while left < right:
            mid = (left + right) // 2
            if memoization[mid] < case:
                left = mid + 1
            else:
                right = mid

        memoization[right] = case

print(len(memoization) - 1)
