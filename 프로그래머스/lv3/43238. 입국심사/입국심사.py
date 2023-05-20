def solution(n, times):
    left = min(times)
    right = max(times) * n
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2
        check = 0
        
        for time in times:
            check += mid // time
            if check >= n:
                break
        
        if check >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return answer