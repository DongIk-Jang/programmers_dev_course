def solution(skill, skill_trees):
    count = 0
    for i in skill_trees:
        idx = 0
        for j in i:
            if j in skill:
                if j == skill[idx]:
                    if j == i[-1]:
                        count += 1
                        break
                    elif idx < len(skill)-1:
                        idx += 1
                    
                    if idx == len(skill)-1:
                        count += 1
                        break
                else:
                    break
            elif j == i[-1]:
                count += 1

    return count