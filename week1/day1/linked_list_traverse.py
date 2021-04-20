class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None
        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    def traverse_my_solution(self):
        answer = []
        curr = self.head
        if self.nodeCount == 0:
            return answer
        i = 1
        for i in range(self.nodeCount):
            answer.append(curr.data)
            curr = curr.next
        return answer
    
    def traverse(self):
        traverse = []
        curr = self.head
        while curr:
            traverse.append(curr.data)
            curr = curr.next
        return traverse
