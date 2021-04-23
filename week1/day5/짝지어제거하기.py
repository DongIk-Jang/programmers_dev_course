def solution(s):
    data = list(s)[::1]
    temp = []
    answer = 0
    while data:
        num = data.pop()
        if len(data) > 0 and num != data[-1]:
            if len(temp) > 0:
                if num != temp[-1]:
                    temp.append(num)
                else:
                    temp.pop()
            else:
                temp.append(num)
        elif len(data) > 0 and num == data[-1]:
            data.pop()
            if len(data) == 0 and len(temp) == 0:
                answer = 1
                break
        else:
            if len(temp) > 0:
                if num != temp[-1]:
                    break
                else:
                    temp.pop()
                    answer = 1
            else:
                break
    return answer