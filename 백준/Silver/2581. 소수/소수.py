m = int(input())
n = int(input())

# 10000의 제곱근 이하의 소수목록
sqrt = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
p = [] # m ~ n 중 일의 자리가 1,3,7,9인 리스트
composite=[] # n 이하의 합성수 리스트
prime=[] # n 이하의 소수 리스트

# p 세팅
for i in range(m, n+1):
    if i%10 == 1 or i%10 == 3 or i%10 == 7 or i%10 == 9:
        p.append(i)
  
if m <= 2 and n >= 2:
    p.append(2)
if m <= 4 and n >= 5:
    p.extend([2,5])
if m > 2 and m < 6:
    p.append(5)

# composite 구하기
for i in sqrt:
    for j in range(2, (10000//i)+1):
            composite.append(j*i)
composite = list(set(composite))

# prime 구하기
for i in p:
    if i not in composite:
        prime.append(i)
prime = list(set(prime))

# 출력 구하기
if 1 in prime:
    prime.remove(1)
if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))