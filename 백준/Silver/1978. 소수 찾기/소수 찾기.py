t = int(input())
n = input().split()

sqrt = [2,3,5,7,11,13,17,19,23,29,31] # 1000 이하 제곱근 내 소수


nlist = list(range(2,1001)) # 2부터 1000까지
nprime = [] # 1000 이하의 합성수 리스트
prime = [] # 1000 이하의 소수 리스트
answer = 0

# nprime 구하기
for i in sqrt:
    for j in range(2, (1000//i)+1):
        nprime.append(j*i)
nrpime = list(set(nprime))

# prime 구하기
for i in nlist:
    if i not in nprime:
        prime.append(i)
# answer 구하기
for i in n:
    if int(i) in prime:
        answer += 1
print (answer)