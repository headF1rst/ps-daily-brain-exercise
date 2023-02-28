n, m = map(int, input().split())
know_truth = list(map(int, input().split()))[1:]
parent = [i for i in range(n + 1)]
parties = []
answer = 0

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a in know_truth and b in know_truth:
        return
    if a in know_truth:
        parent[b] = parent[a]
    elif b in know_truth:
        parent[a] = parent[b]
    else:
        if a < b:
            parent[b] = parent[a]
        else:
            parent[a] = parent[b]

for _ in range(m):
    party_info = list(map(int, input().split()))
    party_len = party_info[0]
    party = party_info[1:]

    for i in range(party_len - 1):
        union(party[i], party[i + 1])
    parties.append(party)

for party in parties:
    for i in range(len(party)):
        if find_parent(party[i]) in know_truth:
            break
    else:
        answer += 1
print(answer)