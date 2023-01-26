def solution(my_string, num1, num2):
    answer = ''
    split = []
    for i in my_string:
        split += i
    for i in range(len(split)):
        if i == num1:
            i = num2
        elif i == num2:
            i = num1
        answer += my_string[i]      
    return answer


# 0 1 2 3 4 5
# i 가 num1이면 num2로 바꿔라
# i 가 num2면 num1로 바꿔라
# for문으로 append