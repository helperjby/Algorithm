def solution(rsp):
    result = ''
    for i in rsp:
        if int(i) == 2:
            result += str((int(i)-2))
        elif int(i) == 0:
            result += str((int(i)+5))
        elif int(i) == 5:
            result += str((int(i)-3))
    return result
