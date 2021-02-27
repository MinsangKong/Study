n , m = map(int,input().split()) #생각해보니 set으로 만들면 자동으로 중복제거
h_num = set()
s_num = set()

for i in range(n):
    h_num.add(input())
for i in range(m):
    s_num.add(input())

result = sorted(list(h_num & s_num)) # &연산자로 동일한 부분 추출
print(len(result))

for i in result:
    print(i)