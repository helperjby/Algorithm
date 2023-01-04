N, X = map(int, input().split())
A = list(map(int, input().split()))
answer = []
for i in A:
    if i < X:
        answer.append(i)
print(*answer)