#https://www.acmicpc.net/problem/16235
#백준 16235번 나무 재테크
import sys
input = sys.stdin.readline
from collections import deque

def breedTree(trees, year):
    fifth = {}
    for i in range(n):
        for j in range(n):
            for c in range(len(trees[i][j])):
                if board[i][j] >= trees[i][j][c]:
                    if (trees[i][j][c]+1)%5 == 0 :
                        if (i,j) in fifth :
                            fifth[(i,j)] += 1
                        else:
                            fifth[(i,j)] = 1
                    board[i][j] -= trees[i][j][c]
                    trees[i][j][c] += 1
                else:
                    for r in range(c,len(trees[i][j])):
                        board[i][j] += (trees[i][j].pop())//2
                    break
    for i in range(n):
        for j in range(n):
            board[i][j] += nutrient[i][j]
            if (i,j) in fifth :
                for a,b in direction:
                    nx = i+a
                    ny = j+b
                    if nx < 0 or nx >= n or ny < 0 or ny >= n :
                        continue
                    for _ in range(fifth[(i,j)]):
                        trees[nx][ny].appendleft(1)

n, m, k = map(int, input().split())
nutrient = [list(map(int, input().split())) for _ in range(n)]
board = [[5]*n for _ in range(n)]
direction = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
trees = [[deque() for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

for year in range(k):
    breedTree(trees,year)

cnt = 0
for i in range(n):
	for j in range(n):
		cnt += len(trees[i][j])
print(cnt)