# DFS 활용한 방문 함수
# def dfs(x,y,n,m,image,d):
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False
#     if image[x][y] == d:
#         image[x][y] = 0
#         dfs(x-1, y,n,m,image,d)
#         dfs(x, y-1,n,m,image,d)
#         dfs(x+1, y,n,m,image,d)
#         dfs(x, y+1,n,m,image,d)
#         return True
#     return False

from collections import deque

# def solution(n, m, image):
#     def dfs(x,y,d):
#         if x <= -1 or x >= n or y <= -1 or y >= m:
#             return False
#         if image[x][y] == d:
#             image[x][y] = 0
#             dfs(x-1, y,d)
#             dfs(x, y-1,d)
#             dfs(x+1, y,d)
#             dfs(x, y+1,d)
#             return True
#         return False
    
    
    
    
#     answer = 0
#     for i in range(n):
#         for j in range(m):
#             d = image[i][j]
#             if image[i][j] != 0 and dfs(i,j,d) == True:
#                 answer += 1
#     return answer

# images = [[1, 2, 3], [3, 2, 1]]
# print(solution(2,3,images))

def bfs(n, m, image):
    answer = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    x = 1
    y = 1
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            d = image[nx][ny]
            if image[nx][ny] == d:
                image[nx][ny] = 0
                queue.append((nx,ny))
                answer += 1
                
    return answer

images = [[1, 2, 3], [3, 2, 1]]
print(bfs(2,3,images))