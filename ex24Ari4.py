# 128 64 32 16 8 4 2 1 
# a = 00000111    
# b = 00000011

a = 7
b = 3
print(bin(a))  # 0b111
print(bin(b))  # 0b11

# 8bit로 표현
# 00000111
# 00000011
print("{0:b}".format(a).zfill(8))  # 00000111
print("{0:b}".format(b).zfill(8))  # 00000011

# 32bit로 표현
# 00000000000000000000000000000111
# 00000000000000000000000000000011
print("{0:b}".format(a).zfill(32))  # 00000111
print("{0:b}".format(b).zfill(32))  # 00000011

# 64bit로 표현
# 0000000000000000000000000000000000000000000000000000000000000111
# 0000000000000000000000000000000000000000000000000000000000000011
print("{0:b}".format(a).zfill(64))  # 00000111
print("{0:b}".format(b).zfill(64))  # 00000011
lo
"""
## 6. 멤버쉽 연산자 (Membership Operators)


구성원의 존재 유무를 확인하는 연산자  
값이 있는지 없는지 판단할 때 사용한다.

연산의 결과 : True, False

종류 : in, not in
in     : 값이 존재하면 True, 존재하지 않으면 False
not in : 값이 존재하지 않으면 True , 존재하면 False
형식 : 
a in b  <-- 반드시 b는 반복할 수 있는 iterable 이 와야 한다. (문자열,리스트,튜플,딕셔너리,셋,함수)
a not in b

-- exMembership1.py --
"""

# number에 1 ~ 10까지 저장한다.
number = [1,2,3,4,5,6,7,8,9,10]

# 반복 가능한지 확인한다.
# print(iter(3))  #  TypeError: 'int' object is not iterable
print(iter([]), iter(()), iter({}), iter(set()))

# number 변수에 5가 존재합니까 ?
print(5 in number)  # True
    
# number 변수에 13이 존재합니까 ?
print(13 in number)  # False

# number 변수에 20이 존재하지 않습니까 ?
print(20 not in number)  # True

# number 변수에 7이 존재하지 않습니까 ?
print(7 not in number)  # False

# number 변수에 13이 존재하지 않습니까 ?
print(13 not in number)  # True

# 실제 코드는 아래처럼 if문을 이용해서 멤버쉽 연산자를 사용한다.
if 5 in number:
    print('number 변수에 5가 존재합니다.')
else:    
    print('number 변수에 5가 존재하지 않습니다.')

a = input('입력 : ')
a = int(a)
a == 1 or a == 2 or a == 3
a in (1,2,3)  # 파이써닉한 코드 (좀 더 파이썬 다운 코드다.)

''' 7. 식별 연산자 (Identity Operators)


두 변수가 동일한 객체인지 확인하는 연산자

연산 결과 -> True, False

파이썬에만 존재하는 특별한 연산자다.
종류 : is, not is
is : 두 객체가 같으면 True, 다르면 False  
is not : 두 객체가 같지 않으면 True, 같으면 False

형식 : 
a is b
a is not b
'''



# 파이썬에서는 모든 변수는 객체로 만든다.
# id() 함수 : 변수의 메모리를 확인할 때 사용한다.
a1 = 7
a2 = 7
a3 = 8

print(a1, a2, a3) # 7 7 8
print("a1 :", id(a1))  # 2693008157168
print("a2 :", id(a2))  # 2693008157168
print("a3 :", id(a3))  # 2226968750608
print(a1 is a2)  # True  동일한 객체이므로 
print(a1 is a3)  # False 동일한 객체가 아니므로 

b1 = 7
b2 = 20
b3 = 20
print("b1 :", id(b1))  # 2693008157168
print("b2 :", id(b2))  # 2210206804880
print("b3 :", id(b3))  # 2210206804880
print(a1 is b1)  # True  동일한 객체이므로
print(b1 is b2)  # False 동일한 객체가 아니므로
print(b2 is b3)  # True  동일한 객체이므로

# is not
print(a1 is not b3)  # True  동일한 객체가 아니므로
print(b2 is not b3)  # False 동일한 객체 이므로