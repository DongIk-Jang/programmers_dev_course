# 세션 풀이


def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    return (solution(n-1) + solution(n-2)) % 1000000007

# 와 이게 피보나치라고?
# n=1이면 경우 1개
# n=2이면 경우 2개
# n=3 이면 경우 3개
# 완전 재귀적인 문제다!
# n=3 이면 n=2일때를 불러와서 거기에 추가로 1칸 더 넣는 방식으로..!
# n이 1, 2 인 경우가 기저조건으로 들어감

def solution(n):
    dp = [1,2] # 1일때랑 2일때
    for i in range(2,n):
        dp.append((dp[i-1] + dp[i-2]) % 1000000007)
    return dp[-1]
    