# 자물쇠
# 21.06.19

import sys
from collections import deque
rd = sys.stdin.readline
INF = int(1e9)


def main():
    t = int(rd())

    for i in range(1, t + 1):
        print(f"#{i} {solution()}")

def getUpCount(arr, row, col, k, upTable):
    up, nextIdx = 0, row

    while arr[nextIdx][col] != 1:
        up += 1
        nextIdx = (nextIdx - 1) % k
    
    upTable[row][col] = up

def getDownCount(arr, row, col, k, downTable):
    down, nextIdx = 0, row

    while arr[nextIdx][col] != 1:
        down += 1
        nextIdx = (nextIdx + 1) % k
    
    downTable[row][col] = down



def solution():
    n, k = map(int, rd().split())

    lock = [[0] * n for _ in range(k)]
    upTable = [[-1] * n for _ in range(k)]
    downTable = [[-1] * n for _ in range(k)]
    maxOne = 0

    for i in range(k):
        line = rd().rstrip()
        for j in range(n):
            lock[i][j] = int(line[j])
            if lock[i][j] == 1:
                upTable[i][j] = downTable[i][j] = 0
        sumLine = sum(lock[i])
        maxOne = sumLine if sumLine > maxOne else maxOne

    if maxOne == n:
        return 0

    countClickList = [INF] * k

    countClick = 0
    for j in range(n):
        if lock[0][j] == 1: continue
        getUpCount(lock, 0, j, k, upTable)
        getDownCount(lock, 0, j, k, downTable)
        countClick += min(upTable[0][j], downTable[0][j])
    countClickList[0] = countClick

    countClick = 0

    answer = INF
    for i in range(1, k):
        countClick = 0
        for j in range(n):
            if lock[i][j] == 1: continue

            if lock[i - 1][j] == 1:
                upTable[i][j] = 1
                getDownCount(lock, i, j, k, downTable)
            else:
                upTable[i][j] = upTable[i - 1][j] + 1

                if lock[(i + 1) % k][j] == 1:
                    downTable[i][j] = 1
                else:
                    downTable[i][j] = downTable[i - 1][j] - 1
            
            countClick += min(upTable[i][j], downTable[i][j])
        if countClick < answer:
            answer = countClick


    return answer



main()