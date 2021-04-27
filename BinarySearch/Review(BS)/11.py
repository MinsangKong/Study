#https://www.acmicpc.net/problem/2470
#백준 2470번 두 용액(이분탐색,더블 포인터)
#import sys
#input = sys.stdin.readline

n = int(input().rstrip())
solutions = list(map(int, input().rstrip().split()))

solutions.sort()
start = 0
end = n-1
rl = start
rr = end
point = abs(solutions[start]+solutions[end])
while start < end:
    check = solutions[start]+solutions[end]
    if point > abs(check):
        point = abs(check)
        rl = start
        rr = end
        if check == 0:
            break
    if check < 0:
        start+=1
    else:
        end-=1
print(solutions[rl],solutions[rr])
'''
스페셜 저지라서 그런가 result 배열에 값을 넣는 식으로 하면 중간에 틀렸습니다가 나온다.
그래서 rr,rl 변수에 인덱스를 넣어주는 식으로 하니까 정답처리되었다. 아무리 봐도 알고리즘이
맞는 데 계속 틀려서 너무 어이가 없었다.
'''