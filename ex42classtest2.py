'''
2.
객체 생성하고 사용하기
클래스 사용하기

'''

# 1. 클래스 정의
class ClassTest2:

    def method1(self):  # 인스턴스 메소드
        """method1() 정의"""
        self.a = 1  # 인스턴스 변수 (self ?)
        self.b = 2
    
    def printValue(self):
        """인스턴스 변수를 출력하는 메소드"""
        print(self.a, self.b)


# 2. 인스턴스(객체) 생성
# 형식: 변수명 = 클래스명()
ct2 = ClassTest2()  # 호출을 하면 클래스가 그대로 메모리에 복사된다.

# 3. 인스턴스(객체) 사용
# 형식: 인스턴스.변수명
# 형식: 인스턴스.메소드명()
ct2.method1()
ct2.printValue()     # 1 2 
print(ct2.a, ct2.b)  # 1 2

'''
3.
디버깅을 이용한 클래스/인스턴스 주소 확인하기

'''
print("---------------------")
#1.클래스 정의
class Class3 :
    a=1
    b=2

    def func1(self): #호출을 할수있게 self라고 적음!
      '''func1()메서드 정의'''
      print("func1()메서드 실행!")
    def printself(self):
        print("printself() 메서드 실행")
        print(self)
        print(id(self))
        print(hex(id(self)))

# 2.인스턴스(객체) 생성
# 객체가 인스턴스 보다 더 큰 범위.예) 객체: 동물,인스턴스 : 강아지 등
# 형식 : 객체변수명 = 클래스명()

ct3 = Class3() # 메모리 생성(ct3이 인스턴스가 됨)

# 3. 인스턴스(객체) 메소드 사용
# 형식: 인스턴스명(객체).메소드명(), 인스턴스명(객체).변수명
# . 의미: ~ 의라고 읽는다.
# . 의미: ~에 존재하는 이라고 읽는다.

ct3.func1() # 호출
print(ct3.a,ct3.b)
print(id(ct3))
print(hex(id(ct3)))
print("--------------")
ct3.printself() # 호출할때 자동으로 주소값이 넘어감
