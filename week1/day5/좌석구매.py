# def solution(seat):
#     # temp = []
#     # count = 0
#     # for i in seat:
#     #     if i in temp:
#     #         count += 1
#     #     temp.append(i)
#     # answer = len(seat) - count
#     # return answer
#     s = {}
#     a = []
#     for i in seat:
#         a.append(str(i))
#     for j in a:
#         s[j] = s.get(j)
#     return len(s)

# a = [[1,1],[2,1],[1,2],[3,4],[2,1],[2,1]]
# b = set(map(str, a))
# print(len(b))

def solution(seat):
    s = set(map(str, seat))
    return len(s)
