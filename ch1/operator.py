# 연산자
a, b = 5, 3
print(a + b)
print(a - b)
print(a * b)
print(a / b) # 1.6666666666666667 (자바는 몫만 나옴 : 1 , 스크립트 : 1.6666666666666667)
print(a // b) # 몫만
print(a % b) # 나머지만
print(a ** b) # 제곱 (5의3승)

# 복합 대입연산자
a += 5
print(a)
a *= 5
print(a)
a %= 5
print(a)

# 동전교환
money, c500, c100, c50, c10 = 0,0,0,0,0
money = 7777

# 500원: 15개, 100원: 2개, 50원: 1개, 10원: 2개, 나머지돈: 7원