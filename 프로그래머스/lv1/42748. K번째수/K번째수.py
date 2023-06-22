def solution(array, commands):
    answer = []
    
    for command in commands:
        i, j, k = command
        tmp = array[i - 1: j]
        tmp.sort()
        answer.append(tmp[k - 1])
    
    return answer