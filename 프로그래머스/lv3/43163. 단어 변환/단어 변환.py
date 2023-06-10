from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    q = deque([(begin, 0)])
    while q:
        w, cnt = q.popleft()
        if w == target:
            return cnt
        
        for word in words:
            diff = 0
            for i in range(len(w)):
                if w[i] != word[i]:
                    diff += 1
                    if diff > 1:
                        break
            
            if diff == 1:
                q.append((word, cnt + 1))
    
    return 0
    