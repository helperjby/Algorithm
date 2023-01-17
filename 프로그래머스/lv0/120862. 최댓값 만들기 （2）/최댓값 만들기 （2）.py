def solution(numbers):
    numbers= sorted(numbers)
    if (numbers[0] * numbers[1]) > (numbers[-1] * numbers[-2]):
        return(numbers[0]*numbers[1])
    else:
        return(numbers[-1]*numbers[-2])



# 리스트를 sorted 제일 큰거 2개 곱하고, 제일 작은거 2개 곱해서
# 두개 중에 큰거 출력
# 