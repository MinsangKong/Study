#https://www.acmicpc.net/problem/2012
#백준 2012번 등수 매기기(정렬)
#import sys
#input = sys.stdin.readline
n = int(input())
grade = []
for i in range(n):
    grade.append(int(input()))
grade.sort()
result = 0
for i in range(n):
    result+=abs(grade[i]-i-1)
    
print(result)
'''
list에 append하는 방식보다 입력받을 때 grade = [int(input()) for i in range(n)]하는
방식이 근소하게 빨랐다.
'''