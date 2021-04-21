class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):
    opStack = ArrayStack()
    answer = ''
    for i in S:
        # 피연산자일때
        if i not in "*/+-()":
            answer += i
        # ( 일 때
        elif i == "(":
            opStack.push(i)
        # ) 일 때
        elif i == ")":
            while opStack.peek() != "(":
                answer += opStack.pop()
            opStack.pop()
        # 일반연산자일때
        else:
            if not opStack.isEmpty():
                while prec[opStack.peek()] >= prec[i]:
                    answer += opStack.pop()
                    if opStack.isEmpty():
                        break
            opStack.push(i)
    while not opStack.isEmpty():
        answer += opStack.pop()
    return answer

print(solution("A*B+C"))
print(solution("(A+B)*C"))
print(solution("A*B+C*D"))