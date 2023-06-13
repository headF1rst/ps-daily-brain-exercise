from collections import defaultdict

def solution(genres, plays):
    cnt = defaultdict(int)
    each_cnt = defaultdict(list)
    tmp = []
    answer = []
    
    for i in range(len(plays)):
        g, p = genres[i], plays[i]
        cnt[g] += p
        each_cnt[g].append((p, i))
    
    for k, v in cnt.items():
        tmp.append((v, k))
    tmp.sort(reverse=True)
    
    for t in tmp:
        _, genre = t
        each_cnt[genre].sort(key=lambda x: (-x[0], x[1]))
        if len(each_cnt[genre]) >= 2:
            answer.append(each_cnt[genre][0][1])
            answer.append(each_cnt[genre][1][1])
        else:
            answer.append(each_cnt[genre][0][1])
    
    return answer