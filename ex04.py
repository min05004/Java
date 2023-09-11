"""
파일명: ex05.py
프로그램 설명: 변수의 값 출력하기
"""

# 값을 입력하는 부분
# 형식: 변수명 = 값
name = '홍길동'
kor  = 100
eng  = 90
math = 80  # 여기서는 math 모듈을 사용하지 않기 때문에 사용이 가능하다.

# 값을 출력하는 부분
# 변수 출력 용법으로 출력한다.
# 형식 : print(문자열,변수)
print('이름:', name)     # 이름: 홍길동
print('국어점수:', kor)   # 국어점수: 100
print('영어점수:', eng)   # 영어점수: 90
print('수학점수:', math)  # 수학점수: 80
print(name, kor, eng, math) # 홍길동 100 90 80
print() # 엔터

# %용법 으로 출력한다.
# 형식 : print('서식 문자열' %(변수))
# %s: 문자열
# %d: 정수
print('이름: %s' %name)
print('국어점수: %d' %kor)
print('영어점수: %d' %eng)
print('수학점수: %d' %math)
print('%s %d %d %d' %(name, kor, eng, math)) # 홍길동 100 90 80
print()

# format() 메소드(함수) 용법으로 출력한다.
# 형식 : print('{}'.format(변수))
print('이름: {}'.format(name))
print('국어점수: {}'.format(kor))
print('영어점수: {}'.format(eng))
print('수학점수: {}'.format(math))
print('{} {} {} {}'.format(name, kor, eng, math)) # 홍길동 100 90 80
print()

# f-string 용법으로 출력한다.
# 형식 : print(f'{변수명}')
print(f'이름: {name}')
print(f'국어점수: {kor}')
print(f'영어점수: {eng}')
print(f'수학점수: {math}')
print(f'{name} {kor} {eng} {math}') # 홍길동 100 90 80
print()


# print() 함수는 변수나 문자열을 화면에 출력하는 함수이다.
# 형식: print(value, ...)
# 형식: print(value, sep=' ') 
# 형식: print(value, end='\n')
# print() 함수의 기본값 
# sep 변수 : ' '  <-- 공백
# end 변수 : '\n' <-- 엔터 / 아스키코드표
i1 = 1
i2 = 2
i3 = 3

print(i1, i2, i3)  # 1 2 3
print(i1, i2, i3, sep='--',end='<-->')  # 1--2--3<-->1 2 3 
print(i1, i2, i3) 


