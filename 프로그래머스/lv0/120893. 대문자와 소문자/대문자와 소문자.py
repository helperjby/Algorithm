def solution(my_string):
    answer = ''
    small = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    big = []
    for i in small:
        big.append(i.upper())
    for i in (my_string):
        if i in small:
            answer += i.upper()
        elif i in big:
            answer += i.lower()
    return answer