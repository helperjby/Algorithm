def solution(num, k):
    str_num = str(num)
    for i in str_num:
        if int(i) == k:
            return int(str_num.index(i))+1
        elif str(k) not in str_num:
            return -1