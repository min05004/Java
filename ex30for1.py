range() 
##https://docs.python.org/ko/3/tutorial/index.html
##https://docs.python.org/ko/3/tutorial/controlflow.html#the-range-function
'''
range() 함수(클래스)를 이용한 숫자 증가하기
형식 : 
range(숫자) : #숫자가 1개가 인수로 올 경우
range(시작숫자,끝숫자) :# 숫자가 2개가 인수로 올 경우
range(시작숫자,끝숫자,증가할개수) :#숫자가 3개가 인수로 올 경우
#range() 함수는 0부터 시작한다. 끝숫자는 포함이 안된다.
'''

'''range(5) : 0,1,2,3,4
range(1,11) : 1,2,3,4,5,6,7,8,9,10
range(5,11) : 5,6,7,8,9,10
range(1,6) : 1,2,3,4,5
range(1,6,1) : 1,2,3,4,5
range(1,11,2) : 1,3,5,7,9
range(5,0,-1) : 5,4,3,2,1
range(10,0,-2) : 10, 8, 6, 4, 2
list(range(1,3001)) : [1, ... 3000]
'''
def myFunction():
    return (1,2,3,4,5)

# for문 옆에 올 수 있는 iterator object 살펴보기
print(iter([1,2,3,4,5]))  # <list_iterator object at 0x0000028E6004B688>
print(iter((1,2,3,4,5)))  # <tuple_iterator object at 0x0000028E6004B688>
print(iter("12345"))      # <str_iterator object at 0x0000028E6004B688>
print(iter(range(1,6)))   # <range_iterator object at 0x0000028E5FB9E770>
print(iter(myFunction())) # <tuple_iterator object at 0x0000028E6004BA88>
print(iter({1,2,3,4,5}))  # <set_iterator object at 0x0000028E60045A98>
print(iter({'a':1, 'b':2, 'c':3, 'd':4, 'e':5})) # <dict_keyiterator object at 0x0000028E60045A98> 

"""
파일명 : exFor3.py
프로그램 설명 : for문
"""

# 반복문을 사용하고 1 ~ 5까지 출력

# 2x1=2  2x2=4  2x3=6  2x4=8  2x5=10  2x6=12  2x7=14  2x8=16  2x9=18

# dan = 2
# i = 1
# 
# while i <= 9:
#     print(f'{dan}x{i}={dan*i}', end='  ')
#     i += 1
# else:
#     print()

dan = 2
for i in range(1,10):
    print(f'{dan}x{i}={dan*i}', end='  ')
else:
    print()

'''
중첩 (이중) for문
for문 안에 for문이 들어간 형태
형식 : 
for i in 이터러블객체 :
    실행문 
       :
    for j in 이터러블객체 :
        실행문
          :
    else:
         실행문
    실행문 
       :
else:
    실행문
'''

# i = 1 ~ 5
for i in range(1,6):
    print(i)

# j = 6 ~ 10
for j in range(6,11):
    print(j)    

# i = 1 ~ 5
for i in range(1,6):

    # j = 6 ~ 10
    for j in range(6,11):
        print(i, j)    
    else:
        print('j for문 종료')
else:
    print('i for문 종료')    
'''-- exForFor.py ---


-- exGugudan3.py --'''
"""
파일명 : exGugudan3.py
프로그램 설명 : 중첩 for문을 이용한 구구단 출력하기
"""

# 2x1=2  3x1=3  4x1=4  5x1=5  6x1=6  7x1=7  8x1=8  9x1=9
# 2x2=4  3x2=6  4x2=8  5x2=10 6x2=12 7x2=14 8x2=16 9x2=18
# 2x3=6  3x3=9  4x3=12 5x3=15 6x3=18 7x3=21 8x3=24 9x3=27
# 2x4=8  3x4=12 4x4=16 5x4=20 6x4=24 7x4=28 8x4=32 9x4=36
# 2x5=10 3x5=15 4x5=20 5x5=25 6x5=30 7x5=35 8x5=40 9x5=45
# 2x6=12 3x6=18 4x6=24 5x6=30 6x6=36 7x6=42 8x6=48 9x6=54
# 2x7=14 3x7=21 4x7=28 5x7=35 6x7=42 7x7=49 8x7=56 9x7=63
# 2x8=16 3x8=24 4x8=32 5x8=40 6x8=48 7x8=56 8x8=64 9x8=72
# 2x9=18 3x9=27 4x9=36 5x9=45 6x9=54 7x9=63 8x9=72 9x9=81

# 2단만 출력
# dan = 2
# for i in range(1,10):
#     print(f'{dan}x{i}={dan*i}', end='  ')
# else:
#     print()

for dan in range(2,10): # 2 ~ 9
    for i in range(1,10):  # 1 ~ 9
        print(f'{dan}x{i}={dan*i:<2d}', end='  ')
    else:
        print()
        