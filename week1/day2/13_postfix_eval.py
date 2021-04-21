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


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []
    
    for i in tokenList:
        # 피연산자일때
        if type(i) is int:
            postfixList.append(i)
        # ( 일 때
        elif i == "(":
            opStack.push(i)
        # ) 일 때
        elif i == ")":
            while opStack.peek() != "(":
                postfixList.append(opStack.pop())
            opStack.pop()
        # 일반연산자일때
        else:
            if not opStack.isEmpty():
                while prec[opStack.peek()] >= prec[i]:
                    postfixList.append(opStack.pop())
                    if opStack.isEmpty():
                        break
            opStack.push(i)
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return postfixList


def postfixEval(tokenList):
    valStack = ArrayStack()

    for token in tokenList:
        #피연산자일때
        if type(token) is int:
            valStack.push(token)
        #연산자일때
        elif token == "*":
            b = valStack.pop()
            a = valStack.pop()
            valStack.push(a*b)
        elif token == "/":
            b = valStack.pop()
            a = valStack.pop()
            valStack.push(a/b)
        elif token == "+":
            b = valStack.pop()
            a = valStack.pop()
            valStack.push(a+b)
        elif token == "-":
            b = valStack.pop()
            a = valStack.pop()
            valStack.push(a-b)
    return valStack.pop()


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val

print(solution("12*3-20+15*3"))