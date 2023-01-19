str = input().rstrip()
alpha = [0] * 26

for s in str:
    alpha[ord(s) - 97] += 1

for a in alpha:
    print(a, end=' ')