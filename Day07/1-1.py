#https://www.acmicpc.net/problem/1822 백준 차집합
#이분 탐색인데 시간 초과 발생 why?? sys 적용해도 시간초과 발생
a, b = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

arr_a.sort()

for i in arr_b:
    start = 0
    end = len(arr_a)
    while start < end:
        mid = (start+end)//2
        if arr_a[mid]== i:
            arr_a.remove(i)
        elif arr_a[mid] > i:
            end = mid
        elif arr_a[mid] < i:
            start = mid+1
            
if len(arr_a) == 0:
    print(0)
else:
    print(len(arr_a))
    for i in arr_a:
        print(i, end=" ")