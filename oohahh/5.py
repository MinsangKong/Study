def solution(rows, columns):
    board = [[0]*columns for _ in range(rows)]
    cnt = rows*columns-1
    visited = [[0]*columns for _ in range(rows)]
    board[0][0] = 1 
    visited[0][0] = 1
    q = [[0,0,1]]
    while q :
        x, y, last = q.pop()

        if cnt == 0 :
            break

        if last %2 == 1 :
            y = (y+1)%columns
        else:
            x = (x+1)%rows

        if not visited[x][y]:
            board[x][y] = last+1
            visited[x][y] = 1
            cnt -= 1
            q.append([x,y,board[x][y]])
        elif board[x][y]%2 == (last+1)%2:
            break
        else:
            board[x][y] = last+1
            q.append([x,y,board[x][y]])
    return board