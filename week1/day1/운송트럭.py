# a = [["toy","70"], ["snack", "200"]]
# b = {}
# for i in a:
#     b[i[0]] = i[1]
# print(b)

# def solution(max_weight, specs, names):
#     spec = {}
#     for name in specs:
#         spec[name[0]] = int(name[1])
#     count = 0
#     temp = spec[names[0]]
#     # names = names[::-1]
#     for i in names[1:]:
#         if temp + spec[i] >= max_weight:
#             count += 1
#             print(temp)
#             temp = spec[i]
            
#         else:
#             temp += spec[i]
#             print(temp)
#     return count

def solution(max_weight, specs, names):
    spec = {}
    for name in specs:
        spec[name[0]] = int(name[1])
    temp = spec[names[0]]
    names = names[::-1]
    count = 0
    while names:
        if temp + spec[names[-1]] >= max_weight:
            count += 1
        n = names.pop()
        temp += spec[n]
    return count


a = [["toy","70"], ["snack", "200"]]
b = ["toy", "snack", "snack", "toy", "toy"]
print(solution(300, a, b))

def solution(max_weight, specs, names):
    answer = 0
    s = {}
    for i, j in specs:
        s[i] = s.get(i, int(j))
    data = []
    for i in names:
        data.append(s[i])
    data = data[::-1]
    weightCount = 0
    print(data)
    while data:
        t = data.pop()
        weightCount += t
        if weightCount == max_weight:
            answer += 1
            weightCount = 0
        elif weightCount > max_weight:
            weightCount = 0
            data.append(t)
            answer += 1
    if weightCount != 0:
        answer += 1
    return answer


# k = [["toy","70"], ["snack", "200"]]
# s = {}
# for i, j in k:
#     s[i] = s.get(i, int(j))
# print(s)

a = [["toy","70"], ["snack", "200"]]
b = ["toy", "snack", "snack", "toy", "toy"]
solution(300, a, b)
