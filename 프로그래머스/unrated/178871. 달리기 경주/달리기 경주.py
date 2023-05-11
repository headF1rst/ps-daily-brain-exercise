from collections import defaultdict

def solution(players, callings):
    answer = []
    dic = defaultdict(int)
    ranking = [0] * len(players)
    
    for i, player in enumerate(players):
        dic[player] = i
        ranking[i] = player
        
    for call in callings:
        cur_rank = dic[call]
        dic[call] = cur_rank - 1
        
        tmp = ranking[cur_rank - 1]
        ranking[cur_rank - 1] = call
        ranking[cur_rank] = tmp
        dic[tmp] = cur_rank
    
    return ranking