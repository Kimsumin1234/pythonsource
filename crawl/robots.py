# 크롤링 : 주기적으로 / 무작위로 데이터 수집

# 패키지 설치 (패키지마다 목적이 다르다, 다양하게 섞어서 사용)
# 1. (venv) E:\source\pythonsource\venv\Scripts>pip install requests : 웹 서버로 요청시 사용
# 2. (venv) E:\source\pythonsource\venv\Scripts>pip install beautifulsoup4
# 3. (venv) E:\source\pythonsource\venv\Scripts>pip install selenium

import requests

urls = ["https://www.naver.com/", "https://www.python.org/"]

file_name = "robots.txt"

for url in urls:
    robots = requests.get(url + file_name)  # 2개의 사이트에 get 방식으로 요청
    print(robots.text)  # 사이트마다 요즘에는 robots.text 가 다 들어있다

# 데이터수집(로봇) : f12 누르고 Elements 에 있는 코드를 전부 긁어서 원하는 항목만 추출
# 사이트가 구조변경을 하면 Elements 가 바뀌기 때문에 크롤러를 다시 만들어야 한다
# 로봇으로 서버에 데이터수집요청 보내면 서버는 파이썬으로 요청 보냈다는걸 알수있다
# 서버에서 로봇으로 요청 들어온걸 막을수있음

# robots.text
# 크롤링을 할수있는지 여부나, 크롤링을 어디까지 할수있는지 범위설정 이러한 것들이 기록되있다
# User-agent: *
# Disallow: /
# Allow : /$
