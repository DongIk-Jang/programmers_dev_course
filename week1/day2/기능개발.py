def solution(progresses, speeds):
    answer = []
    while progresses:
        for i in range(len(progresses)):
            progresses[i] = progresses[i] + speeds[i]
        if progresses[0] >= 100:
            count = 0
            while len(progresses) > 0 and progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                count += 1
            answer.append(count)
    return answer

progresses = [93,30,55]
speeds = [1,30,5]
print(solution(progresses, speeds))