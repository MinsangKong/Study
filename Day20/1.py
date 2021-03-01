import sys

#넘모 빡센 문제(분석해서 다시 풀어보기)
def binary_search(start, end):
    while start < end:
        #print(start, end)
        mid = (start+end)//2  # alchol
        if check(mid): # 이 알콜수치 최댓값으로 만족도가 채워진다면, 최댓값을 줄여야지
            end = mid - 1
        else:  # 이 알콜 수치 최댓값으로는 만족도가 안채워진다면 안되는 값 최댓값의 후보다.
            if start == mid: # 근데 스타트와 미드가 같다면, 무한 루프를 도니까
                if check(end): # 엔드값에서 실행이 되면 가장 큰 안되는 값은 스타트
                    end = mid
                else: # 엔드값에서 실행이 안되면, 가장 큰 안되는 값은 엔드
                    mid = end
            start = mid #그리고 스타트 값을 미드값으로 바꿔준다.
    if start == min_alch and check(start):  # 최솟값일 때 되고, 최솟값 + 1일 때는 안된다면 => 최솟값 출력
        print(start)
    elif start == max_alch and not check(start):  # 최댓값일 때 안된다면, 그냥 안된다는 것
        print(-1)
    elif start == max_alch and check(start):  # 최댓값일 때만 되면
        print(start)
    #elif start == min_alch and not check(start):
     #   print(-1)
    else:
        print(start+1)


def check(mid):
    #print('check',mid)
    global kind, day, sum_taste
    s = 0
    cnt = 0
    for i in range(kind):
        if cnt == day:
            break
        if beer[i][1] <= mid:
            s += beer[i][0]
            cnt += 1
    #print(cnt,s)
    #print(not(cnt != day or s < sum_taste))
    if cnt != day or s < sum_taste:
        return False
    else:
        return True


day, sum_taste, kind = map(int, input().split())
min_alch = 10000000000
max_alch = 0
beer = []
for _ in range(kind):
    taste, alch = map(int, sys.stdin.readline().split())
    beer.append((taste, alch))
    if alch > max_alch:
        max_alch = alch
    if alch < min_alch:
        min_alch = alch
beer.sort(key=lambda x: -x[0])
#print(beer)
binary_search(min_alch,max_alch)