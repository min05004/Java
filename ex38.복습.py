''' 
keyword arguments : 

함수를 호출할 때 인수값을 순서대로 저장하는 방식이 아니라 
변수의 이름으로 값을 전달하는 방식

# 매개변수의 위치는 중요하지 않고 호출할 때 변수명만 맞추어주면 된다.
# 조건은 변수명이 동일해야 한다.

# 형식: 함수명(변수명=값)

keyword arguments 가 먼저 오면 에러가 발생
'''

# 순서에 상관이 없다.
# f(a=1,b=2,c=3)  # 1 2 3
# f(c=3,a=1,b=2)  # 1 2 3
# f(b=2,c=3,a=1)  # 1 2 3


# positional 과 keyword arguments를 섞어서 사용하는 경우의 
# 대표적인 함수는 print() 함수이다.
# 주의할 점은 keyword arguments가 먼저오면 에러가 발생한다.
# https://docs.python.org/3/library/functions.html#print

# end 매개변수는 default 값이 "\n"가 저장되어 있다.
#  print(end='---', 1)  # 에러
print(1, end='---')  # 1--->>>

def f(*args, a=1,b=2,c=3):   # o 
    print(args, a, b, c)   

f(10,20,30)  # (10, 20, 30) 1 2 3
f(10,20,30, a=100, b=200, c=300)  # (10, 20, 30) 100 200 300

def f(**kwargs):   
    print(kwargs, type(kwargs) )  

f(a=1,b=2,c=3)  # {'a': 1, 'b': 2, 'c': 3} <class 'dict'>

dictData = {'a':100,'b':200,'c':300}
# f(dictData)  # 에러
# f(*dictData) # 에러
f(**dictData)  # 호출 시 풀어서 넘긴다. {'a': 100, 'b': 200, 'c': 300} <class 'dict'>