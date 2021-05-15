#https://www.acmicpc.net/problem/1920
#백준 1920번 수 찾기(정렬,이분 탐색)
#import sys
#input = sys.stdin.readline

n = int(input())
num1 = set(list(map(int, input().split())))
m = int(input())
num2 = list(map(int, input().split()))

for i in num2:
    if i in num1:
        print(1)
    else:
        print(0)