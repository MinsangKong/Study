#https://www.acmicpc.net/problem/14247
#백준 14247번 나무 자르기(그리디)
n = int(input())
hi = list(map(int, input().split()))
ai = list(map(int, input().split()))
result=[]
for i in range(n):
    result.append([hi[i],ai[i]])
l = lambda x: x[1]
result = sorted(result, key = l)
cost = 0
for i in range(n):
    cost += result[i][0]+result[i][1]*i
    
print(cost)
'''
남의 코드를 보니까 애초에 result 배열을 만들 필요가 없었다. 
ai를 정렬하고 작은 순서대로 곱해주기만 하면 최종 결과는 똑같기 때문에 
비효율적으로 코드를 작성했다... 반성하자
'''