#https://www.acmicpc.net/problem/1292
#백준 1292번 쉽게 푸는 문제(구현)
a, b = map(int, input().split())
cnt = 1
check = 1
result = 0
for i in range(1, b+1):
    if cnt==0:
        check+=1
        cnt = check
    cnt-=1
    if i >= a:
        result+=check

print(result)