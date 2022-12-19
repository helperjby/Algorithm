a = input().split(' ')
b = list(map(int, a)) # 리스트를 인트로 변환
c = [1, 1, 2, 2, 2, 8]
d = [x-y for x, y in zip(c,b)]

print(*d)