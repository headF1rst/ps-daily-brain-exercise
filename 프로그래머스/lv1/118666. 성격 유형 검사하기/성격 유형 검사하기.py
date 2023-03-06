from collections import defaultdict

def solution(survey, choices):
    answer = ''
    dict = defaultdict(int)
    dict['R'], dict['T'], dict['C'], dict['F'], dict['J'], dict['M'], dict['A'], dict['N']
    
    for s, c in zip(survey, choices):
        a, b = s[0], s[1]
        score = 4 - c
        if score < 0:
            dict[b] += abs(score)
        else:
            dict[a] += score
        
    if dict['R'] < dict['T']:
        answer += 'T'
    else:
        answer += 'R'
        
    if dict['C'] < dict['F']:
        answer += 'F'
    else:
        answer += 'C'
        
    if dict['J'] < dict['M']:
        answer += 'M'
    else:
        answer += 'J'
    
    if dict['A'] < dict['N']:
        answer += 'N'
    else:
        answer += 'A'
    return answer
        