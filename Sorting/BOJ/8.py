#https://www.acmicpc.net/problem/2217
#백준 2217번 로프(정렬)
import sys
input=sys.stdin.readline

n = int(input())
rope = []
for i in range(n):
    rope.append(int(input()))
rope.sort(reverse=True)
w = 0
for i in range(n):
    if (i+1)*rope[i] >= w:
        w=rope[i]*(i+1) 
print(w)