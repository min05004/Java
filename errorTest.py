"""
파일명 : errorTest.py
프로그램설명 : print() 함수와에러구분하기
"""

#문자열을 사용할 때는 따옴표(작은,큰)로 묶어서 사용한다.
#형식 : print(변수), print(문자열)
print('오늘은 파이썬을 배웁니다.')
print("오늘은 파이썬을 배웁니다.")

#파이썬에 자주 접하는 에러 확인
#1. 문법이 틀린 경우
#SyntaxError: 에러의 원인이 출력된다.
#print(Hello world!)
print("Hello world!")

#2. 들여쓰기가 잘못된 경우
#IndentationError: 에러의 원인이 출력된다.
# print("Hello world!")

#3. 이름이 잘못된 경우
#NameError: 에러의 원인이 출력된다.
#prin("Hello world!")
