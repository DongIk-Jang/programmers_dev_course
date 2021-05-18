def solution(tickets):
    routes = {}
    for t in tickets:
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
    # 매번 가장 빠른 알파벳 순으로 확인해야 하기 때문에 정렬해줄 필요
    # 파이썬에서 list형은 뒤에서부터 추가하고 삭제하는 것이 가장 빠르기 때문에
    # 알파벳의 역순으로 정렬, 시간 복잡도는 N log N
    for r in routes:
        routes[r].sort(reverse=True)
    print(routes)
    stack = ["ICN"]
    path = []
    while len(stack) > 0:
        top = stack[-1]
        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[top][-1])
            routes[top].pop()
    return path[::-1]


a = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
routes = {}
for t in a:
    routes[t[0]] = routes.get(t[0], []) + [t[1]]
print(routes)
solution(a)