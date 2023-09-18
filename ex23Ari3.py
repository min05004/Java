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

# 논리 부정 테스트
print(not False)  # True
print(not True)   # False