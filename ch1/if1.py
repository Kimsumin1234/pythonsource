# %%
# 파이썬에서 if 구문은 {} 안쓰기 때문에 자동으로 주는 들여쓰기로 구분해서 중요함
if True:
    print("True")

# %%
a = 200
# a 가 100 보다 크고 200 보다 작거나 같은지 확인
if a > 100 and a <= 200:
    print("a는 100 보다 크고 200 보다 작거나 같다")

# %%
# 파이썬은 수학연산 처럼 사용해도 가능하다
if 100 < a <= 200:
    print("a는 100 보다 크고 200 보다 작거나 같다")

# %%
# 세 개의 숫자 중 가장 큰 수 출력
a, b, c = 12, 6, 18
max = a
if max < b:
    max = b
if max < c:
    max = c
print("a,b,c 중 가장 큰 수는 {}".format(max))

# %%
if True:
    print("True")
else:
    print("False")

# %%
score, grade = 90, "A"
# score 가 90이상이고 grade가 A 이면 합격, 아니면 불합격
if score >= 90 and grade == "A":
    print("합격")
else:
    print("불합격")

# %%
# 숫자를 입력 받은 후 짝/홀 출력
num1 = int(input("숫자를 입력해주세요"))
if num1 % 2 == 0:
    print("짝수")
else:
    print("홀수")

# %%
# 중첩 if 문
a = 75
if a > 50:
    if a < 100:
        print("50보다 크고 100보다 작다")
    else:
        print("100보다 크다")
else:
    print("50 보다 작다")

# %%
# 다중 if (파이썬은 switch 구문 없음)
# 자바: else if  ,  파이썬: elif
num = 90
if num >= 90:
    print("A")
elif num >= 80:
    print("B")
elif num >= 70:
    print("C")
elif num >= 60:
    print("D")
else:
    print("D")

# %%
# age, height 입력받은 후
# age 가 20 이상이고 height 가 170 이상 : A 지망 지원가능 출력
# age 가 20 이상이고 height 가 160 이상 : B 지망 지원가능 출력
# age 가 20 이상이고 height 가 160 미만 : 지원불가 출력
# age 가 20 미만 : 20세 이상만 지원가능 출력
age = int(input("나이를 입력해 주세요"))
height = int(input("키를 입력해 주세요"))
# if age >= 20 and height >= 170:
#     print("A 지망 지원가능")
# elif age >= 20 and height >= 160:
#     print("B 지망 지원가능")
# elif age >= 20 and height < 160:
#     print("지원불가")
# elif age < 20:
#     print("20세 이상만 지원가능")
if age >= 20:
    if height >= 170:
        print("A 지망 지원 가능")
    elif height >= 160:
        print("B 지망 지원가능")
    else:
        print("지원 불가")
else:
    print("20세 이상만 지원가능")

# %%
# 점수 입력 받은 후
# 81 ~ 100 : A 학점
# 61 ~ 80 : B 학점
# 41 ~ 60 : C 학점
# 21 ~ 40 : D 학점
# 0 ~ 20 : E 학점
num = int(input("점수를 입력해 주세요"))
if 81 <= num <= 100:
    print("A 학점")
elif 61 <= num <= 80:
    print("B 학점")
elif 41 <= num <= 60:
    print("C 학점")
elif 21 <= num <= 40:
    print("D 학점")
elif 0 <= num <= 20:
    print("E 학점")
else:
    print("점수를 다시 입력해 주세요")

# %%
# 두 개의 숫자 입력 받기, 연산자(+, -, *, /, //, **, %) 입력받기
# 연산 후 결과 출력 (출력예시 5 + 3 = 8)
num1 = int(input("숫자1을 입력해 주세요"))
oper = input("연산자(+, -, *, /, //, **, %)를 입력해주세요")
num2 = int(input("숫자2를 입력해 주세요"))
result = 0
if oper == "+":
    result = num1 + num2
elif oper == "-":
    result = num1 - num2
elif oper == "*":
    result = num1 * num2
elif oper == "/":
    result = num1 / num2
elif oper == "//":
    result = num1 // num2
elif oper == "**":
    result = num1**num2
