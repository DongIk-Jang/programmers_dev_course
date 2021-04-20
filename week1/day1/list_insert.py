def solution(L, x):
    counter = 0
    for i in L:
        if x >= i:
            counter += 1
        else:
            L.insert(counter, x)
            break
    else:
        L.append(x)
    return L