from itertools import combinations

def solution(m, weights):
    answer = 0
    for i in range(1, len(weights)+1):
        temp = combinations(weights, i)
        for i in temp:
            if sum(i) == m:
                answer += 1
    return answer

w = [500, 1500, 2500, 1000, 2000]
print(solution(3000, w))