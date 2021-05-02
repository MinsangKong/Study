#Q29 공유기 설치
#import sys
#input = sys.stdin.readline

n, c = map(int, input().split())
homes = []
for i in range(n):
    home = int(input())
    homes.append(home)

homes.sort()
start = 0
end = homes[-1]-1
result = 0
while start <= end:
    mid = (start+end)//2
    cnt = 1
    point = homes[0]  
    for i in range(1,n):
        if homes[i]-point >= mid:
            cnt+=1
            point = homes[i]
    print(start,mid,end)
    if cnt >= c:
        result = mid
        start = mid+1
    else:
        end = mid -1
        
print(result)