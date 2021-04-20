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

def solution3(x):
    if x <= 1:
        return x
    else:
        i = 2
        t0 = 0
        t1 = 1
        while i <= x:
            t0, t1 = t1, t0 + t1
            i += 1
        return t1

print(solution2(5))