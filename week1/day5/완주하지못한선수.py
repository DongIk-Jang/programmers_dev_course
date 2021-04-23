def solution(participant, completion):
    s ={}
    for p in participant:
        s[p] = s.get(p, 0) + 1
    for c in completion:
        s[c] -= 1
    answer = ""
    for i, j in s.items():
        if j > 0:
            answer += i
    return answer

p = ["marina", "josipa", "nikola", "vinko", "filipa"]
c = ["josipa", "filipa", "marina", "nikola"]
print(solution(p,c))