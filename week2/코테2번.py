# def solution(arr):
#     data = sorted(arr)
#     stack = []
#     answer = []
#     while True:
#         a = data.pop()
#         if (stack[-1][1]-stack[-1][0]) < (a[1]-a[0]):
#             answer.append(stack.pop())
#     for i in data:
#         temp = i[1]


    
    
#     answer = 0
#     return answer


# def solution(arr):
#     data = sorted(arr)
#     s = {}
#     for i in data:
#         s[i[0]] = s.get(i[0], [])
#         s[i[0]].append(i[1])
    
#     print(s)
#     stack = []
#     idx = 0
#     while idx < len(data):
#         data[idx] 

# # data = [[1, 2], [2, 4], [2, 2]]
# # data = sorted(data)
# # s = {}
# # for i in data:
# #     s[i[0]] = s.get(i[0], [])
# #     s[i[0]].append(i[1])
# # print(s[1])



# data = [[1, 2], [2, 4], [2, 2]]
# data = [[1, 4], [2, 6], [4, 7]]
# data = sorted(data)
# stack = []
# stack.append(data[0])
# i = 1
# temp = data[0][1]
# for i in range(1, len(data)):
#     print(data[i])
#     print(temp)
#     if data[i][0] == temp:
#         stack.append(data[i])
#         temp = data[i][1]
# print(stack)

# s = set()
# s.add(1)
# s.add(10)
# print(min(s))


# def solution(arr):
#     data = sorted(arr)
#     answer = set()
#     stack = []
#     while data:
#         for i in data:
#             if len(stack) == 0:
#                 stack.append(i)
#             else:
#                 if i[0] == stack[-1][1]:
#                     stack.append(i)
#         answer.add(len(stack))
#         data = data[1:]
    
#     return max(answer)

# arr = [[1, 2], [2, 4], [2, 2]]
# print(solution(arr))


# data = [[1, 2], [2, 4], [2, 2]]


def dfs(graph, v, visited, answer):
    visited[v] = True
    answer.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited, answer)

def solution(arr):
    answer = []
    data = sorted(arr)
    graph = [[] for i in range(100000)]
    visited = [False] * 100000
    for i, j in data:
        graph[i].append(j)
    dfs(graph, 1, visited, answer)
    print(answer)
    return len(answer)

# data = [[1, 2], [2, 4], [2, 2]]
# # data = [[1, 4], [2, 6], [4, 7]]
# print(solution(data))



# s = {}
# for i in data:
#     s[i[0]] = s.get(i[0], [])
#     s[i[0]].append(i[1])
# print(s[1])

# stack = []
# while stack:
#     stack.append(data[-1])

def solution(arr):
    answer = []
    graph = {}
    data = data = sorted(arr)
    for i in data:
        graph[i[0]] = graph.get(i[0], [])
        graph[i[0]].append(i[1])
    for r in graph:
        graph[r].sort(reverse=True)
    
    for i in graph:
        answer.append(dfs(graph, i))
    return max(answer)
    
def dfs(graph, v):
    count = 0
    temp = []
    stack = []
    stack += graph[v]
    while len(stack) > 0:
        print(stack)
        top = stack.pop()
        temp.append(top)
        if top not in graph or len(graph[top]) == 0:
            continue
        else:
            stack += graph[top]
            count += 1
        
    return count

data = [[1, 2], [2, 4], [2, 2]]
# data = [[1, 4], [2, 6], [4, 7]]
print(solution(data))