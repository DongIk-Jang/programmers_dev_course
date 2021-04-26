# def solution(s):
#     data = list(s)
#     answer = set()
#     if len(s) == 1:
#         return 1
    
#     if len(s) % 2 == 1:
#         for i in range(1,len(data)-1):
#             count = 1
#             upper = i+1
#             lower = i-1
#             while data[lower] == data[upper]:
#                 count += 2
#                 upper += 1
#                 lower -= 1
#                 if upper >= len(data) or lower < 0:
#                     break
#             answer.add(count)
#     else:
#         for i in range(len(data)-1):
#             count = 0
#             upper = i+1
#             lower = i
#             while data[lower] == data[upper]:
#                 count += 2
#                 upper += 1
#                 lower -= 1
#                 if upper >= len(data) or lower < 0:
#                     break
#             answer.add(count)
        
#     return max(answer)


def solution(s):
    data = list(s)
    answer = set()
    if len(s) == 1:
        return 1
    if len(s) == 2:
        if s[0] == s[1]:
            return 2
        else:
            return 1
        
    for i in range(1,len(data)-1):
        if data[i] == data[i+1]:
            count = 0
            upper = i+1
            lower = i
            while data[lower] == data[upper]:
                count += 2
                upper += 1
                lower -= 1
                if upper >= len(data) or lower < 0:
                    break
            answer.add(count)
        else:
            count = 1
            upper = i+1
            lower = i-1
            while data[lower] == data[upper]:
                count += 2
                upper += 1
                lower -= 1
                if upper >= len(data) or lower < 0:
                    break
            answer.add(count)
    return max(answer)

print(solution("keceabcdcbadabcdcblsi"))
print(solution("aaaoaabbaaoaaal"))
print(solution("abccccbalgik"))