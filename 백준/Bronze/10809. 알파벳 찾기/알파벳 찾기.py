s = str(input())
alpa = list('abcdefghijklmnopqrstuvwxyz')
answer = []
for i in alpa:
    if i in s:
        answer.append(s.index(i))
    elif i not in s:
        answer.append(-1)

print(*answer)