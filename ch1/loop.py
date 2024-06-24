# %%
# while / for 구문도 {} 를 안쓰기 때문에 tab 구별 잘하기
# 파이썬은 i++ 같은건 사용 못함
i = 1
while i < 11:
    print(i)
    i += 1  # i = i + 1

# %%
# 1 ~ 100 사이의 짝수만 출력
i = 1
while i < 101:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1
# %%
i = 0
while i <= 98:
    i += 2
    print(i, end=" ")

# %%
# 1 ~ 100 합계 구한후 출력
i = 1
sum1 = 0  # sum 이라는 함수가 있기 때문에 1을 붙여준다
while i <= 100:
    sum1 += i
    i += 1

print(f"1 ~ 100 합계 : {sum1}")

# %%
# 6단 구구단 출력
i = 1
six = 6
while i < 10:
    print("%d * %d = %2d" % (six, i, (six * i)))
    i += 1

# %%
# 사용자로부터 입력을 받은 후 화면 출력
# q 라는 문자 입력 시 입력 받는 것 중단
while True:
    msg = input("글자를 입력하시오 (q를 입력하면 입력중단)")
    print(msg)
    if msg == "q":
        break
# %%
# 파이썬 for 구문
# for 변수명 in 범위:
range(5)  # 범위
print(list(range(5)))  # [0, 1, 2, 3, 4]
print(list(range(1, 5)))  # [1, 2, 3, 4]
print(list(range(1, 11, 2)))  # 2씩증가 해서 홀수만출력 [1, 3, 5, 7, 9]

# %%
# Jupyter 가 설치되있느면 변수 하나만 확인 할떄는 print() 안써도됨
i = 10
i

# %%
for i in range(10):
    print(i, end=" ")  # 0 1 2 3 4 5 6 7 8 9

for i in range(1, 11):
    print(i, end=" ")  # 1 2 3 4 5 6 7 8 9 10

# %%
# 1 ~ 100 까지 홀수만
for i in range(1, 101, 2):
    print(i, end=" ")

# %%
# 1 ~ 100 까지 합계 구하기
sum1 = 0
for i in range(1, 101):
    sum1 += i
sum1

# %%
# sum() 함수 사용해서 합계 구하기
print(sum(range(1, 101)))  # 1 ~ 100 까지 합계 : 5050
print(sum(range(1, 101, 2)))  # 홀수 합계 : 2500

# %%
range(10, 1)
print(list(range(10, 1)))  # []

# 거꾸로 가려면 -1 을 알려줘야 한다
print(list(range(10, 1, -1)))  # [10, 9, 8, 7, 6, 5, 4, 3, 2]
print(list(range(10, -1, -1)))  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# %%
# 사용자로부터 숫자를 입력받은 후 1 부터 사용자 입력 숫자까지 합계 구한 뒤 출력
num1 = int(input("숫자를 입력해 주세요"))

# print(f"1 ~ 사용자 입력 숫자까지 합계 : {sum(range(1, (num1+1)))}")

sum1 = 0
for i in range(1, num1 + 1):
    sum1 += i
print(f"1 ~ {num1} 까지 합계 : {sum1}")

# %%
# 문자열에서 문자 하나씩 가져오기
for s in "dreams":
    print(s, end=" ")

# %%
# 3행 3열로 출력하기
for i in range(3):
    for j in range(3):
        print(j, end=" ")
    print()

# %%
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()

# %%
# 구구단 2 ~ 9단 출력
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i*j}", end=", ")
    print()

# %%
# [] 리스트 (파이썬은 배열이 없음) : 자바스트립트 배열 과 유사
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 38]
for num in numbers:
    print(num)

# %%
# break
i = 1
while i < 11:
    if i == 5:
        break
    print(i, end=" ")
    i += 1

# %%
# continue
i = 1
while i < 11:
    i += 1
    if i % 2 == 1:
        continue
    print(i, end=" ")

# %%
