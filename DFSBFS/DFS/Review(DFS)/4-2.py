#https://www.acmicpc.net/problem/2210
#백준 2210번 숫자판 점프(DFS)
def dfs(i, j, string):
    string += numbers[i][j]
    if len(string) == 6:
        result.add(string)
        return
    if 0 <= i - 1:
        dfs(i - 1, j, string)
    if i + 1 < 5:
        dfs(i + 1, j, string)
    if 0 <= j - 1:
        dfs(i, j - 1, string)
    if j + 1 < 5:
        dfs(i, j + 1, string)


numbers = [input().split() for _ in range(5)]
result = set([])
for i in range(5):
    for j in range(5):
        dfs(i, j, '')
print(len(result))