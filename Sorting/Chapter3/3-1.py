#026번 카드 정렬하기
#import sys
#input = sys.stdin.readline
import heapq

n = int(input())
cards = []
for _ in range(n):
    num = int(input())
    heapq.heappush(cards,num)
    
if n == 1:
    print(0)
else:
    result = heapq.heappop(cards)+heapq.heappop(cards)
    point = 0
    last = result
    while cards:
        card1 = heapq.heappop(cards)
        if last > card1:
            if len(cards) >= 1:
                card2 = heapq.heappop(cards)
                if last+card1 > card1+card2:
                    point+=card1+card2
                    heapq.heappush(cards,card1+card2)
                else:
                    heapq.heappush(cards,card2)
                    last +=card1
                    result+=last
            else:
                last += card1
                result+=last
        else:
            last += card1
            result+=last
    print(result+point)