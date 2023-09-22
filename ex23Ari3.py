'''
 4. 논리 연산자 (Logical Operators)
 
 두 개 이상의 관계 연산자를 묶을 때 사용하는 연산자

형식 : 조건1 논리연산자 조건2  --> 결과는 True/False
조건1 : 관계 연산자 (1 == 1 and 2 == 2)  1 == 1
조건2 : 관계 연산자 (1 == 1 and 2 == 2)  2 == 2

*** 참고 ***
논리곱은 조건1의 연산 결과가 거짓이면 조건2를 평가하지 않는다.
논리합은 조건1의 연산 결과가 참이면 조건2를 평가하지 않는다.



논리 연산자 : and, or, not
논리 연산자의 우선 순위
1. not  (참고: C,C++,Java,C# 언어에서는 !를 사용한다.)
2. and  (참고: C,C++,Java,C# 언어에서는 &&를 사용한다.)
3. or   (참고: C,C++,Java,C# 언어에서는 ||를 사용한다.)

연산자   사용 예    의미
and      a and b    a와 b를 and 연산
or       a or  b    a와 b를 or 연산
not      not a      a의 논리 부정 연산

논리곱(and) : 두 조건이 모두 참이면 참
논리합(or)  : 두 조건 중 하나만 참이면 참
논리부정(not) : 피연산자의 값이 참이면 거짓, 거짓이면 참으로 바꾼다.


ex) 사용 예
a, b = 2, 8
a == 2 and b < 8
a == b and b == c  
a == b or b == c  
not a            

'''

# 논리합 테스트
print(False or False)   # False
print(False or True)    # True
print(True or False)    # True
print(True or True)     # True

# 논리곱 테스트
print(False and False)  # False
print(False and True)   # False
print(True and False)   # False
print(True and True)    # True

# 1이 참


# 논리 부정 테스트
print(not False)  # True
print(not True)   # False

# 나이 : age
# 9세 이상 ~ 12세 이하
age = 13  # 8:F , 9 ~ 12:T, 13 ~ : F
print(age >= 9 and age <= 12)

# 8세 미만, 11세 초과
age = 13  # True
age = 11  # False
age = 7   # True
age = 8   # False
print(age < 8  or age > 11)

# 아래처럼 and 로 묶으면 안된다.
# 2개의 나이를 동시에 가지는 사람은 없기 때문이다.
# print(age < 8 and age > 11) X

# 8세, 10세, 12세인 경우
# age = 7   # False
# age = 8   # True
age = 10  # True
# age = 12  # True
# age = 13  # False
print(age == 8 or age == 10 or age == 12)
#print(age in (8, 19, 12)) # 동일, 튜플 형태 파이써딕 코드


# 6세 이상 ~ 8세 이하, 10세 이상 ~ 12세 이하
age = 5   # False
# age = 6   # True
# age = 7   # True
# age = 8   # True
# age = 9   # False
# age = 10  # True
# age = 12  # True
# age = 13  # False
print(age >= 6 and age <= 8 or age >= 10 and age <= 12)

# 아래처럼 and 로 묶으면 안된다.
# print(age >= 6 and age <= 8 and age >= 10 and age <= 12)a = 7, b = 3 일 경우 2진수 표현하면


# a = 00000111
# b = 00000011

# 연산자 사용 예    의미       
# &      a & b      비트 AND 연산. 둘다 참일때만 만족	
# |      a | b      비트 OR 연산. 둘 중 하나만 참이여도 만족
# ^      a ^ b      비트 XOR 연산. 둘 중 하나만 참일 때 만족	
# ~      a ~ b      비트 NOT 연산, 보수 연산.	
# <<     a << b     왼쪽 시프트 연산자. 변수의 값을 왼쪽으로 지정된 비트 수 만큼 이동	
# >>     a >> b     오른쪽 시프트 연산자. 변수의 값을 오른쪽으로 지정된 비트 수 만큼 이동	

# a & b : 3
# a =    00000111
# b =  & 00000011
#      ----------
#        00000011

# a | b : 7
# a =    00000111
# b =  | 00000011
#      ----------
#        00000111

# a ^ b : 4
# a =    00000111
# b =  ^ 00000011
#      ----------
#        00000100

# ~a : -8
# a = 00000111
# ~a :11111000

# 1  : 00000001   
# ~1 : 11111110   10000001(x)

# 1 : 00000001
# 1의 보수 : 11111110
# 2의 보수 : 11111111

# -1 : 11111111
# -2 : 11111110
# -3 : 11111101
# -4 : 11111100

# 1일 경우 왼쪽 쉬프트 연산을 한 경우
# 128 64 32 16 8 4 2 1 
# 1 << 1
# 00000001  << 1  => 00000010
# 00000001  << 2  => 00000100
# 00000001  << 3  => 00001000


# 128 64 32 16 8 4 2 1 
# 64일 경우 오른쪽 쉬프트 연산을 한 경우
# 64 : 01000000 >> 1 => 00100000
# 64 : 01000000 >> 2 => 00010000

# a << 1 : 14
# a = 7
# a =    00000111
# a << 1 00001110

# a << 2 : 28
# a =    00000111
# a << 2 00011100

# a >> 1 : 3
# a =    00000111
# a >> 1 00000011

# a >> 2 : 1
# a =    00000111
# a >> 2 00000001



"""
파일명 : exBitwise1.py 
프로그램 설명 :  비트 연산자 예제 1
"""