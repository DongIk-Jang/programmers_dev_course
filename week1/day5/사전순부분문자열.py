def solution(s):
    collected = []
    # collected가 자기가 가장 마지막에 받은 것보다 큰게 들어오면
    # 마지막꺼 버리고 새로운 큰걸 취하는 방식
    # 가장 마지막 값보다 작은건 나중에 큰거 나오기 전까지 일단 받아서 유지
    for num in s:
        while len(collected) > 0 and collected[-1] < num:
            collected.pop()
        collected.append(num)
    
    answer = ''.join(collected)
    return answer