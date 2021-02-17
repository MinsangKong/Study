#https://www.acmicpc.net/problem/14916
#백준 14916번 거스름돈
n = int(input())
arr = [0]*100001

arr[2] = 1
arr[4] = 2
arr[5] = 1
for i in range(2, n+1):
    if arr[i-2] > 0 and arr[i-5] > 0:
        arr[i] = min(arr[i-2]+1, arr[i-5]+1)
    elif arr[i-2] > 0:
        arr[i] = arr[i-2]+1
    elif arr[i-5] > 0:
        arr[i] = arr[i-5]+1
        
if arr[n] == 0:
    print(-1)
else:
    print(arr[n])