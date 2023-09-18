# 크기 함수
# 크기 함수를 이용해서 자료의 길이(개수)를 확인할 수 있다.
# 리스트에서 크기 함수를 사용하면 항목의 개수를 구한다.
# 형식 : 함수명(인수),  len(변수명)
# 리턴값 : 변수의 개수
# 인수 : 입력값, 리턴값 : 출력값

student = {'name':'홍길동', 'phone':'010-1111-2222', 'birth':'12월25일'}
print(len(student))  # 3

# 슬라이싱
# 슬라이싱은 주로 순서가 있는 시퀀스 자료형(예: 리스트, 문자열)에서 사용되고
# 딕셔너리는 순서가 없기 때문에 슬라이싱(slicing) 개념은 사용되지 않는다. 

# 반복성
# 딕셔너리 자료형은 반복성을 가지고 있으므로 for문으로 돌릴 수 있다.
dictData = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}

# 딕셔너리는 for문에서 키를 던진다.
for value in dictData:
    print(value)  # a b c d e  : 키값만 나옴

# key 변수에 저장된 키의 값을 이용해서 값을 출력한다.
for value in dictData:
    print(dictData[value])  # 1 2 3 4 5 

# 딕셔너리에서 메소드(메서드)를 이용해서 key를 추출한다.
for key in dictData.keys():
    print(key)  # a b c d e  / 키값만

# 딕셔너리에서 메소드(메서드)를 이용해서 값을 추출한다.
for value in dictData.values():
    print(value) # 1 2 3 4 5 / 자료의 값만

# 학생의 정보를 저장하는 변수를 사전 자료형으로 생성한다.
# 저장되는 값: 이름(name), 핸드폰(phone), 생일(birth)
student = {'name':'홍길동', 'phone':'010-1111-2222', 'birth':'12월25일'}
#student = ['홍길동', '010-1111-2222', '12월25일']

print(student['name'])   # 홍길동
print(student['phone'])  # 010-1111-2222
print(student['birth'])  # 12월25일
print()  # 엔터

for value in student.values():
    print(value)