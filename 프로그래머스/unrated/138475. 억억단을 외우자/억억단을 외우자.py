def solution(e, starts):
    answer = []
    divisor = [1] * (e + 1)
    check = [0] * (e + 1)
    max_num = 0
    
    for i in range(2, e + 1):
        for j in range(i, e + 1):
            tmp = i * j
            if tmp > e:
                break
            divisor[tmp] += 1 if i == j else 2
    
    for i in range(e, 0, -1):
        if divisor[i] >= max_num:
            max_num = divisor[i]
            check[i] = i
        else:
            check[i] = check[i + 1]
    
    return [check[start] for start in starts]