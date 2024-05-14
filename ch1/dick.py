# 딕셔너리 == Map
# list 와 같이 많이 쓰이는 자료형
# key, value 형태
# {} 사용
# 파이썬은 리스트와 딕셔너리 구조가 중요하다
# 딕셔너리 에서 get() 과 items() 를 많이 사용한다

# %%
# 생성
dict1 = {}
dict2 = {"name": "Song", "age": 12}
dict3 = {0: "Hello Python", 1: "Hello Coding"}
dict4 = {"arr": [1, 2, 3, 4, 5]}

# %%
print(dict2)
print(dict3)
print(dict4)

# %%
# 특정 키의 요소 출력
print(dict2["name"])
print(dict3[0])
print(dict4["arr"])

# %%
dict1["addr"]  # KeyError : 키가 없는 경우

# %%
# get()
dict1.get("addr")  # 키가없어도 에러가 안남

# %%
# 2024-05-14
# 데이터 추가 - 키와 값의 형태로 추가
dict2["birth"] = "0514"
dict2

# %%
dict3[2] = ["Hello Java", "Hello Oracle"]
dict3

# %%
# dick4 : rank키 => 튜플(16,17,18)값 추가
dict4["rank"] = (16, 17, 18)
dict4

# %%
numbers = [1, 2, 3, 4, 5, 6, 2, 4, 5, 7, 9, 8, 4, 5, 7, 1]
counter = {}
# {1:3, 2:4, 6:1}
# count()
for num in numbers:
    counter[num] = numbers.count(num)
print(counter)

# %%
# 데이터 삭제
del dict2["birth"]
dict2

# %%
# 1) keys() : key 리스트 리턴
dict2.keys()

# %%
# 2) values() : value 리스트 리턴
dict2.values()

# %%
# 3) items() : key, value 리턴
dict2.items()

# %%
# keys(), values(), items() 는 주로 for문 이랑 같이 사용한다
for k in dict2.keys():
    print(k)

# %%
for k, v in dict2.items():
    print((k, v))

# %%
# in : key 값이 있는지 확인 할수있다
"name" in dict1

# %%
"name" in dict2

# %%
# clear() : key, value 전부 제거
dict2.clear()
dict2

# %%
q1 = {"봄": "딸기", "여름": "토마토", "가을": "사과", "겨울": "귤"}
# 가을에 해당하는 과일 출력
str1 = q1.get("가을")
print("가을에 해당하는 과일 : ", str1)

for k in q1.keys():
    if k == "가을":
        print("for문 : ", q1[k])

# 사과가 포함되었는지 확인
# in
"사과" in q1.values()
# 삼항연산자
str2 = "사과가 포함됨" if "사과" in q1.values() else "사과가 포함되지 않음"
print(str2)

# %%
