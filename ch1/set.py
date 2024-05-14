# set(집합)
# 중복 허용하지 않음
# 순서 없음 : 인덱싱을 할수없음

# %%
# set() 생성
set1 = set()
set2 = set([1, 2, 3, 4])
set3 = set([1, 4, 5, 6, 6])

# %%
print(set2)
print(set3)  # {1, 4, 5, 6} 중복x

# %%
# set을 인덱싱 하기위해서는 리스트나 튜플로 변환해야한다
# list(), tuple()
list1 = list(set2)
tuple1 = tuple(set3)
print(list1)
print(tuple1)

# %%
set4 = set("abcdefg")  # {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
set4

# %%
# dict => set 으로 변경시 key 값만 가져온다
dict1 = {"no": 1, "name": "hong", "age": 25}
set(dict1)

# %%
list1 = [1, 2, 3, 4, 5]
set(list1)

# %%
# 집합함수
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
# 교집합
print(s1 & s2)
print(s1.intersection(s2))
# 합집합
print(s1 | s2)
print(s1.union(s2))
# 차집합
print(s1 - s2)
print(s1.difference(s2))

# %%
# 한개 데이터 추가 : add()
s1.add(7)
s1

# %%
# 여러개 데이터 추가 : update()
s1.update([9, 10, 11])
s1

# %%
# 데이터 제거 : remove()
s1.remove(2)
s1

# %%
