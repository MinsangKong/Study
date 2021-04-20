#https://www.acmicpc.net/problem/1302
#백준 1302번 베스트 셀러(정렬)
#import sys
#input = sys.stdin.readline

n = int(input())
store = []
for _ in range(n):
    store.append(input())
    
store.sort()
check1 = 1
check2 = 0
result = ""
for i in range(1,n):
    if store[i] == store[i-1]:
        check1+=1
    else:
        if check2 < check1:
            check2 = check1
            result = store[i-1]
        check1=1
if check2 < check1:
    print(store[-1])
else:
    print(result)