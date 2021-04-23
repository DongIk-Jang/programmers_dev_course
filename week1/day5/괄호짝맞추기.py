def solution(s):
    match = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    stack = []
    for i in s:
        if i in '({[':
            stack.append(i)
        elif i in match:
            if len(stack) == 0:
                return False
            else:
                t = stack.pop()
                if t != match[i]:
                    return False
    return len(stack) == 0