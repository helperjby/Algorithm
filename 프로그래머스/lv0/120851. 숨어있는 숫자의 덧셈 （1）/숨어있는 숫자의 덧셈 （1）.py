def solution(my_string):
    a = list(map(str, my_string))
    b = 0
    for i in a:
        try:
            b += int(i)
        except:
            pass
    return b