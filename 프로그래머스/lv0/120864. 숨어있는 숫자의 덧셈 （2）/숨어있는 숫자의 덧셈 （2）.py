def solution(my_string):
    # 매개변수를 소문자로 바꾸고 a-z까지 전부 공백으로 변환
    # 문자열을 숫자형으로 변환하고 공백을 구분하여 리스트에 담음
    # 리스트 요소를 다 더함
    my_string = my_string.lower()
    atoz = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in my_string:
        if i in atoz:
            my_string = my_string.replace(i, ' ')
      
    answer = list(map(int, my_string.split()))
    return sum(answer)

