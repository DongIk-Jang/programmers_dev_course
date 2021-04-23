def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    answer = sum(map(lambda x, y: x*y, A, B))
    return answer