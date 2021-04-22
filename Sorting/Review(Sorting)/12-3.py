#import sys
#input = sys.stdin.readline
import heapq
n = int(input())
heap = []
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if i == 0:
            heapq.heappush(heap,data[j])
        elif heap[0] < data[j]:
            heapq.heappop(heap)
            heapq.heappush(heap, data[j])

print(heap[0])
'''
생각해보니 작은 수부터 pop할 수 있는 건 heapq였다. heapq를 구현해서 하는 것까지는
순조로웠는데 초기값을 0으로 한 것때문에 계속 해맸다. 값에는 음수도 포함되어 있기 때문에
초기값이 없어야 이상 없이 수행할 수 있었다.
'''