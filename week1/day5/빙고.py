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