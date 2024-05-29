import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

ws.title = "네이버책검색API"
ws.column_dimensions["B"].width = 30
ws.column_dimensions["C"].width = 100
ws.column_dimensions["D"].width = 15

# 제목 행 삽입
ws.append(["번호", "isbn", "책제목", "가격"])

# 네이버 개발자 센터 검색후 -> Products -> 검색 -> 책

headers = {
    "X-Naver-Client-Id": "OXcNjlND9NccBIPZPnUa",
    "X-Naver-Client-Secret": "V8_FpCZ4lA",
}

start, num = 1, 1
for idx in range(3):
    # idx = 0 ~ 2
    start_num = start + (idx * 100)
    url = "https://openapi.naver.com/v1/search/book.json"
    # 베르나르 베르베르 작가로 책 검색해보기
    params = {"query": "베르나르 베르베르", "display": "100", "start": str(start_num)}
    response = requests.get(url, headers=headers, params=params)
    # print(response.url) # 주소 잘 만들어졌는지 확인

    # json 가져오기
    data = response.json()

    for idx, item in enumerate(data["items"], 1):
        # print(f"{idx} - 제목 : {item["title"]},\t 링크 : {item["link"]}") # <b>아이폰</b>
        ws.append([num, item["isbn"], item["title"], item["discount"]])
        num += 1

base_dir = "./crawl/file/"  # ipynb 에서 할때랑 경로 잡는게 틀리다 (터미널에 PS E:\source\pythonsource> 까지만 되있음)
wb.save(base_dir + "naverbook.xlsx")  # 파일명 으로 저장
wb.close()
