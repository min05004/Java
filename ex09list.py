'''
컬렉션이란 여러 개의 요소를 하나로 묶어서 저장할 수 있는 데이터 타입을 의미한다.

파이썬에서 존재하는 컬렉션 데이터 유형
  . 1. list  : 순서가 있고 값을 변경 가능하고 반복할 수 있고 중복된 데이터를 허용한다.
    - Sequence(Ordered), Mutable, Iterable, duplicate 
 
   . 2. tuple : 순서가 있고 값을 변경할 수 없고 반복할 수 있고 중복된 데이터를 허용한다.
    - Sequence(Ordered), IMMutable, Iterable, duplicate 
  
  . 3. dictionary : 순서가 없고 키의 이름은 변경할 수 없지만 값을 변경할 수 있고 
      반복할 수 있고 
    - 키는 중복될 수 없지만 데이터는 중복을 허용한다.
    - UnOrdered, Key(IMMutable), Value(Mutable), Iterable
    - Key(No duplicate), Value(duplicate)
  
  . 4. set : 순서가 없고 값을 변경할 수 없고 반복할 수 있고 중복된 데이터를 허용하지 않는다.
    - UnOrdered, IMMutable, Iterable, No duplicate '''

# 다양한 형태의 리스트 생성 방법
a = []  # 빈리스트
b = [1,2,3,4,5]  # 정수
c = [1.2, 2.5, 3.15]  # 실수
d = ['홍길동', "고길동", '김길동']  # 문자열
e = [1, 2.5, '홍길동']  # 정수, 실수, 문자열을 섞어서 넣을 수 있다.
f = [1, 2.5, ['홍길동', 2023]]  # 리스트
#  f[0] f[1]  f[2][0]   f[2][1]

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(f[2][0])
print(b[2])  # 3
print(d[0])  # 홍길동
print(f[2][1])  # 2023

print("---------------")

print(b[2])
print(c[2])
print(d[1])
print(f[2][1])

print("------------------")
# 변수 l에 리스트 형식으로 정수 1 ~ 5까지 저장한다.
l = [1, 2, 3, 4, 5]
print(l, type(l))  # [1, 2, 3, 4, 5] <class 'list'>

# 인덱싱
# 인덱스 번호로 항목을 출력하는 방법
# 형식: 변수명[인덱스번호]
# print(l[2], l[-3])  # 3  --> [2]  [-3] <--
# print(l[0], l[-5])  # 1  --> [0]  [-5] <--
# print(l[4], l[-1])  # 5  --> [4]  [-1] <--

# 멤버쉽 연산
# 종류: in, not in
# in : 값이 있으면 True, 없으면 False
# not in : 값이 없으면 True, 있으면 False
# 연산의 결과 : True, False
# 형식1 : 값 in 변수명
# 형식2 : 값 in 값
# 형식3 : 변수명 in 변수명
# 형식4 : 변수명 in 값

# l변수에 2가 존재합니까 ?
# print(2 in l)      # True
# l변수에 7이 존재하지 않습니까 ?
# print(7 not in l)  # True

# 크기 함수
# 크기 함수를 이용해서 자료의 길이(개수)를 확인할 수 있다.
# 리스트에서 크기 함수를 사용하면 항목의 개수를 구한다.
# 형식 : 함수명(인수),  len(변수명)
# 리턴값 : 변수의 개수
# 인수 : 입력값, 리턴값 : 출력값
print(len(l))  # 5

# 슬라이싱
# 슬라이싱 : 범위를 지정해서 데이터를 추출하는 기법이다.
# 형식 : 변수명[시작숫자:끝숫자]
# 여기서 시작숫자와 끝숫자는 index 번호를 의미한다.
# 범위 : 시작숫자 ~ 끝숫자 -1 까지
# 시작숫자 생략 : 처음부터
# 끝숫자 생략 : 시작숫자 ~ 끝까지

print(l[1:3])
print(l[-4:-2])