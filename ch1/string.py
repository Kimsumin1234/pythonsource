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

# 2024-05-13
# %%
str1 = "파이썬 프로그래밍"
for s in str1:
    print(s)
# %%
str1 = "파이썬프로그래밍"
for s in str1:
    print(s, end="♥")

# %%
# 사용자로부터 숫자입력받기 => 5
num1 = input("숫자를 입력해주세요")
for i in range(len(num1)):
    for j in range(int(num1[i])):
        print("♥", end="")
    print()

# %%
# 문자열 함수
# 1) count() : 문자열에 포함된 특정 문자열 개수
str1 = "hobby"
print("a 문자열에 포함된 b 개수 %d" % str1.count("b"))

# %%
# 2) find() : 문자열 위치
str1 = "Python is the best choice"
print("a 문자열에 b 위치 %d" % str1.find("b"))
print("a 문자열에 b 위치 {}".format(str1.find("b")))
print(f"a 문자열에 b 위치 {str1.find("b")}")
print("a 문자열에 b 위치 ",str1.find("b"))

# %%
# 3) index() : 문자열 위치
print("a 문자열에 b 위치 %d" % str1.index("b"))

# %%
# find() vs index()
# 찾는문자가 존재하지 않는경우 : -1 vs ValueError:
print("a 문자열에 b 위치 %d" % str1.find("K")) # -1
# print("a 문자열에 b 위치 %d" % str1.index("K")) # ValueError: substring not found

# %%
# startswith(~로 시작하는가) / endswith(~로 끝나는가)
str2 = "Python Is Easy Programming"
print(str2.startswith("P"))
print(str2.endswith("P"))

# %%
# 5) join()
",".join("abcdefg") # 'a,b,c,d,e,f,g'

# 리스트나 튜플을 문자열로 변경 시 많이 사용됨
list1=["a","b","c","d","e"]
print("".join(list1)) # abcde

# %%
# 6) upper / lower / swapcase / title : 대소문자 변경
a = "abcde"
print("소문자 => 대문자 ",a.upper())
a = "ABCDE"
print("대문자 => 소문자 ",a.lower())
a = "Python is Easy"
print("대문자 소문자 상호 변환",a.swapcase())
a = "python is easy"
print("단어의 제일 앞 글자만 대문자 변환",a.title())

# %%
# 파이썬은 대소문자 구별한다
"abc" == "ABC"

# %%
# 7) lstrip / rstrip / strip : 공백 제거
a = "        hi"
print(a)
print(a.lstrip())

a = "hi        "
print(a)
print(a.rstrip())

a = "        hi        "
print(a)
print(a.strip())

# %%
# 8) replace() : 문자열 변경
a = "Life is too short"
a.replace("Life","Your leg")

# %%
# 9) split() : 문자열 나누기
print(a.split()) # 기본값 : 공백기준
b="a:b:c:d"
print(b.split(":")) # 기준을 정할수있다

# %%
# 10) splitlines() : 엔터 기준 나누기
c="하나\n둘\n셋"
print(c.splitlines())
print(c.split("\n"))

# %%
# 11) is~ : True, False 로 리턴(문자열 구성 파악)
print("1234".isdigit())
print("abcd".isalpha())
print("abc123".isalnum()) # 알파벳 + 숫자
print("abcd".islower())
print("ABCD".isupper())
print("    ".isspace())

# %%
# 대문자 <=> 소문자
name = "KennRY"
print(name.swapcase())
# 직접 해볼경우
for s in name:
    if s.islower():
        print(s.upper(),end="")
    else:
        print(s.lower(),end="")

# %%
# 년월일 입력 받은 후 10년 후 날짜 출력
# 2024/05/13 (입력예시)
day = input("년월일 입력(예시 2024/05/13)")
position = day.find("/")
year = int(day[:position])+10
print("입력한 날짜의 10년후 %s"%(str(year)+"년"+day[5:7]+"월"+day[8:]+"일"))
# 두번째
# day1 = day.split("/")
# print(int(day1[0])+10,day1[1],day1[2],sep="/")

# %%
# 사이트별 비밀번호 작성
# http://naver.com
# 규칙1 -  http:// 제외 : naver.com
# 규칙2 -  처음에 나오는 . 이후 부분은 제외 : naver
# 규칙3 -  남은 글자 중 처음 세자리 + 글자 개수 + 글자 내 'e' 문자 개수 + '!' 로 구성 : nav51!
password = input("사이트주소 입력(http://naver.com)")
print(password[7:])
print(password[7:].split(".")[0])
password1 = password[7:].split(".")[0]
print(password1[0:3]+str(len(password1))+str(password1.count("e"))+"!")
