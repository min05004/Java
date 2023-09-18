'''
학습 목표 : 
파이썬에서 제공하는 연산자의 종류를 파악할 수 있다.
  
연산자의 종류
1. 산술 연산자 (Arithmetic operators)
2. 대입 연산자 (Assignment operators)
3. 관계 연산자 (Relational operators)
4. 논리 연산자 (Logical operators)
5. 비트 연산자 (Bitwise operators)
6. 구성원 연산자 (Membership Operators)
7. 식별 연산자 (Identity Operators)

파이썬에서 수식(식)은 연산자와 피연산자로 이루어져 있다.  
2 + 3 이라는 수식에서 2와 3은 피연산자(연산의 대상)에 해당되며, 
+ 는 연산자(무엇을 연산할 것이지 나타내는 부분)에 해당한다.

연산자(operator) : 프로그램을 짤 때 변수나 값의 연산을 위해 사용되는 부호를 말한다.
피연산자(operand) : 피연산(operation)의 대상이 되는 데이터를 말한다.
a + b라는 연산에서 +는 연산자에 해당되고 a와 b는 피연산자에 해당된다.


%         a % b      나머지 (Modulus) 
//        a // b     나누기 (몫, 소수점 제거)  (Floor division)
**        a ** b     거듭 제곱 (Exponentiation)

산술 연산자 우선 순위
1. **
2. *, /, //, %
3. +, -
우선 순위를 변경하기 위해서는 ( ) 괄호를 넣어준다. 

(20 + 3) + 12 + 2 ** 3 / 4 * 3 

'''

# a = 2, b = 8 이라고 할 때
a, b = 2, 8

# 연산의 결과를 일시적으로 사용하는 방법
# 연산 결과를 바로 적용한다.
print(a, b)  
print(a - b)  # -6
print(a * b)  # 16
print(b / a)  # 4.0 몫
print(b % a)  # 0  나머지
print(b // a)  # 4 몫(소수점 제거) 
print(a ** 3)  # 거듭 제곱

# 연산의 결과를 영구적으로 저장하는 방법
# 연산 결과를 변수에 저장한다.
# 산술 연산자(+)가 대입 연산자(=)보다 우선 순위가 높다.
hap = 2 + 20
print(max(hap, 10, 3*2))  
# max() 값들 중 가장 큰 값을 리턴해줌.
