# %%
# 문자 처리
# 파이썬은 문자, 문자열 구분 안함 '' 사용 가능하지만 black formatter 가 설치되서 자동으로 "" 변경함
# "Life is too short, You need Python"  # 파이썬의 모토
# 'Life is too short, You need Python'
# '''Life is too short, You need Python'''
# """Life is too short, You need Python"""

multiline = """
    Life is too short
    You need Python
"""
multiline

# %%
# 문자열 결합 : +
str1 = "Python" + " is fun"
str1

# %%
# 문자열 반복 : *
"python" * 2

# %%
print("=" * 50)
print("My Program")
print("=" * 50)

# %%
# 문자열 인덱싱과 슬라이싱
# str1 = Python is fun
# 인덱싱
print(str1[3])
print(str1[5])
print(str1[-1])  # 오른쪽에서 부터 인덱싱

# %%
# 슬라이싱 [시작위치:끝나는위치] => 끝나는위치 는 포함 안함
str1 = "Life is too short, You need Python"
print(str1[0:])
print(str1[0:4])
print(str1[4:])
print(str1[4:8])
print(str1[:17])
print(str1[0:-4])

# %%
# len() : 길이함수
len(str1)

# %%
str2 = "20240510Sunny"
# 년월일 출력 : 20240510
print(str2[:8])
# 날씨 출력 : Sunny
print(str2[8:])

# %%
# 년월일 출력 : 2024-05-10
date = str2[:8]
year = date[:4]
month = date[4:6]
day = date[6:]
print(year, month, day, sep="-")

# %%
jumin = "901205-3234567"
# 주민등록번호 에서 1 or 3 면 남자, 2 or 4 면 여자
print(jumin[7])
no = int(jumin[7])

if no == 1 or 3:
    print("남자")
else:
    print("여자")

if no % 2 == 1:
    print("남자")
else:
    print("여자")
