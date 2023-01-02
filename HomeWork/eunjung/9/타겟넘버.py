from itertools import combinations

def solution(numbers, target):
    answer = 0
    sumn= sum(numbers)
    for i in range(1, len(numbers)+1):
        for j in combinations(numbers, i):
            if sumn - 2*sum(j) == target:
                answer += 1
    return answer