def solution(N, number):
    # 숫자를 i+1번 사용해서 만들어진 모든 경우의 수를 담는 집합 생성
    s = [set() for i in range(8)]
    # 우선 각 횟수마다 N을 사칙연산 없이 횟수번 이어붙인 숫자를 넣음
    for i in range(8):
        s[i].add(int(str(N)*(i+1)))

    # 사칙연산을 위한 loop 시작
    for i in range(8):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i-1-j]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)
        if number in s[i]:
            answer = i + 1
            break
    else:
        answer = -1
    return answer

# a = [set() for i in range(8)]
# print(a)
# for i in range(8):
#     a[i].add(int(str(5)*(i+1)))
# print(a)

print(solution(5, 12))