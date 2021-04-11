#https://www.acmicpc.net/problem/1300
#백준 1300번 K번째 수(그리디)
n = int(input()) 
k = int(input()) 
s, e = 1, k 
while s <= e: 
    m = (s+e)//2 
    cnt = 0 
    for i in range(1, n+1): 
        cnt += min(n, m//i) 
    if cnt < k:
        s = m+1 
    else: 
        e = m-1 
print(s)