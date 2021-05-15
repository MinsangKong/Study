import heapq
n = int(input())
# 힙(Heap)에 초기 카드 묶음을 모두 삽입
heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)
result = 0

# 힙(Heap)에 원소가 1개 남을 때까지
while len(heap) != 1:
# 가장 작은 2개의 카드 묶음 꺼내기
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    # 카드 묶음을 합쳐서 다시 삽입
    sum_value = one + two
    result += sum_value
    heapq.heappush(heap, sum_value)
print(result)
'''
굳이 값을 비교할 필요 없이 바로 가장 작은 2개의 값을 빼낸 뒤 그 값을 결과값에 더한 뒤
더한 두 값은 다시 push방식으로만 했어도 문제가 없었다. 그냥 0이 될 때까지 pop을 하는 식으로
생각했는데 계속 push만 해줘도 결과적으로는 가장 큰 값만 남기 때문이다. 방식을 떠올린
것까지는 좋았지만 조금 아쉬웠다...
'''