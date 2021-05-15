import heapq
import sys

N = int(input())

heap = []

for _ in range(N):
    nums = list(map(int,sys.stdin.readline().split()))

    if not heap: 
        for num in nums:
            heapq.heappush(heap,num)
    else:
        for num in nums:
            if heap[0] < num:
                heapq.heappush(heap,num)
                heapq.heappop(heap)
    
print(heap[0])
'''
heapq에 처음에 넣는 코드를 굳이 data안에서 체크 하지 말고 if not heap을 활용해서
했었으면 매번 i==0을 체크하지 않아도 괜찮기 때문에 더 빨라졌을 것 같다.
'''