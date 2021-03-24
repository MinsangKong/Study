#https://www.acmicpc.net/problem/17952
#백준 17952번 과제는 끝나지 않아!(구현)
#import sys
#input = sys.stdin.readline
from collections import deque 
task = deque()
time = deque()
score = 0
n = int(input())
for i in range(n):
    x = list(map(int,input().split()))
    if x[0] == 1:
        task.append(x[1])
        time.append(x[2])
    else:
        pass 
    if time:
        time[-1] -= 1 
        if time[-1] == 0:
            time.pop()
            score+=task.pop()
print(score)
'''
입력이 달라지는 경우에는 애초부터 입력을 list로 받으면 편리하다.
'''