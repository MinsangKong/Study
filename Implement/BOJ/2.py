#https://www.acmicpc.net/problem/1316
#백준 1316번 그룹 단어 체커(구현)
N = int(input())
array = []
count = 0

for i in range(N):
    word = input()
    array.append(word)

for i in array:
    arr_num = []
    for j in range(len(i)):
        if i[j] in arr_num:
            if i[j-1] == i[j]:
                arr_num.append(i[j])
            else:
                break
        else:
            arr_num.append(i[j])
    if len(arr_num) == len(i):
        count+=1

print(count)