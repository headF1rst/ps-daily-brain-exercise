from collections import deque

def solution(priorities, location):
    q = deque()
    answer = 0
    
    for i, priority in enumerate(priorities):
        q.append((priority, i))
    
    while True:
        Max = max(q)
        e, i = q.popleft()
        
        if e == Max[0]:
            answer += 1
            if i == location:
                return answer
        else:
            q.append((e, i))
    
    