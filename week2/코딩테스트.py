def solution(strs, t):
    data = sorted(strs, key=len, reverse=True)
    answer = []
    detect = []
    for j in range(len(data)):
        temp = t
        stack = []
        idx = j
        print(idx)
        while idx < len(strs):
            a = data[idx]
            # print(idx, a)
            if a in temp:
                # print(a, t)
                count = temp.count(a)
                temp = temp.replace(a, '')
                for i in range(count):
                    stack.append(a)
            else:
                idx += 1
            if len(temp) == 0:
                print(stack)
                answer.append(len(stack))
            if idx == len(strs) and len(temp) != 0:
                detect.append(-1)
        # answer.append(-1)
        idx += 1
    print(answer)
    return min(answer)

# print(solution(["ba","na","n","a"], "banana"))
print(solution(["ab", "na", "n", "a", "bn"], 'nabnabn'))
# a = "na"
# # b = "banana"
# # print(b.count(a))
# stack = []
# stack.append(a*2)
# print(stack)
