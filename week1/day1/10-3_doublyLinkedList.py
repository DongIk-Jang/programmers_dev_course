class Node:

    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None


    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result


    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        if pos > self.nodeCount // 2:
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        else:
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1

        return curr


    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)


    def popAfter(self, prev):
        curr = prev.next
        next = curr.next
        prev.next = next
        next.prev = prev
        self.nodeCount -= 1
        return curr.data


    def popBefore(self, next):
        curr = next.prev
        prev = curr.prev
        prev.next = next
        next.prev = prev
        self.nodeCount -= 1
        return curr.data


    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        # prev = self.getAt(pos-1)
        # curr = prev.next
        # next = curr.next
        # prev.next = next
        # next.prev = prev
        # self.nodeCount -= 1
        # return curr.data
        prev = self.getAt(pos - 1)
        return self.popAfter(prev)



def solution(x):
    return 0


testList = DoublyLinkedList()
scores = {"James":80, "Aaron":75, "Paul":90, "Ella":85, "Kyle":80}
for i in scores:
    print(i)
    scores[i] = Node(scores[i])
    print(scores)
    # i = Node(scores[i])
    # testList.insertAt(1, i)
for i in scores:
    testList.insertAt(1, scores[i])
James = Node(80)
Aaron = Node(75)
print(testList.traverse())
print(testList.popAt(3))
testList.insertAt(1, James)
print(testList.traverse())
testList.insertAfter(James, Node(10))
print(testList.traverse())

a = DoublyLinkedList()
n = Node(5)
k = Node(5)
a.insertAt(1, n)
a.insertAfter(n, Node(10))
a.insertAt(1, Node(9))
a.insertAfter(n, Node(8))
a.insertAt(4, k)
a.insertAfter(k, Node(1))
print(a.traverse())