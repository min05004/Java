"""
파일명: ex02.py
프로그램 설명: 변수를 이용한 문자열 출력하기
"""
# 변수의 저장 형식
# 변수명 = 값
# 변수명 = 변수명
# 변수명 = 수식
# 변수명 = 함수

#==가 같다. 
name = "홍길동" #문자열 값 대입
number = 3  

print(name,number)
print('%s %d' %(name,number))
print('{} {}' .format(name,number)) #format 메서드를 이용한 출력법
print(f'{name} {number}') 

#출력방법 4가지.

print(1,2,3,4,5)
print('%d %d %d %d %d' %(1,2,3,4,5))
print(f'{1} {2} {3} {4} {5}')

# 변수를 활용하여 출력하기
'''변수명을 만드는 규칙
파이썬에서 제공되는 예약어로는 사용이 안됨(if,while ..)
특수문자 안됨,변수명은 _를 사용할 수 있고 _로 시작할 수 있다.
'''

messagw_string = "Hello"

#------------파이썬 내 키워드만 출력 가능-----------
import keyword
print(keyword.kwlist)
#키워드모듈 안 키워드 리스트를 출력.
 
studentName = "홍길동"
student_name = "홍길동"

print('%s %s' %(studentName,student_name))
print('{}''{}' .format(studentName,student_name))
print(f'{student_name}{studentName}')
 


# format() 메서드 이용 (출력방법 4가지)
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

