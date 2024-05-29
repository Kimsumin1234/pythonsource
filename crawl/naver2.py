import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from openpyxl import Workbook
import re  # 정규식 사용 라이브러리

# 워크북 생성 openpyxl workbook 생성
wb = Workbook()
ws = wb.active

ws.title = "네이버오픈API"  # 시트명
ws.column_dimensions["B"].width = 100  # 셀 너비 조정
ws.column_dimensions["C"].width = 60  # 셀 너비 조정

ws.append(["순위", "상품명", "판매경로"])

# naver.py 에서 했던 크롤링 작업을 네이버 측에서는 오픈API 로 제공을 해준다
# 네이버 개발자 센터 검색후 -> Products -> 검색 -> 오픈API

headers = {
    "X-Naver-Client-Id": "OXcNjlND9NccBIPZPnUa",
    "X-Naver-Client-Secret": "V8_FpCZ4lA",
}

start, num = 1, 1
for idx in range(10):
    # idx = 0 ~ 9
    start_num = start + (idx * 100)
    url = "https://openapi.naver.com/v1/search/shop.json"
    params = {"query": "아이폰", "display": "100", "start": str(start_num)}
    response = requests.get(url, headers=headers, params=params)
    # print(response.url) # 주소 잘 만들어졌는지 확인

    # json 가져오기
    data = response.json()

    for idx, item in enumerate(data["items"], 1):
        # print(f"{idx} - 제목 : {item["title"]},\t 링크 : {item["link"]}") # <b>아이폰</b>

        # 정규식을 사용해서 태그 정리 <b>아이폰</b> => 아이폰
        title = re.sub("<.*?>", "", item["title"])

        ws.append([num, title, item["link"]])
        num += 1

base_dir = "./crawl/file/"  # ipynb 에서 할때랑 경로 잡는게 틀리다 (터미널에 PS E:\source\pythonsource> 까지만 되있음)
wb.save(base_dir + "naver.xlsx")  # 파일명 으로 저장
wb.close()
