def solution(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    return solution(x-1) + solution(x-2)

def solution2(x):
    fibo = [0, 1]
    i = 2
    while i <= x:
        fibo.append(fibo[i-1] + fibo[i-2])
        i += 1
    return fibo[x]

print(solution2(5))