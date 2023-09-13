'''
딕셔너리는    가지고 자료를 하나로 모아서 묶어 놓은 자료형이다.
딕셔너리의 키는 문자열과 숫자로 구성할 수 있지만 주로 문자열로 key를 만든다.

딕셔너리의 특징
. 키는 중복될 수 없지만 데이터는 중복을 허용한다.
. 순서가 없고 반복할 수 있고 키의 이름은 변경할 수 없지만 값은 변경할 수 있다.

형식 : 
변수명 = {'키':값, '키':값 ...}
변수명 = dict(키 = 값, 키 = 값 ...)
'''

# d 변수에 1 ~ 5까지 저장한다.
d = {'a':1, 'b':2, 'c':3, 'z':4, 'y':5 }
print(d, type(d)) # {'a': 1, 'b': 2, 'c': 3, 'z': 4, 'y': 5} <class 'dict'>

# 딕셔너리는 Sequence 타입의 객체가 아니므로 순서를 가지고 있지 않다.
# 그러므로 리스트나, 튜플처럼 index인 변수명[0] 처럼 값에 접근할 수 없다.
# 편법을 쓰면 가능하다. 키를 숫자로 지정하면 된다.
# print(d[0])  # KeyError: 0


# 편법으로 번호로 지정한 경우(index 번호의 효과)
dictData2 = {0:1, 1:2, 2:3, 3:4, 4:5}
print(dictData2, type(dictData2))  # {0: 1, 1: 2, 2: 3, 3: 4, 4: 5} <class 'dict'>
print(dictData2[0])  # key를 index 처럼 사용할 수 있다. (잘 사용되지는 않는다.)

# 딕셔너리에 저장된 데이터에 접근하기 위해서는 키로 접근해야 한다.
# 형식 : 변수명['키'], 변수명[변수]
# 변수에 방을 번호(리스트, 튜플)로 표현하는 것이 아니라 이름(딕셔너리)으로 표현한다.

print(d['a'])  # 변수명['키'] 1 반드시 '' 를 붙여야함.
a = 'z'
print(d[a])  # 4

print("-----------------------")
a = 'a'
b = 'b'
c = 'c'
d = 'd'
e = 'e'
dictData = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
print(dictData[a])  # 1 변수 a에 저장된 값이 키가 된다.
print(dictData[b])  # 2 변수 b에 저장된 값이 키가 된다.
print(dictData[c])  # 3 변수 c에 저장된 값이 키가 된다.
print(dictData[d])  # 4 변수 d에 저장된 값이 키가 된다.
print(dictData[e])  # 5 변수 e에 저장된 값이 키가 된다.


# 변수를 이용하는 방법
dictData = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}

# 변수를 이용하는 방법
key = ['a', 'b', 'c', 'd', 'e']
print(dictData[key[0]])  # 1 변수 key[0]에 저장된 값이 키가 된다.
print(dictData[key[1]])  # 2 변수 key[1]에 저장된 값이 키가 된다.
print(dictData[key[2]])  # 3 변수 key[2]에 저장된 값이 키가 된다.
print(dictData[key[3]])  # 4 변수 key[3]에 저장된 값이 키가 된다.
print(dictData[key[4]])  # 5 변수 key[4]에 저장된 값이 키가 된다.

# 인덱싱
# 순서가 없기 때문에 리스트처럼 인덱스 번호로 접근할 수 없고
# 키(key)를 사용하여 해당 키에 대응하는 항목의 값을 출력하는 방법
# 형식: 변수명[key]
student = {'name':'홍길동', 'phone':'010-1111-2222', 'birth':'12월25일'}
print(student['name'])   # 홍길동
print()  # 엔터

print("----------------")
# 멤버쉽 연산
# 종류: in, not in
# in : 값이 있으면 True, 없으면 False
# not in : 값이 없으면 True, 있으면 False
# key in dictionary      # key가 딕셔너리에 있는지 확인
# key not in dictionary  # key가 딕셔너리에 없는지 확인
# 연산의 결과 : True, False
# 형식1 : 키 in 변수명
# 형식1 : 키 not in 변수명

# student 변수에 'abc' 키가 존재합니까 ?
print('abc' in student)   # False

# student 변수에 'name' 키가 존재합니까 ?
print('name' in student)  # True