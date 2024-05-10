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
