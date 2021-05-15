import sys
input = sys.stdin.readline
sys.setrecursionlimit(3000000)

def check(k, temp):
    for j in range(k+1,n):
        if result[j] < temp:
            check(j,result[j])
            result[j]=temp
            return
n = int(input())
result = [0]*n
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        for k in range(n):
            if data[j] > result[k]: 
                check(k,result[k])
                result[k] = data[j]
                break
print(result[n-1])
'''
두 번째로 생각한 방법은 가장 큰 수 n개를 지정한 뒤 재귀로 정렬하는 방식이었다.
그러나 가장 큰 수 n개를 저장하는 방식으로도 재귀의 문제로 시간 초과가 발생했다. 
후 시간초과를 어떻게 잡아야 할지 고민이 된다.
'''