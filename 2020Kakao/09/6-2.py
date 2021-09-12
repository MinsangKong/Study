def solution(board, skill):
    answer = 0
    n = len(board)
    m = len(board[0])
    prepixSum = [[0]*(m+1) for _ in range(n+1)]

    for k in range(len(skill)):
        sort, r1, c1, r2, c2, degree = skill[k]
        if sort == 2:
            prepixSum[r1][c1] += degree
            prepixSum[r2+1][c2+1] += degree
            prepixSum[r1][c2+1] -= degree
            prepixSum[r2+1][c1] -= degree
        else:
            prepixSum[r1][c1] -= degree
            prepixSum[r2+1][c2+1] -= degree
            prepixSum[r1][c2+1] += degree
            prepixSum[r2+1][c1] += degree

    for i in range(n):
        for j in range(m):
            if i > 0 and j > 0:
                prepixSum[i][j] += prepixSum[i-1][j]+prepixSum[i][j-1]-prepixSum[i-1][j-1]
            elif i > 0:
                prepixSum[i][j] += prepixSum[i-1][j]
            elif j > 0 :
                prepixSum[i][j] += prepixSum[i][j-1]

    
    for i in range(n):
        for j in range(m):
            board[i][j] += prepixSum[i][j] 
            if board[i][j] > 0 :
                answer += 1

    for i in range(n):
        print(*board[i])
    return answer

board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
print(solution(board, skill))