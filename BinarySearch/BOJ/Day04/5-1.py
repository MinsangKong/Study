#https://www.acmicpc.net/problem/2003 수들의 합2
n, m = map(int, input().split()) #맨 처음에 생각한 방법, but 시간 초과
arr = list(map(int, input().split())) 
cnt = 0 
for i in range(n):
    total = 0 
    for j in range(i, n):
        total += arr[j]
        if total == m:
            cnt += 1 
            break 
        elif total > m:
            break 
            
print(cnt)