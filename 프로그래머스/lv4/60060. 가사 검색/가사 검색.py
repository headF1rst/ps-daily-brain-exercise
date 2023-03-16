from collections import defaultdict
from bisect import bisect_left, bisect_right

def count_by_range(lst, s, e):
    return bisect_right(lst, e) - bisect_left(lst, s)

def solution(words, queries):
    answer = []
    cands = defaultdict(list)
    reverse_cands = defaultdict(list)
    for word in words:
        cands[len(word)].append(word)
        reverse_cands[len(word)].append(word[::-1])
    
    for cand in cands.values():
        cand.sort()
    for cand in reverse_cands.values():
        cand.sort()
    
    for query in queries:
        if query[0] == '?':
            lst = reverse_cands[len(query)]
            s, e = query[::-1].replace('?', 'a'), query[::-1].replace('?', 'z')
        else:
            lst = cands[len(query)]
            s, e = query.replace('?', 'a'), query.replace('?', 'z')
        answer.append(count_by_range(lst, s, e))
    
    return answer