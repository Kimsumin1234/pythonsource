# 변수
# 변수 : 타입 없음 (값을 담고 난 다음에 결정) / 키워드 없음(let, const X)

num = 1
num = "10"  # 10 으로 초기화
print(num)

a = b = 3
print(a, b)  # 3 3 으로 출력

a, b = 10, 15
print(a, b)  # 10 15 로 출력

# 두개의 변수에 있는 값 서로 바꿔 넣기 (자바에서는 탬프에 담고 복사한다음에 이차저차 복잡하지만, 파이썬은 간단하다)
a, b = b, a
print("a = %d, b = %d" % (a, b))  # a = 15, b = 10 출력

str1 = "500"
num1 = 500  # TypeError: can only concatenate str (not "int") to str
# print(str1 + num1) # 자바는 연결의 의미로 해서 에러가 안나지만 파이썬은 에러가 난다

print("========================")
# 타입변환 : str(), int(), float(), bool()
# type() : 타입확인
print(type(str1))
print(type(num1))
print(type(10.5))
print(type(False))

print("인트로변환", type(int(str1)))
print(int(str1) + num1)  # 1000

f = 3.5
print(type(f))
print("문자로변환", type(str(f)))

print("========================")
print(int(True))  # 1
print(int(False))  # 0
print(int(3.6))  # 3 , 소수점은 버리고 변환해준다
print(int("3"))  # 3
# 소수점 혹은 지수를 포함하는 문자열은 int로 변경못함
# print(int("3.6")) # ValueError: invalid literal for int() with base 10: '3.6'  문자타입의 3.6 은 변환 안해줌

print("========================")
print(float(True))  # 1.0
print(float(False))  # 0.0
print(float(3.6))  # 3.6
print(float("3"))  # 3.0
print(float("3.6"))  # 3.6
print(float("3.06e4"))  # 30600.0

print("========================")
# 0 이 아닌 데이터는 전부 True
print(bool(1))  # True
print(bool(0))  # False
print(bool(99))  # True
print(bool("99"))  # True
print(bool("구십구"))  # True
