import heapq

def solution(healths, items):
    healths = healths.sort()
    heap = heapq.heapify()
    answer = []
    return answer