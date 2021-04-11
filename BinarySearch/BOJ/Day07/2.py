#https://www.acmicpc.net/problem/14921 용액 합성하기
#이분 탐색으로 감이 안잡혀서 이중 포인터 활용
n = int(input())
arr = list(map(int, input().split()))
minv=100,000,000
left=0
right=n-1
while left<right:
    sum=arr[left]+arr[right]
    if abs(sum)<abs(minv): #최소값 갱신
        minv=sum
    if sum < 0:
        left+=1 #음수가 0에 가깝게 하려면 left증가
    else:
        right-=1 #양수가 0에 가깝게 하려면 right감소

print(minv)