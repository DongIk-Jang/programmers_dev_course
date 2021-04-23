def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                return False
            else:
                t = stack.pop()
                if t != '(':
                    return False
    return len(stack) == 0

def solution2(s):
    c = 0
    for x in s:
        if x == '(':
            c += 1
        else:
            c -= 1
        if c < 0:
            return False
    return c == 0

print(solution2(")()("))