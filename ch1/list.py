# %%
# 숫자, 문자열

# 데이터 모임 표현 : list(리스트 == [자바] ArrayList or 배열), dict(딕셔너리 == [자바] Map), set(== [자바] HashSet), tuple()
# 파이썬은 동일한 타입만을 담지 않음

# %%
# 리스트 생성
list1 = []
list2 = [1, 2, 3, 4, 5, 6]
list3 = [1, "a", 3, "b", 5, 6]
list4 = [1, 2, 3, 4, 5.5, 6.7]
list5 = [1, 2, 3, 4, ["Life", "is", "short"]]
list6 = list([3, 4, 5])  # 리스트 함수도 있다

# %%
# 출력
print(list5)

# %%
# 리스트 인덱싱 / 슬라이싱
print(list2[2])
print(list2[-2])
print(list2[-1])
print(list5[-1])  # ['Life', 'is', 'short']
print(list5[4][0])
print(list5[4][2])

# %%
list7 = [1, 2, 3, 4, ["a", "b", ["Life", "is"]]]
print(list7[-1][-1][1])  # is

# %%
print("list2 : ", list2)
print(list2[2:4])
print(list2[:4])
print(list2[:-1])

# %%
list5 = [1, 2, 3, 4, ["Life", "is", "short"]]
print(list5[4:])  # [['Life', 'is', 'short']] 2차원 리스트 형태로 잘려짐
print(list5[4][:2])  # ['Life', 'is']

# %%
# 리스트 연산자
# + : 연결
print(list2 + list3)
print(list5 + list6)
print(list2[1] + list3[0])  # 요소+요소는 산술 2+1=3

# %%
# * : 반복
print(list2 * 2)

# %%
# len() : 길이
print(len(list2))
print(len(list5))

# %%
# 리스트 수정 / 삭제
list2[0] = 7  # 수정
print(list2)

list2[1] = [10, 11, 12]
print(list2)

del list2[1]  # 삭제
print(list2)

del list2[2:]  # 범위지정 가능
print(list2)

# %%
for i in list3:
    print(i, end="\t")

# %%
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
# 100 이상의 요소만 출력
for i in numbers:
    if i >= 100:
        print(i, end=" ")
# %%
# numbers 홀수, 짝수 구분하여 출력
for i in numbers:
    if i % 2 == 0:
        print("{} 는 짝수".format(i))
    else:
        print("{} 는 홀수".format(i))

# %%
# 숫자의 자릿수 출력
for i in numbers:
    print("{} : {} 자리".format(i, len(str(i))))

# %%
# 리스트 함수
# 1) append() : 리스트 끝에 요소 추가하기
list3.append(["c", "d", "e"])
print(list3)
list3.append(5)
print(list3)

# %%
# 1 ~ 100 까지 숫자 중에서 짝수만 리스트로 생성
even = []
for i in range(1, 101):
    if i % 2 == 0:
        even.append(i)
print(even)

# %%
# 2) sort() : 오름차순 정렬(기본)
a = [1, 4, 3, 2]
a.sort()
print(a)
a = ["a", "e", "g", "b", "c"]
a.sort()
print(a)  # 문자도 정렬해준다
a = ["ㅎ", "ㄱ", "ㅈ", "ㅁ", "ㅋ"]
a.sort()
print(a)  # 한글도 정렬해준다

# %%
# 3) reverse() : 리스트 뒤집기
print(list4)
list4.reverse()
print(list4)  # 정렬을 해주는게 아니고 뒤집기만 함

# %%
# 4) index() : 위치 값 리턴
# 리스트에 find() 는 없음
list4.index(3)
list4.index(6)  # ValueError : 찾는게 없는 경우

# %%
# 5) remove() == del
# list4.remove(4)
print(list4)
list4.append(5.5)  # [6.7, 5.5, 3, 2, 1, 5.5]
print(list4)
list4.remove(5.5)  # 처음만난 요소만 삭제
print(list4)

# %%
# 6) pop() : 맨 마지막 리스트 요소 꺼내서 제거
list4.pop()
print(list4)

# %%
# 위치를 지정해 꺼내서 제거 가능
list4.pop(1)
print(list4)

# %%
# 7) count(찾을요소) : 찾을요소 개수 리턴
list4 = [12, 13, 14, 15, 14]
list4.count(14)

# %%
# 8) extend : + 같은 역할
list4.extend([16, 17, 18])
list4

# %%
# 9) clear() : 리스트 요소 모두 삭제
list4.clear()
list4

# %%
# 내림차순 정렬
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
numbers.sort(reverse=True)
print(numbers)

# %%
# 파이썬에서 False 에 해당 : "", [], (), {}, 0
city = ""
list8 = []
if city:
    print("비어있지 않음")
else:
    print("비어있음")

if list8:
    print("비어있지 않음")
else:
    print("비어있음")

# %%
fruits = ["딸기", "바나나", "사과", "배", "수박"]
# in == sql(in 연산자)
if "딸기" in fruits:
    print("딸기 요소가 포함됨")
# 포함여부 도 확인가능
print("메론" not in fruits)

# %%
a_class = [70, 60, 55, 75, 92, 80, 85, 100, 87, 65]
total = 0
# a_class 평균과 총합을 구하시오
for num in a_class:
    total += num
print(f"총합 : {total}, 평균 : {total/len(a_class)}")
# sum() 사용
print(f"총합 : {sum(a_class)}, 평균 : {sum(a_class)/len(a_class)}")

# %%
