from collections import defaultdict
import sys
import math
sys.setrecursionlimit(10 ** 6)

def solution(numbers):
    numbers = list(map(int, numbers))
    n = len(numbers)
    dic = defaultdict(dict)
    
    W = [
        [1, 7, 6, 7, 5, 4, 5, 3, 2, 3],
        [7, 1, 2, 4, 2, 3, 5, 4, 5, 6],
        [6, 2, 1, 2, 3, 2, 3, 5, 4, 5],
        [7, 4, 2, 1, 5, 3, 2, 6, 5, 4],
        [5, 2, 3, 5, 1, 2, 4, 2, 3, 5],
        [4, 3, 2, 3, 2, 1, 2, 3, 2, 3],
        [5, 5, 3, 2, 4, 2, 1, 5, 3, 2],
        [3, 4, 5, 6, 2, 3, 5, 1, 2, 4],
        [2, 5, 4, 5, 3, 2, 3, 2, 1, 2],
        [3, 6, 5, 4, 5, 3, 2, 4, 2, 1],
    ]
    
    def dfs(depth, left, right):
        if depth == n:
            return 0
        
        if (left, right) in dic[depth]:
            return dic[depth][(left, right)]
        
        c = math.inf
        num = numbers[depth]
        
        if num != right:
            c = min(c, dfs(depth + 1, num, right) + W[left][num])
        if num != left:
            c = min(c, dfs(depth + 1, left, num) + W[right][num])
        
        dic[depth][(left, right)] = c
        return c
        
    return dfs(0, 4, 6)