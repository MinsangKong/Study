#https://www.acmicpc.net/problem/1749
#백준 1749번 점수따먹기(누적합)
#import sys
#input = sys.stdin.readline

n, m = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = dp[i-1][j]+dp[i][j-1]+nums[i-1][j-1]-dp[i-1][j-1]
        
#result의 최솟값은 200x200칸에 모두 -10000이 들어 있는 경우인 -4억 구하기 귀찮으면 -float('inf')
result = -400000001
for i in range(1,n+1):
    for j in range(1,m+1):
        for x in range(i,n+1):
            for y in range(j,m+1):
                result = max(result, dp[x][y]-dp[x][j-1]-dp[i-1][y]+dp[i-1][j-1])
                
print(result)
'''
https://hbj0209.tistory.com/142 참고,
dp를 통해 2차원 배열을 구했지만 그 다음부터 막혔다... 찾아보니까 구한 dp를 기준으로
그 안에서 4중 포문으로 완전 탐색을 돌리면 답을 알 수 있었다... 알고보니 허망하다
A B C 
D E F
G H I
부분행렬 안에 있는 정수들의 합을 구하는 것도 누적합을 구하는 것과 비슷하다.
위의 그림에서 (E+F+H+I)를 구하고 싶으면 I까지의 누적합(A+B+C+...+H+I)에서 C까지의 
누적합(A+B+C)과 G까지의 누적합(A+D+G)을 빼 준 뒤겹치는 부분인 A를 더해주면 된다.
'''