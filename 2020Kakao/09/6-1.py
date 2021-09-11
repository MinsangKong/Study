def solution(board, skill):
    answer = 0

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
    return answer