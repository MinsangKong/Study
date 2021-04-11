#https://www.acmicpc.net/problem/1292
#백준 1292번 쉽게 푸는 문제(구현)
number_list = []
for i in range(1, 46):
    number_list += [i] * i
    
A, B = map(int, input().split())
print(sum(number_list[A-1:B]))
'''
굳이 하나 하나씩 구하지 말고 미리 경우의 수를(1~1000) 정한 다음에 그 값들을 합해주는
방식이 훨씬 빠르다.
'''