# import heapq
class MaxHeap:

    def __init__(self):
        self.data = [None]

    def insert(self, item):
        if len(self.data) >= 2:
            self.data.append(item)
            i = len(self.data)-1
            while item > self.data[i//2]:
                self.data[i], self.data[i//2] = self.data[i//2], self.data[i]
                i = i//2
                if i <= 1:
                    break
        else:
            self.data.append(item)

    def remove(self):
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop(-1)
            self.maxHeapify(1)
        else:
            data = None
        return data


    def maxHeapify(self, i):
        left = i * 2
        right = (i * 2) + 1
        smallest = i
        if left < len(self.data) and self.data[left] > self.data[smallest]:
            smallest = left

        if right < len(self.data) and self.data[right] > self.data[smallest]:
            smallest = right

        if smallest != i:
            self.data[smallest], self.data[i] = self.data[i], self.data[smallest]
            self.maxHeapify(smallest)



def solution(no, works):
    result = 0
    heap = MaxHeap()
    for i in works:
        heap.insert(i)
    print(works)
    for i in range(no):
        # 만약 가장 큰 값이 0인 경우 일을 다 끝냈기 때문에 배상비용 없음
        if heap.data[1] == 0:
            return 0
        w = heap.remove() -1
        heap.insert(w)
    leftover = heap.data[1:]
    print(leftover)
    for i in leftover:
        result += i*i
    print(result)
    return result


solution(4, [1,7,5,3,9,8])
# a = [1,7,5,3,9,8]
# b = MaxHeap()
# for i in a:
#     b.insert(i)
# print(b.data)
