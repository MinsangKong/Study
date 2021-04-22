#https://www.acmicpc.net/problem/2075
#백준 2075번 N번째 큰 수(정렬)
#import sys
#input = sys.stdin.readline
n = int(input())
board = [[0]*n for _ in range(n)]
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        board[j][i] = data[j]
result = 0
for i in range(n):
    check = 0
    idx = 0
    for j in range(n):
        if board[j][-1] > check:
            idx = j
            check = board[j][-1]
    result = board[idx].pop()
    
print(result)

'''
내가 생각한 방식은 메모리 초과가 발생했다... 차선책으로 가장 큰 수 N개의 수를 저장
하는 배열만 만들어서 풀어야 했다.
'''