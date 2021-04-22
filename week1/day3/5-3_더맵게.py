import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while True:
        min1 = heapq.heappop(scoville)
        if min1 >= K:
            break
        elif len(scoville) == 0:
            break
        min2 = heapq.heappop(scoville)
        hotter = min1 + 2 * min2
        heapq.heappush(scoville, hotter)
        answer += 1
    return answer