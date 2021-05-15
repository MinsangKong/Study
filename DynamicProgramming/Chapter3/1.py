#Q31 금광
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    boards = list(map(int, input().split()))
    cave = [[0]*m for _ in range(n)]
    
    for i in range(len(boards)):
        a, b = i//m, i%m
        cave[a][b] = boards[i]
    
    for j in range(1,m):
        for i in range(n):
            if i == 0:
                low = 0
            else:
                low = cave[i-1][j-1]
            if i == n-1:
                high = 0
            else:
                high = cave[i+1][j-1]
            medium = cave[i][j-1]
            cave[i][j] = cave[i][j]+max(low,medium,high)
    result = 0
    for i in range(n):
        result = max(result, cave[i][m-1])
    print(cave)
    print(result)
        