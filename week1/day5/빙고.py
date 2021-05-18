def solution(board, nums):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] in nums:
                board[i][j] = 0
    
    for i in range(len(board)):
        if sum(board[i]) == 0:
            answer += 1
        temp = []
        for j in range(len(board)):
            temp.append(board[j][i])
        if sum(temp) == 0:
            answer += 1
    
    temp2 = []
    temp3 = []
    for i in range(len(board)):
        temp2.append(board[i][i])
        temp3.append(board[i][len(board)-i-1])
    if sum(temp2) == 0:
        answer += 1
    if sum(temp3) == 0:
        answer += 1
    print(board)
    return answer

board = [[6,15,17,14,23],[5,12,16,13,25],[21,4,2,1,22],[10,20,3,18,8],[11,9,19,24,7]]
nums = [15,7,2,25,9,16,12,18,5,4,10,13,20]

a = [[11,13,15,16],[12,1,4,3],[10,2,7,8],[5,14,6,9]]
b = [14,3,2,4,13,1,16,11,5,15]
print(solution(a, b))

# 세션 풀이

# 핵심은 빙고를 세기 위해 알아야 하는 키 요소는 인덱스를 가져가야한다는 것.
# 그렇다면 인덱스를 어떻게 담을것인가? -> 딕셔너리! 키의 유일성과 데이터 엑세스의 시간적 유리함
# 1. 빙고판에서 빙고 개수를 알기 위해 N X N을 알아야함

def solution(board, nums):
    answer = 0
    size = len(board)

    hor = [0] * size # 가로
    ver = [0] * size # 대각선
    diag = [0] * 2 # 대각선

    idx = {}
    # 이중 loop을 통해서 board -> (x,y)
    for i in range(size):
        for j in range(size):
            idx[board[i][j]] = (i,j) # 숫자를 키로 갖고 인덱스를 벨류로 설정
    
    # 'num'을 순회
    for elem in nums:
        y, x = idx[elem]
        if y == x: diag[0] += 1
        if y == size - x - 1: diag[1] += 1
        ver[x] += 1
        hor[y] += 1
    
    # counting
    return hor.count(size) + ver.count(size) + diag.count(size)





