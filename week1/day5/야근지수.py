import heapq

def solution(n, works):
    answer = 0
    heap = [-x for x in works]
    heapq.heapify(heap)
    for i in range(n):
        if heap[0] == 0:
            return 0
        w = heapq.heappop(heap) + 1
        heapq.heappush(heap, w)
    leftover = [-x for x in heap]
    for i in leftover:
        answer += i*i
    return answer