def solution(sequence, k):
    answer = []
    s, e = 0, 0
    total = sequence[0]
    len_s = len(sequence)
    min_len = 1000001
    
    while s < len_s:
        if total >= k:
            if total == k:
                length = e - s + 1
                if length < min_len:
                    answer = [s, e]
                    min_len = length
            total -= sequence[s]
            s += 1
        elif e + 1 < len_s:
            e += 1
            total += sequence[e]
        else:
            break
            
        
    return answer