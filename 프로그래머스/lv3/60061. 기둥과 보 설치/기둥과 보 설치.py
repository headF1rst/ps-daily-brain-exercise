def impossible(answer):
    TOWER, PLATE = 0, 1
    for x, y, a in answer:
        if a == TOWER:
            if y != 0 and (x, y - 1, TOWER) not in answer and (x - 1, y, PLATE) not in answer and (x, y, PLATE) not in answer:
                return True
        else:
            if (x, y - 1, TOWER) not in answer and (x + 1, y - 1, TOWER) not in answer and not ((x - 1, y, PLATE) in answer and (x + 1, y, PLATE) in answer):
                return True
    return False

def solution(n, build_frame):
    answer = set()
    
    for x, y, a, b in build_frame:
        item = (x, y, a)
        if b == 1:
            answer.add(item)
            if impossible(answer):
                answer.remove(item)
        elif item in answer:
            answer.remove(item)
            if impossible(answer):
                answer.add(item)
        
    answer = map(list, answer)
    answer = sorted(answer)
    return answer