from collections import deque
def solution(grid, clockwise):
    length = len(grid)
    grid = [deque(grid[i]) for i in range(length)]
    board = ["" for _ in range(length)]
    limit = length*2-1
    if clockwise :
        idx = length-1
        while idx >= 0:
            cur = length-1
            while len(board[idx]) < limit:
                if limit-len(board[idx]) == 1 :
                    board[idx]+= grid[cur].pop()
                else:
                    if len(grid[cur]) == 1 :
                        a = grid[cur].pop()
                        board[idx] += a
                        cur -= 1
                    else:
                        a = grid[cur].pop()
                        b = grid[cur].pop()
                        board[idx] += a+b
                        cur -= 1
            idx -= 1
            limit -= 2
    else:
        idx = length-1
        start = 0
        while idx >= 0:
            cur = start 
            while len(board[idx]) < limit:
                if limit-len(board[idx]) == 1 :
                    board[idx]+= grid[cur].popleft()
                else:
                    if len(grid[cur]) == 1 :
                        a = grid[cur].popleft()
                        board[idx] += a
                        cur += 1
                    else:
                        a = grid[cur].popleft()
                        b = grid[cur].popleft()
                        board[idx] += b+a
                        cur += 1
            idx -= 1
            start += 1
            limit -= 2
    return board

print(solution(["1", "abc", "23456", "defghij", "789123456"],False))