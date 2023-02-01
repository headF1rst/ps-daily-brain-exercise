from collections import defaultdict

dic = defaultdict(int)

def solution(skill, skill_trees):
    for i in range(len(skill)):
        dic[skill[i]] = i

    answer = 0
    for st in skill_trees:
        visited = [False] * len(skill)
        tmp = []
        flag = True
        for s in st:
            if not tmp and s == skill[0]:
                tmp.append(s)
                visited[0] = True
            elif not tmp and s in skill:
                flag = False
                break
            elif s in skill and dic[tmp[-1]] + 1 == dic[s]:
                visited[dic[s]] = True
                tmp.append(s)
            elif s in skill and dic[tmp[-1]] + 1 < dic[s] and not visited[dic[s]]:
                flag = False
                break
            elif s in skill and dic[tmp[-1]] > dic[s] and not visited[dic[s]]:
                flag = False
                break
        if flag:
            answer += 1

    return answer

