#최대값을 구하는 사용자 함수 만들기

# 파일명: myMax.py
# 함수명: myMax
# 인수: 값 2개
# 첫 번째 매개변수명: a
# 두 번째 매개변수명: b
# 리턴값: 두 개의 값을 비교해서 가장 큰 값을 리턴한다.
# 기능: 전달된 인수값을 비교해서 가장 큰 값을 돌려준다.
print("----예제 1----")
def myMax (a,b):
    if a>b:
        return a
    else :
        return b
    
print(myMax(1,2))

print("----예제 2 ----")

def myMax (a,b):
 print(max(a,b))

myMax(1,2)

# 여러 개의 인수를 받을 때는 매개변수를 *args로 받으면 된다.
print("----여러개의 인수를 받을 경우-----")
def function(*args): # *로 받으면 묶어서 받음.
    print(args)  # tuple

function(1,2)
function(1,2,3)    
function(1,2,3,4,5)

print("--------예제 3---------")
def myMax(*args):
    a = args[0]  # 첫 번째 index의 값을 변수a에 저장한다.

    for b in args[1:]:  # 첫번째 값을 0번 방에 넣은 후 나머지 값을 1번방 이후에 넣어 비교.
        if a > b:
            continue
        else:
            a = b
    return a
    
print(myMax(1,2))    # 2
print(myMax(100,2))  # 100
print(myMax(100,2,200))  # 200 여러 개 받을 수 있다.
print(myMax(-1,-2,-3))   # -1