def solution(grid):
    n, m = len(grid), len(grid[0])
    answer = []
    visit = [[[0]*4 for _ in range(m)] for _ in range(n)]
    dir = [[0,1], [1,0], [0,-1], [-1,0]]
    for i in range(n):
        for j in range(m):
            for k in range(4):
                if visit[i][j][k]:
                    continue
                cnt = 0
                x, y, d = i, j, k
                while not visit[x][y][d]:
                    visit[x][y][d] = True
                    cnt += 1
                    x += dir[d][0]
                    y += dir[d][1]
                    x = (x + n) % n
                    y = (y + m) % m
                    if grid[x][y] == 'L':
                        d = (d + 3) % 4
                    elif grid[x][y] == 'R':
                        d = (d + 1) % 4
                answer.append(cnt)
    answer.sort()
    return answer