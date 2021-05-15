import sys
n = int(sys.stdin.readline().rstrip())
student=[]
for _ in range(n):
    g = list(sys.stdin.readline().rstrip().split())
    student.append((100-int(g[1]),int(g[2]),100-int(g[3]),g[0]))

    
student.sort()
for st in student: print(st[3])
'''
더 빠르게 풀기 위해선 lambda를 쓰지 않고 값에 맞게 수를 조절한 다음에 sort함수를
한 번만 쓰는 것이 가장 효율적이다.
'''