m, n = map(int, input().split())
array = [True for i in range(n+1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)

# 에라토스테네스의 체
for i in range(2, int(n**(1/2)) + 1): #2부터 n의 제곱근까지의 모든 수를 확인하며
    if array[i] == True: # i가 소수인 경우(남은 수인 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1
answer = [i for i in range(m, n+1) if array[i] ]
if 1 in answer:
    answer.remove(1)
for i in answer:
    print(i)