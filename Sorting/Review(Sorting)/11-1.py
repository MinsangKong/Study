#https://www.acmicpc.net/problem/1946
#백준 1946번 신입 사원(정렬)
#import sys
#input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    info = []
    for i in range(n):
        info.append(list(map(int, input().split())))
    
    cnt = 1
    info.sort()
    check = info[0][1]
    for i in range(1,n):
        if info[i][1] < check:
            cnt+=1
            check = info[i][1]
    print(cnt)