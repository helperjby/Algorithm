n = int(input())

for i in range(n):
    score = 0
    mark = input().split('X')
    for j in mark:
        score += ((len(j)+1) * len(j) / 2)
    print(int(score))