elif oper == "%":
    result = num1 % num2
else:
    print("연산을 다시 입력해주세요")
print(f"{num1} {oper} {num2} = {result}")

# %%
# 2024-05-14
# 리스트 컴프리헨션(comprehension)

numbers = []

# 요소추가
numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
numbers.append(5)
numbers.append(6)
numbers.append(7)

numbers

# %%
numbers = []

for i in range(1, 101):
    numbers.append(i)

numbers

# %%
numbers = list(range(1, 101))
print(numbers)

# %%
# 리스트 컴프리헨션
# for 구문을 간략화 시킨것
numbers = [x for x in range(1, 101)]
numbers

# %%
a = [1, 2, 3, 4]
# a 라는 리스트 요소에 *3을 한 후 결과를 새로운 리스트로 돌려받기
result = []
for num in a:
    result.append(num * 3)
result

# %%
# 리스트 컴프리헨션
result2 = [num * 3 for num in a]
result2

# %%
b = ["갑", "을", "병", "정"]
# b 라는 리스트에서 정 요소를 제외하고 새로운 리스트로 돌려받기
a = []
for i in b:
    if i != "정":
        a.append(i)
print(a)

# %%
# 리스트 컴프리헨션
a = [i for i in b if i != "정"]
a

# %%
a = [1, 2, 3, 4]
# 새로운 리스트에 짝수에만 3을 곱해서 담고 싶다면
result2 = [num * 3 for num in a if num % 2 == 0]
result2

# %%
# 1 ~ 100 숫자 중에서 홀수만 담아서 새로운 리스트로 생성
a = [i for i in range(1, 101)]
b = [z for z in a if z % 2 != 0]
print(b)

# %%
list1 = ["nice", "study", "python", "anaconda", "!"]
# 5글자 이상의 요소만 담아서 새로운 리스트로 생성
list2 = [str1 for str1 in list1 if len(str1) >= 5]
print(list2)

# %%
list3 = ["A", "b", "c", "D", "e", "F", "G", "h"]
# 소문자만 담아서 새로운 리스트로 생성
list4 = [str1 for str1 in list3 if str1.islower()]
print(list4)

# %%
# [1,2,3,4] ==> [2,4,6,8]
print([x * 2 for x in [1, 2, 3, 4]])
# [0,1,2,3,4] ==> [0,1,4,9,16]
print([x * x for x in range(5)])

# %%
# [1,2,3]
# [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
print([[x, x + 1, x + 2] for x in [1, 2, 3]])

# %%
# 실습
# pass 빨간줄 미리 예방
parking_lot = []
top, car_name = 0, "A"
while True:
    no = int(input("[1] 자동차 넣기 | [2] 자동차 빼기 | [3] 종료"))
    if no <= 3:
        if no == 1:
            if top >= 5:
                print("주차장 꽉 찼음")
            else:
                parking_lot.append(car_name)
                print(f"{car_name} 자동차 들어감. 주차장 상태 ==> {parking_lot}")

                top += 1
                car_name = chr(ord(car_name) + 1)
        elif no == 2:
            if top > 0:
                outCar = parking_lot.pop()
                print(f"{outCar} 자동차 나감감. 주차장 상태 ==> {parking_lot}")
                top -= 1
                car_name = chr(ord(car_name) - 1)
            else:
                print("빠져나갈 자동차가 없음")
        else:
            print("프로그램 종료")
            break
    else:
        print("번호를 확인해 주세요")

# %%
# ord() : 특정 문자열 => 유니코드 값
# chr() : 유니코드 값 => 특정 문자열
print(ord("A"))
print(chr(65))

# %%
# enumerate() : 리스트, 튜플, 문자열 값을 입력받아서 인덱스 값을 포함하는 객체로 만들어 준다
list1 = ["body", "foo", "bar"]
for x in enumerate(list1):
    print(x)  # 기본은 튜플 형태로 리턴 (0, 'body') (1, 'foo') (2, 'bar')

for idx, value in enumerate(list1):
    print([idx, value])

# start= : 인덱스 시작값 지정 가능
for idx, value in enumerate(list1, start=1):
    print({idx, value})

# %%
