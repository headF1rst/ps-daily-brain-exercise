from collections import deque

def solution(n, computers):
    visited = [False] * n
    answer = 0
    
    def bfs(start):
        q = deque([start])
        while q:
            node = q.popleft()
            if not visited[node]:
                visited[node] = True
                for i in range(n):
                    if computers[node][i] == 1 and not visited[i]:
                        q.append(i)

    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1

    return answer
