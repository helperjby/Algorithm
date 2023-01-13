# 등차수열 찾기
N = int(input())
cnt = 0
for i in range(1, N+1):
    a=list(map(int, str(i)))
    if i < 100:
        cnt += 1
    elif i > 99 and a[0] - a[1] == a[1] - a[2]:
        cnt += 1
print(cnt)