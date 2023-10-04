'''
전역 변수 & 지역 변수
전역 변수: 모든 함수에서 사용할 수 있는 변수
지역 변수: 함수 내에서만 사용하는 변수

               전역 변수   지역 변수
함수 안에서 읽기    O          O   
함수 안에서 쓰기    X (global 키워드를 이용하면 O) O  
함수 밖에서 읽기    O          X
함수 밖에서 쓰기    O          X


'''

value = 1


def printValue():
  print(value, type(value))

printValue()    
# 함수 내부에서 전역변수 읽기 
# 함수 내부에서 전역변수 value에 접근할 수 있다.
# r(읽기) 가능하다.

print("----------------------------")
def changeValue():
 value = 10
 value += 10
 print(value, type(value))

changeValue()
print(value)    
# 함수 내부에서 전역변수 쓰기 
# 함수 내부에서 전역변수 value에 접근해서 저장한다.
# w(쓰기) 불가능하다.

