import sys
input = sys.stdin.readline

n, s = map(int, input().split())
numbers = [0] + list(map(int, input().split()))
sum = numbers[1]
idxS, idxE = 1, 1
result = []

while idxS <= idxE:
    if sum < s:
        idxE += 1
        if idxE <= n:
            sum += numbers[idxE]
        else:
            break
    else:
        result.append(idxE - idxS + 1)
        sum -= numbers[idxS]
        idxS += 1
        if idxS > n: break

if not result:
    print(0)
else:
    print(min(result))