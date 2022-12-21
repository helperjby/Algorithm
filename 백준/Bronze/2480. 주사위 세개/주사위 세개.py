a, b, c = map(int, input().split(' '))

# 3개가 같으면 10000 + (눈 값)*1000
# 2개가 같으면 1000 + (눈 값)*100
# 같은게 없으면 가장 큰 눈 값 * 100

if a == b == c:
    print(10000 + a * 1000)
elif a == b or a == c or b == c:
    if a == b:
        print(1000 + a*100)
    elif b == c:
        print(1000 + b*100)
    elif c == a:
        print(1000 + c*100)
else:
    print(max(a, b, c) * 100)