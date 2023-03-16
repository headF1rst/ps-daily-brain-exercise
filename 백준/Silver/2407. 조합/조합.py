n, m = map(int, input().split())

def facto(n):
    num = 1
    for i in range(2, n + 1):
        num *= i
    return num

print(facto(n) // (facto(n - m) * facto(m)))