# 일단 문제에서 n이 주어지는 범위가 최대 12이기 때문에 모든 경우의 수를 다 해보라는 의도인 듯 하다..
# 안될것같은 애들은 가지치는 방법 백트랙킹이라는 방법으로 진행된다 (DFS에서 가지치기)

# DFS 사용 (Stack, Recursive)
def n_queen(lst, row, n):
    # (row번째 행을 체크하는 재귀함수)
    # lst : 어떤 열에 담았는지 두는 리스트
    # row : 현재 행 
    # n : 체스판 사이즈(NxN), 종료조건
    count = 0
    if row == n:
        return 1
    for col in range(n):
        lst[row] = col # 인덱스 : row, 값은 col
        for i in range(row): # 0 ~ 바로 전까지!
            # 열 체크
            if lst[i] == lst[row]:
                break
            # 대각선 체크 (우상향, 우하향)
            if (lst[i] + i == lst[row] + row):
                break
            if (lst[i] + i == lst[row] + row):
                break
            # 근데 이거 한줄로도 가능하다!
        else:
            count += n_queen(lst, row + 1, n)
    return count

def solution(n):

    answer = 0
    return n_queen([-1]*n, 0, n)