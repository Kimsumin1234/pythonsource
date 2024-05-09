# print 가 있어서 print.py 는 못만든다 print1.py 로 만들어야함

# 함수 : print(출력할문장) == sout()
# 문자 : '' or "" 가능
print('Hello Python!')
print("Hello Python!")
print(100)
print("100")
print(25.3)
print("25.3")

# type() : 데이터 타입
# 파이썬에서 True , False 는 대문자 시작
print(type("Hello Python!")) # <class 'str'> 문자 형태는 다 str
print(type(100)) # <class 'int'> 숫자 형태는 다 int
print(type(25.3)) # <class 'float'> 소숫점은 다 float
print(type(True)) # <class 'bool'>

print("T","E","S","T") # T E S T  한칸씩 공백을 가지고 출력

# print() 에 사용하는 옵션
# sep : 문자열 출력시 구분을 줄수있다 (기본값은 스페이스바 한번)
print("T","E","S","T", sep="") # TEST
print("2024","05","09", sep="-") # 2024-05-09
# end : print() 후 값을 줄수있다 (기본값은 줄바꿈 \n)
print("Welcome to", end=" ") # Welcome to 안녕하세요
print("안녕하세요")

# 1) 포매팅 - %d, %s, %f, %c (%s 로 다 대체가능)
# 포맷코드 + 숫자 : %5d (전체자리수 5, 기본은 오른쪽정렬)
print("%d" % 100)
print("%5d" % 100)
print("%05d" % 100, end="\n\n") # 전체자릿수에서 빈자리에 0 채우기, end="\n\n" 엔터 두번
print("%s" % "hi")
print("%5s" % "hi", end="\n\n")
print("%-8.2f" % 123.21) # - : 왼쪽정렬 , 8 : 전체자리수(소수점 자리수 포함해서) , .2 : 소수점 자리수
print("%8.2f" % 123.21)
print("%8.2f" % 123.21567) # 반올림을 알아서 해준다

# 파이썬은 변수 선언할때는 타입 없음 (값을 담고 난 다음에 결정)
# 파이썬은 변수 선언할때 정하는 키워드 없음 (let, const X)
number = 4
print("I eat %d apples" % number)

# print("%d : %s" % 1, "홍길동") TypeError: not enough arguments for format string
print("%d : %s" % (1, "홍길동")) # 여러개 대입할때는 () 묶어서 사용

# %s : 어떤 형태의 값이든 문자열로 변환해서 대입
print("I eat %s apples" % number)
print("I eat %s apples" % 3.1415)
print("I eat %s apples" % "three")

# %% : % 기호를 화면에 출력하는 방법
print("Error is %d%%" % 98)

print("===========================")
# 2) format() 함수 : 포맷코드와 유사한 역할
print("I eat {} apples".format(3))
print("{} and {}".format("you","me"))
# format() + 인덱스
# {0} {1} ... : 대입자리를 정할수있다
print("I eat {0} apples".format(3))
print("{0} and {1} and {0}".format("you","me"))
# format() + 인덱스 + 이름
print("{var1} and {var2}".format(var1="You",var2="niceman"))
print("I ate {0} apples, so I was sick for {day} days".format(10,day=3))
# format() + 인덱스 + 정렬
print("{0:<10}".format("hi")) # 총 자릿수는 10 그리고 왼쪽 정렬
print("{0:>10}".format("hi")) # 총 자릿수는 10 그리고 오른쪽 정렬
print("{0:^10}".format("hi")) # 총 자릿수는 10 그리고 가운데 정렬
print("Test1: {0:5d}, Price: {1:4.2f}".format(776,6523.123)) # 5d %를 안주고 자리값만 주려고할떄 이렇게 사용

print("===========================")
# 3) f 문자열 포매팅
name= "홍길동"
age= 30
print(f"나의 이름은 {name} 입니다. 나이는 {age} 입니다.")

print("===========================")
print("\n줄바꿈\n연습")
print("\t탭\t연습")
print("글자가 '강조' 되는 효과")
print('글자가 "강조" 되는 효과')