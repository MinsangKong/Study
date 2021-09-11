def solution(board, skill):
    answer = 0
    prepixSum = dict()

    for k in range(len(skill)):
        sort, r1, c1, r2, c2, degree = skill[k]
        keyword = str(r1)+' '+str(c1)+' '+str(r2)+' '+str(c2)
        if sort == 2:
            if keyword in prepixSum:
                prepixSum[keyword] += degree
            else:
                prepixSum[keyword] = degree
        else:
            if keyword in prepixSum:
                prepixSum[keyword] -= degree
            else:
                prepixSum[keyword] = -degree

    for keyword in prepixSum:
        r1, c1, r2, c2 = keyword.split(' ')
        for i in range(int(r1), int(r2)+1):
            for j in range(int(c1), int(c2)+1):
                board[i][j] += prepixSum[keyword]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] > 0 :
                answer += 1
    return answer

board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
print(solution(board, skill))