from itertools import combinations
N, K = map(int, input().split())
words = [input() for _ in range(N)]
binary_words = []
answer = 0

if K < 5:
    print(0)
else:
    for word in words:
        s = 0
        for w in word:
            s |= 2 ** (ord(w) - 97)
        binary_words.append(s)

    combs = [2 ** i for i in range(26)]
    for i in [0, 2, 8, 13, 19]:
        combs.remove(2 ** i)

    for c in combinations(combs, K - 5):
        cnt, bit = 0, 532741
        for i in c:
            bit += i
        for i in binary_words:
            if bit & i == i:
                cnt += 1
        answer = max(answer, cnt)
    print(answer)
