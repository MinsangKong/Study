#https://www.acmicpc.net/problem/2170
#백준 2170번 선 긋기(정렬)
#import sys
#input = sys.stdin.readline

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
    
board.sort(key = lambda x : x[0])
check = board[0][1]
result = board[0][1]-board[0][0]

for i in range(1,n):
    if check < board[i][0]:
        check = board[i][1]
        result += board[i][1]-board[i][0]
    elif check < board[i][1]:
        result+=board[i][1]-check
        check = board[i][1]
        
print(result)

'''
가장 직관적인 방법으로 풀었는데도 시간초과가 발생했다... 후...
정렬할 때 그냥 sort()로 하면 시간초과가 발생했다. 나는 당연히 그냥 정렬하면 앞의 값만
기준으로 정렬이 될 줄 알았는데 잘못 판단했다. 앞으로는 2차원 배열이 나오면 무조건
lambda x를 사용해서 정렬해야겠다...
'''