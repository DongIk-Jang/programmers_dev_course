def solution(d, budget):
    data = sorted(d)
    money = 0
    answer = 0
    i = 0
    while i <= len(d) and money <= budget:
        money += data[i]
        answer += 1
        i += 1
        print(money)

    return answer

d = [1,3,2,5,4]
print(solution(d, 9))