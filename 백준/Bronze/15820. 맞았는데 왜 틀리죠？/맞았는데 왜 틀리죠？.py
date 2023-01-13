s1, s2 = map(int, input().split())
cnt = 0
for i in range(s1):
    s, a = map(int, input().split(' '))
    if s != a:
        cnt += 1
for i in range(s2):
    s, a = map(int, input().split(' '))
    if s != a:
        cnt += 101

if cnt == 0:
    print('Accepted')
elif cnt < 100 and cnt > 0:
    print('Wrong Answer')
elif cnt > 100:
    print ('Why Wrong!!!')