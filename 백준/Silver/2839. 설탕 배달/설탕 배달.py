n = int(input())

# N >= 8 부터 적용, % 5 값이 6, 12, 3, 9 형태로 패턴 반복
if n == 4 or n == 7:
    a = -1
elif n % 5 == 0:
    a = n//5
elif n % 10 == 1 or n % 10 == 6: # 1 & 6 case
    a = (n-5)//5 + (n-((n-5)//5*5))//3
elif n % 10 == 2 or n % 10 == 7: # 2 & 7 case
    a = (n-10)//5 + (n-((n-10)//5*5))//3
elif n % 10 == 3 or n % 10 == 8: # 3 & 8 case
    a = n//5 + n % 5//3
elif n % 10 == 4 or n % 10 == 9: # 4 & 9 case
    a = (n-5)//5 + (n-((n-5)//5*5))//3
elif n % 3 == 0:
    a = n//3
else:
    a = -1
    
print(a)