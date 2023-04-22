def solution(picks, minerals):
    answer = 0
    costs = []
    
    def divide(minerals, off_set):
        return [minerals[i: i + off_set] for i in range(0, len(minerals), off_set)]
        
    divided_minerals = divide(minerals, 5)
    
    for mineral in divided_minerals:
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
            continue
        if picks[1] > 0:
            picks[1] -= 1
            answer += cost[1]
            continue
        if picks[2] > 0:
            picks[2] -= 1
            answer += cost[2]
            continue
            
    return answer