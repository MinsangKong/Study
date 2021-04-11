import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(n, m, maze) :
    qu = [(0,0,1)]
    visited = [[False for c in range(m)] for r in range(n)]
    while len(qu) :
        cx,cy,ci = qu.pop(0)
        if cx == n-1 and cy == m-1 :
            return ci
        if visited[cx][cy] :
            continue
        visited[cx][cy] = True
        if 0 < cx and maze[cx-1][cy] == '1' and not visited[cx-1][cy] :
            qu.append((cx-1, cy, ci+1))
        if cx < n-1 and maze[cx+1][cy] == '1' and not visited[cx+1][cy] :
            qu.append((cx+1, cy, ci+1))
        if 0 < cy and maze[cx][cy-1] == '1' and not visited[cx][cy-1] :
            qu.append((cx, cy-1, ci+1))
        if cy < m-1 and maze[cx][cy+1] == '1' and not visited[cx][cy+1] :
            qu.append((cx, cy+1, ci+1))
    return -1

n, m = map(int, input().split())
maze = [input() for i in range(n)]
print(solve(n, m, maze))