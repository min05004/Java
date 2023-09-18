'''
변수에 값을 저장(대입)하기 위해서 사용하는 연산자

결과는 변수에 값을 저장한다.

형식 : 
a는 변수가 오고 b는 값, 변수, 수식, 함수를 사용한다.
a 대입연산자 b       --> a = 1 (값 1을 변수 a에 저장)

대입 연산자의 종류
= : 순수한 대입 연산자
+=, -=, *=, /=, %=, **= , //= : 복합 대입 연산자(대입 연산자 + 산술 연산자)


a, b = 2, 8

연산자  사용 예     의미
=       a = b       우변의 값을 좌변에 대입
+=      a += b      좌변에 우변 값을 더한 결과를 대입 (a = a + b 동일)
-=      a -= b      좌변에 우변 값을 뺀 결과를 대입 (a = a - b 동일)
*=      a *= b      좌변에 우변 값을 곱한 결과를 대입 (a = a * b 동일)
/=      a /= b      좌변에 우변 값을 나눈 결과를 대입 (a = a / b 동일)
%=      a %= b      좌변에 우변 값을 나눈 나머지를 대입 (a = a % b 동일)
**=     a **= b     좌변에 우변 값만큼 제곱하고 결과를 대입 (a = a ** b 동일)
//=     a //= b     좌변에 우변 값을 나눈 결과를 대입 (a = a // b 동일)

'''


a = 2
b = 8

# 변수 a에 저장된 값을 1증가
# 형식 : 변수명 += 1
print(a)  # 2
a += 1    # a = a + 1 / 증가연산자 없음.
print(a)  # 3

# 변수 b에 저장된 값을 1감소
# 형식 : 변수명 -= 1
print(b)  # 8
b -= 1    # b = b - 1
print(b)  # 7

a **= b      # a = a ** b
print(a, b)  # 2187 7


'''
3. 관계 연산자 (비교 연산자) (Relational Operators) 
좌변과 우변의 값을 비교해서 크기 관게를 평가하며,
그 결과를 참,거짓으로 나타낸다.

형식 : 
a는 변수, 값, 함수가 오고 b는 변수, 값, 함수를 사용한다.
 a 관계연산자 b  --> 결과는 True/False

 a,b = 2,8 이라고 할 때 

연산자    사용 예   의미 설명
==        a == b    같다 (동등) (Equal)
!=        a != b    같지 않다   (Not equal)
>         a > b     크다 (초과) (Greater than)
<         a < b     작다 (미만) (Less than)
>=        a >= b    크거나 같다 (이상) (Greater than or equal to)
<=        a <= b    작거나 같다 (이하) (Less than or equal to


'''

a , b = 2, 8
print(a, b)  # 2 8

print(a == b)  # False
print(a != b)  # True
print(a > b)   # False
print(a < b)   # True
print(a >= b)  # False
print(a <= b)  # True

#주로 제어문에서 사용 , 출력해서 보여질 일은 없음.

count = 1
while count <= 5:
    print(count)
    count += 1

print()