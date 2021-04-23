def solution(monster, S1, S2, S3):
    s = []
    for i in range(1, S1+1):
        for j in range(1, S2+1):
            for k in range(1, S3+1):
                s.append(i+j+k)
    num = len(s)
    count = 0
    for i in s:
        if i+1 in monster:
            count += 1
    answer = int(1000 - (count / num) * 1000)
    return answer

from itertools import product

# product(S1, S2, S3) 이용
