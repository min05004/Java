dictData = {'a':1, 'a':2, 'b':3, 'b':4, 'e':5}
print(dictData)  # {'a': 2, 'b': 4, 'e': 5}

for key in dictData :
    print(key)

for value in dictData.values():
    print(value)

# kor: 국어점수, eng: 영어점수, math: 수학점수
dictData = { 'kor':100, 'eng':100, 'math':100 }

for value in dictData.values():
    print(value)  # 100 100 100

# 딕셔너리에 키와 값을 추가하는 형식: 존재하지 않는 키의 값이 아닌 중복된 키의 값일경우는 삽입이 아닌 변경으로 됨.
# 변수명['키'] = 값 
# 변수명[키변수명] = 값
dictData = {}  # 빈 딕셔너리
dictData['kor'] = 1
dictData['eng'] = 2
dictData['math'] = 3

print(dictData)
print("---삭제하기---")
dictData.pop('kor') # pop() 안에 키값을 넣어야 삭제가 됨.

print(dictData)

# 딕셔너리에서 제공되는 메소드(함수)
# 함수는 하나의 명령어다. ex) print(), type(), len()
# 메소드는 클래스 안에서 정의된 함수를 말한다.
# 딕셔너리변수명.keys()   : 변수의 모든 키를 출력한다. (출력형식 : list형태)
# 딕셔너리변수명.values() : 변수에 값을 출력한다.      (출력형식 : list형태)
# 딕셔너리변수명.items()  : 변수에 키 + 값 출력한다.   (출력형식 : list형태)

# 딕셔너리에서 key만 추출한다.


student =  { 
             'name'  : '홍길동', 
             'phone' : '010-1111-2222', 
             'birth' : '12월25일'
           }
print(student.items())  
# name 홍길동
# phone 010-1111-2222
# birth 12월25일
# for문에서 딕셔너리를 반복하면 key가 추출된다.
for key in student:
    # 값에 접근하기 위해서는 변수명.[key]로 접근해야 한다.
    print(key, student[key])

tupleData = (1,2,3,4)
a = tupleData
a,b,c,d = tupleData
print()

#a,*b : *이 붙은 값에 나머지 값들이 다 들어감.
'''[2, 3, 4, 5]
>>> *a,b = tupleData
>>> a
[1, 2, 3, 4]
>>> b
5
'''
# 'key' in 딕셔너리변수 : 변수 내에 해당 키 값의 존재유무(True, False)
dictData = { 'a':1, 'b':2, 'c': 3, 'd':4, 'e':5}

# print('a' in dictData)      # True
# print('b' in dictData)      # True
# print('x' in dictData)      # False
# print('x' not in dictData)  # True
# print('a' not in dictData)  # False
key = 'a'
print(key in dictData)        # True


# 딕셔너리변수['key']    : 해당 key에 해당하는 value값을 조회한다. (에러 O)
# 딕셔너리변수.get(key)  : 해당 key에 해당하는 value값을 조회한다. (에러 x)
# print(dictData['x'])  # KeyError: 'x'
# print(dictData.get('x'))  # None  해당 key가 없으면 None(문자열이 아니다.)을 리턴한다.
# print(dictData.get('a'))  # 1 해당 key가 있으면 1을 리턴한다.

# 딕셔너리변수['key'] = value값  : 변수 내에 key+value값 를 추가한다.
print(dictData)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# 키가 없으므로 키가 추가된다.
dictData['f'] =  6
print(dictData)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

# 키가 이미 존재하므로 값이 변경된다.
dictData['f'] =  60
print(dictData)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 60}

# del 딕셔너리변수['key]  : 변수 내에 해당 key + value값 삭제한다.
del dictData['a']  # dictData['a'] 삭제
del dictData['f']  # dictData['f'] 삭제
print(dictData)  # {'b': 2, 'c': 3, 'd': 4, 'e': 5}

# 딕셔너리변수.pop('key')  : 변수 내에 해당 key + value값 삭제한다.
dictData.pop('b')  # dictData['b'] 삭제
print(dictData)    # {'c': 3, 'd': 4, 'e': 5}
dictData.pop('c')  # dictData['c'] 삭제
print(dictData)    # {'d': 4, 'e': 5}
# dictData.pop()   # 반드시 인수가 와야 한다. 에러