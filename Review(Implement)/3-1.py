#https://www.acmicpc.net/problem/7568
#백준 7568번 덩치(구현)
#import sys
#input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
result = []
for i in arr:
    cnt = 1
    for j in arr:
        if i[0] < j[0] and i[1] < j[1]:
            cnt+=1
    result.append(cnt)
    
print(*result)