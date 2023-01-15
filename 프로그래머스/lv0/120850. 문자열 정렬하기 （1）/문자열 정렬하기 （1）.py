def solution(my_string):
    answer = list(map(str, my_string))
    num =[]
    for i in answer:
        try:
            num.append(int(i)/1 )
        except:
            pass
    return sorted(num)