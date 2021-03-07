#https://www.acmicpc.net/problem/2217
#백준 2217번 로프(그리디)
n = int(input())
rope = []
for i in range(n):
    rope.append(int(input()))
rope.sort(reverse=True)
w = 0
for i in range(n):
    if (i+1)*rope[i] >= w:
        w=rope[i]*(i+1)
print(w)

"""
else로 작은 건 break했는데 잘못 생각한거였음.
생각을 잘못해서 시간이 엄청 오래 걸렸다. 
"""