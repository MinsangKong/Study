def solution(board, skill):
    answer = 0
    n = len(board)
    m = len(board[0])
    for k in range(len(skill)):
        sort, r1, c1, r2, c2, degree = skill[k]
        if sort == 1:
            for i in range(r1,r2+1):
                for j in range(c1,c2+1):
                    board[i][j] -= degree
        else:
            for i in range(r1,r2+1):
                for j in range(c1,c2+1):
                    board[i][j] += degree

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] > 0 :
                answer += 1
    for i in range(n):
        print(*board[i])
    return answer

board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
print(solution(board, skill))