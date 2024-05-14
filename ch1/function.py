# 함수
# 파이썬은 클래스 생성보다 함수를 만들어서 쓰는 형태가 많다

# 함수 기본구조
# def 함수명(매개변수):
#     수행할 문장1
#     수행할 문장2
#     .
#     .
#     .


# %%
# 함수 생성
def hello():
    print("Hello !!!")


hello()  # 함수 호출


# %%
def add(a, b):
    return a + b


add(5, 3)


# %%
# 매개변수에 기본값을 줄수있다
# 기본값 : 값이 안 넘어오는 경우 사용
def sub(a, b=3):
    return a - b


print(sub(9, 5))
print(sub(9))


# %%
# 가변 매개변수 : 입력값이 몇개가 될지 모르는 경우 사용 *
#                 입력값을 모아서 튜플로 만들어 줌
def add_many(*args):
    print(args)


add_many(1, 2, 3)
add_many(1, 2, 3, 4, 5, 6, 7)
add_many("35", "24", "65", "98")
add_many({"dessert": "macaroon", "wine": "marlot"})


# %%
def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result


print(add_many(1, 2, 3))
print(add_many(1, 2, 3, 4, 5, 6, 7))


# %%
# TypeError: add_many() missing 1 required keyword-only argument: 'choice' : add_many(*args, choice)
# 가변매개변수 와 일반 매개변수가 섞일때 가변매개변수를 맨 뒤에 선언
def add_many(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result += i
    return result


print(add_many("add", 1, 2, 3))
print(add_many("mul", 1, 2, 3, 4, 5, 6, 7))


# %%
# 키워드 매개변수 : kwargs
# 입력값을 모아서 딕셔너리로 만들어 줌
def print_kwargs(**kwargs):
    print(kwargs)


print_kwargs(name="foo", age=3)  # {'name': 'foo', 'age': 3}
print_kwargs(name="foo", age=3, addr="seoul")


# %%
# 일반, 가변, 키워드 매개변수 섞이는 경우
def print_kwargs(arg1, arg2=5, *args, **kwargs):
    print(arg1, arg2, args, kwargs)


print_kwargs(10, 20)  # 10 20 () {} 매개변수에 값이 안들어와도 에러 안남
print_kwargs(10, 20, "park", "kim")
print_kwargs(10, 20, "park", "kim", age=25, name="choi")


# %%
# 리턴값
# 파이썬은 여러개를 리턴할수 있는거 처럼 보이지만 내부적으로는 튜플() 묶어서 하나로 리턴
def add_and_mul(a, b):
    return a + b, a * b


print(add_and_mul(3, 4))

hap, mul = add_and_mul(5, 6)
print(hap, mul)


# %%
# return [] 리스트로 리턴 가능 (기본은 튜플)
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]


print(func_mul(100))


# %%
def say_nick(nick):
    if nick == "바보":
        return
    print(f"나의 별명은 {nick} 입니다.")


say_nick("바보")  # "바보" 는 return 됨
say_nick("고양이")

# %%


# 두 개의 숫자와 연산자를 입력받아 사칙연산 함수
def four_rules(num1, num2, op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    else:
        return print("연산을 다시 입력해주세요")


num1 = int(input("숫자1을 입력해 주세요"))
op = input("연산자(+, -, *, /)를 입력해주세요")
num2 = int(input("숫자2를 입력해 주세요"))
print(f"{num1} {op} {num2} = {four_rules(num1,num2,op)}")

# %%
a = 1


def vartest(a):
    # 함수 안에서 선언한 변수는 함수 안에서만 유효하다
    a = a + 1


vartest(a)
print(a)

# %%
a = 1


def vartest(a):
    # 함수 안에서 선언한 변수는 함수 안에서만 유효하다
    a = a + 1


a = vartest(a)
print(a)

# %%
a = 1


def vartest(a):
    # 함수 안에서 선언한 변수는 함수 안에서만 유효하다
    # 함수 안에 선언한 변수를 리턴해주면 된다
    a = a + 1
    return a


a = vartest(a)
print(a)

# %%
a = 1


def vartest():
    # global 사용 바깥에 있는 변수라고 선언
    # 이 방법은 추천하지 않음 return 방법을 추천
    global a
    a = a + 1


vartest()
print(a)

# %%
# 1 ~ 100 숫자 중에서 소수에 해당하는 숫자를 찾아서 리스트에 담기
# 소수 : 1 과 자기 자신으로 나누어 떨어지는 숫자
#        2,3,5 ... 97
primes = []


def isPrime(x):
    # x 가 소수이면 primes 에 추가
    cnt = 0
    for i in range(1, x + 1):
        if x % i == 0:
            cnt += 1
    # 소수이면 0으로 떨어지는게 2개뿐이다
    if cnt == 2:
        primes.append(x)


for j in range(1, 101):
    isPrime(j)  # isPrime() 호출

print(primes)

# %%
