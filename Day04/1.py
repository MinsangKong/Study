#https://www.acmicpc.net/problem/2110 공유기 설치
n,c = map(int,input().split()) #문제의 관점은 좌표의 차이라서 굉장히 오래걸림

house = []
for _ in range(n):
    x = int(input())
    house.append(x)

house.sort()

# 가장 낮은 좌표와 그 다음으로 낮은 좌표의 차이로 하면 실패. why???
start = 1
# 가장 높은 좌표와 가장 낮은 좌표의 차이
end = house[-1] - house[0]

result = 0

while (start <= end):
    mid = (start+end)//2 # 해당 gap
    old = house[0]
    count = 1

    for i in range(1, len(house)):
        if house[i] >= old+mid: # gap 이상
            count+=1
            old = house[i]
    
    if count < c:
        end = mid - 1
    else:
        start = mid + 1
        result = mid
        
print(result)