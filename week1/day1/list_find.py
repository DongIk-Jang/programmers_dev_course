def solution(L, x):
    counter = 0
    answer = []
    if x in L:
        for i in L:
            if i == x:
                answer.append(counter)
                counter += 1
            else:
                counter += 1
    else:
        answer = [-1]
    return answer

L = [64,72,83,72,54]
x = 72
print(solution(L, x))