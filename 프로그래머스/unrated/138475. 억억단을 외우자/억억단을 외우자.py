def solution(e, starts):
    appeared = [0] * (e + 1)
    numbs = [1] * (e + 1)
    max_num = 0
    
    for i in range(1, e + 1):
        for j in range(i, e + 1):
            tmp = i * j
            if tmp > e:
                break
            appeared[tmp] += 1 if i == j else 2
    
    for i in range(e, 0, -1):
        if appeared[i] >= max_num:
            numbs[i] = i
            max_num = appeared[i]
        else:
            numbs[i] = numbs[i + 1]
    
    return [numbs[start] for start in starts]