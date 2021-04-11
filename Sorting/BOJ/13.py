#https://www.acmicpc.net/problem/2870
#백준 2870번 수학숙제(정렬)
import sys

def solution():
    T = int(sys.stdin.readline())
    arr = []
    for _ in range(T):
        string = sys.stdin.readline().strip()

        temp = ''
        for j in range(len(string)):

            if '0' <= string[j] <= '9':
                temp += string[j]
            else:
                if temp:
                    arr.append(int(temp))
                temp = ''
        if temp:
            arr.append(int(temp))

    arr.sort()
    for i in arr: print(i)

solution()