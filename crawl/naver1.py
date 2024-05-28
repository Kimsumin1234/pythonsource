import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from urllib.error import HTTPError

# naver.py 에서 했던 크롤링 작업을 네이버 측에서는 오픈API 로 제공을 해준다
# 오픈API 로 가져올수있으면 오픈API 를 사용하는게 더 편하다
# 네이버 개발자 센터 검색후 -> Products -> 검색 -> 오픈API
# Client ID : OXcNjlND9NccBIPZPnUa
# Client Secret : V8_FpCZ4lA

# 뉴스 검색은 검색 API를 사용해 네이버 검색의 뉴스 검색 결과를 반환하는 RESTful API입니다. => 데이터 형태를 json 이나 xml 형태로 보내는 방식

# 요청 URL : https://openapi.naver.com/v1/search/news.json
# 파라미터 : URL ? 뒤에 붙는 것들  ex) https://openapi.naver.com/v1/search/news.json?query=
# 파라미터 필수여부 : Y 는 꼭 있어야 하는것

# 포스트맨으로 테스트
# + 버튼 눌러서 REST API 베이직으로 생성
# naver 오픈API => Variables => id 는 삭제 , base_url(Inital value,Current value) 에 요청 URL 넣기 => save
# Get data => Params => 기존에 있는거 지우고 key 에 query 추가 value 는 검색어 아무거나
# Get data => Headers => X-Naver-Client-Id , X-Naver-Client-Secret 추가 (네이버 개발자 센터 검색후 -> Products -> 검색 -> 개발가이드 보기 -> 뉴스탭 -> 참고사항 참고)
# 저장후 send 해도 인증에실패했습니다 메세지는 안나오고 제대로 나오게 된다

url = "https://openapi.naver.com/v1/search/news.json"

headers = {
    "X-Naver-Client-Id": "OXcNjlND9NccBIPZPnUa",
    "X-Naver-Client-Secret": "V8_FpCZ4lA",
}

# with requests.Session() as s:
#     response = s.get(url, headers=headers)
# soup = BeautifulSoup(reponse.text, "lxml") # 지금은 soup 이 필요가없다 (soup 을 사용하는 경우는 html 형태로 내려올때 사용)

response = requests.get(url, headers=headers, params={"query": "파이썬"})
# json 가져오기
data = response.json()
# print(data["items"])  # 포스트맨 에서 "items" 확인
for idx, item in enumerate(data["items"], 1):
    print(f"{idx} - 제목 : {item["title"]},\t 링크 : {item["link"]}")
