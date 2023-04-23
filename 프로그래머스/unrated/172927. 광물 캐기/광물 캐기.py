def solution(picks, minerals):
    
    def divide(minerals, n):
        return [minerals[i: i + n] for i in range(0, len(minerals), n)]
    
    minerals_divided = divide(minerals, 5)
    costs = []
    answer = 0
    
    for mineral in minerals_divided:
        cost = [0, 0, 0]
        for m in mineral:
            if m == 'diamond':
                cost[0] += 1
                cost[1] += 5
                cost[2] += 25
            elif m == 'iron':
                cost[0] += 1
                cost[1] += 1
                cost[2] += 5
            else:
                cost[0] += 1
                cost[1] += 1
                cost[2] += 1
        costs.append(cost)
    
    while len(costs) > sum(picks):
        costs.pop()
    
    costs.sort(key=lambda x: x[2], reverse=True)
    
    for cost in costs:
        if picks[0] > 0:
            picks[0] -= 1
            answer += cost[0]
        elif picks[1] > 0:
            picks[1] -= 1
            answer += cost[1]
        elif picks[2] > 0:
            picks[2] -= 1
            answer += cost[2]
    
    return answer