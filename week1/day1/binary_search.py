def solution(L, x):
    lower = 0
    upper = len(L) - 1
    factor = False
    idx = -1
    while lower <= upper:
        middle = (lower + upper) // 2
        if L[middle] == x:
            factor = True
            idx = middle
            break
        elif L[middle] < x:
            lower = middle + 1
        elif L[middle] > x:
            upper = middle -1
    return idx

L = [2, 3, 5, 6, 9, 11, 15]
print(solution(L, 6))