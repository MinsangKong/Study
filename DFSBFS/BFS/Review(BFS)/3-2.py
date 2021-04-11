import sys
input = sys.stdin.readline
print = sys.stdout.write
def BOJ4963():
    while True:
        w, h = map(int, input().split())
        if w==0 and h==0:
            break
        MAP = [[*map(int,input().split())] for _ in range(h)]
        def BFS(i, j):
            MAP[i][j]=0
            stack = [(i,j)];f=0
            while f<len(stack):
                x, y = stack[f];f+=1
                for (ii,jj) in [(x-1, y-1),(x-1, y),(x-1, y+1),(x, y-1),(x, y+1),(x+1, y-1),(x+1, y),(x+1, y+1)]:
                    if 0<=ii<h and 0<=jj<w and MAP[ii][jj]:
                        stack.append((ii,jj))
                        MAP[ii][jj] = 0
        cnt = 0
        for i in range(h):
            for j in range(w):
                if MAP[i][j]:
                    BFS(i, j);cnt+=1
        print("{}\n".format(cnt))
BOJ4963()