#함수유형

#1.입력 값 : o , 출력 값 : o
def f1(x):
    y = x+5
    return y
number = f1(3)
print(number)

#2. 입력 값 : x ,출력값 : x

def f2():
    x=3
    y=3
    print(x+y)
f2()

#3.입력값 : o,출력값 :x
def f3 (x):
    y=5
    print(x+y)
f3(3) 

#4.입력값 : x,출력값 : o
def f4() :
    x=3
    y=5
    return x+y

print(f4())