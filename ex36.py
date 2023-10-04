'''
매개변수에 *를 사용하면 나머지를 모두 묶는다.

'''

def function():
    print("function() 함수 실행")
    return 1,2,3,4,5

a=function() # (1,2,3,4,5)
print(a)

# 함수에 값을 대입
a,b,c,d,e = function() #(1,2,3,4,5)
print(a,b,c,d,e)
#1,2,3,4,5 각 값이 대입됨.

#예외 발생 경우 - a,b = function()

# *을 이용하여 나머지를 묶어서 출력하는 경우
a,*b,c = function()
print(a,b,c) # 1,[2,3,4],5

a,b,*c = function()
print(a,b,c) #1,2,[3,4,5]