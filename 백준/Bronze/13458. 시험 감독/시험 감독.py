import sys
from math import ceil

input = sys.stdin.readline

def solution(n, a, b, c):
    answer = 0
    for number in a:
        cnt = 0
        tmp = number
        flag = False
        while True:
            if not flag:
                flag = True
                number -= b
                cnt += 1
                if number <= 0:
                    break
            else:
                cnt += ceil(number / c)
                break
        answer += cnt
    return answer


n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
print(solution(n, a, b, c))