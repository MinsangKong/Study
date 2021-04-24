#https://www.acmicpc.net/problem/10815
#백준 10815번 숫자 카드(이분 탐색)
#import sys
#input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))
result = []
cards.sort()
for i in check:
    flag = False
    start = 0
    end = n-1
    while start <=end:
        mid = (start+end)//2
        if cards[mid] == i:
            flag = True
            break
        elif cards[mid] > i:
            end = mid-1
        else:
            start = mid+1
    if flag:
        result.append(1)
    else:
        result.append(0)
print(*result)
'''
심오한 문제. 문제 조건에서 A에는 중복된 숫자가 없다고 말해서 정렬한 뒤 이분탐색을 
적용해서 풀었는데 빠르게 푼 사람들은 모두 set을 활용해서 풀었다...
'''