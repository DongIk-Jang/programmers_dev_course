def solution(participant, completion):
    d = {}
    for x in participant:
        d[x] = d.get(x, 0) + 1
    for x in completion:
        d[x] = d.get(x, 0) - 1
    answer = []
    for j, k in d.items:
        if k > 0:
            answer.append(j)

    return answer

a = {"a":1, "b":2}
print(a.items())
for j, k in a.items():
    print(j, k)