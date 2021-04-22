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

    def show(self):
        print(self.data)

            
def solution(x):
    return 0


a = MaxHeap()


n = [2, 3, 7, 8, 13, 15, 17, 19, 24, 28, 29]

for i in n:
    a.insert(i)
a.show()


