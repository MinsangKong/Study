#https://www.acmicpc.net/problem/13164
#백준 13164번 행복 유치원(정렬)
#import sys
#input = sys.stdin.readline

n, k = map(int, input().split())
school = list(map(int, input().split()))
diff = []
for i in range(1,n):
    diff.append(school[i] - school[i-1])
diff.sort()

result = 0
for i in range(n-k):
    result += diff[i]
print(result)
'''
이해를 잘 못 해서 엄청 해메고 계속 틀렸다. 간단하게 옆에 붙어 있는 순자더라도 
차이가 적으면 결국 묶어서 처리하면 되기 때문에 이렇게 풀 수 있었다. 후...
생각을 잘못해서 틀리면 엄청 지친다...
'''