def solution(d, budget):
    # data = sorted(d)
    # money = 0
    # answer = 0
    # i = 0
    # while i <= len(d) and money <= budget:
    #     money += data[i]
    #     answer += 1
    #     i += 1
    # if money > budget:
    #     answer -= 1
    # return answer
    data = sorted(d)
    count = 0
    answer = 0
    for i in data:
        count += i
        if count > budget:
            return answer
        answer += 1
    return answer