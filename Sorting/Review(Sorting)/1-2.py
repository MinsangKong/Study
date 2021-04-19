import sys
input = sys.stdin.readline
n = int(input())
array = [0]*n
for i in range(n):
    a,b = input().split()
    array[i] = (int(a),b)
array.sort(key = lambda x:x[0])
for i in range(n):
    array[i] = (str(array[i][0]),array[i][1])
    array[i] = " ".join(array[i])
print("\n".join(array))
'''
굳이 입력할 때 i를 넣지 않아도 lambda를 사용 할 때 숫자를 기준으로 정렬하면
같은 숫자일 경우 순위는 동일하다
'''