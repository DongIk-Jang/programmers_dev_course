class MyStack(object):
    def __init__(self):
        self.lst = list()

    def push(self, x):
        self.lst.append(x)

    def pop(self):
        return self.lst.pop()

    def size(self):
        return len(self.lst)

class MyQueue(object):
    def __init__(self, max_size):
        self.stack1 = MyStack()
        self.stack2 = MyStack()
        self.max_size = max_size

    def qsize(self):
        # 구현하세요
        return self.stack1.size()

    def push(self, item):
        # 구현하세요
        if self.qsize() == self.max_size:
            return False
        elif self.qsize() < self.max_size:
            self.stack1.push(item)

    def pop(self):
        # 구현하세요
        if self.qsize() == 0:
            raise Exception("Queue is Empty")
        else:
            while self.qsize() > 0:
                self.stack2.push(self.stack1.pop())
                if self.qsize() == 0:
                    answer = self.stack2.pop()
            while self.stack2.size() > 0:
                self.stack1.push(self.stack2.pop())
            return answer
    
n, max_size = map(int, input().strip().split(' '))
data = []
q = MyQueue(max_size)
for i in range(n):
    data.append(input().split(' '))
for i in data:
    if i[0] == "SIZE":
        print(q.qsize())
    elif i[0] == "POP":
        try:
            print(q.pop())
        except:
            print(False)
    else:
        if q.push(int(i[1])) == False:
            print(False)
        else:
            print(True)