#https://www.acmicpc.net/problem/3020
#백준 3020번 개똥벌레(이분탐색)
#import sys
#input = sys.stdin.readline

n, h = map(int, input().rstrip().split())
caves = [0]*h
for i in range(n):
    num = int(input().rstrip())
    if i%2 == 0:
        for j in range(h-1,h-1-num,-1):
            caves[j] += 1
    else:
        for j in range(0,num):
            caves[j] += 1
            
caves.sort()
cnt = 0
for cave in caves:
    if caves[0] == cave:
        cnt+=1
    else:
        break
        
print(caves[0], cnt)
'''
후 아무리 봐도 이 이상 줄일 수 있는 방법을 모르겠다.. 계속 시간초과가 발생한다.
'''