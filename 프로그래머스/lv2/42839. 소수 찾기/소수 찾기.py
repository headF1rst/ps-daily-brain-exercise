from itertools import permutations

def solution(numbers):
    nums = [n for n in numbers]
    pers = []
    answer = []
    
    for i in range(1, len(numbers) + 1):
        pers += list(permutations(nums, i))
    
    new_numbs = [int("".join(p)) for p in pers]
    
    for num in new_numbs:
        if num < 2:
            continue
        is_prime = True
        
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
            answer.append(num)
    
    return len(set(answer))