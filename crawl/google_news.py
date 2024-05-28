import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from urllib.error import HTTPError

# 파이썬 으로 구글뉴스 기사 크롤링 하기


def main(keyword):
    url = "https://news.google.com/search?q=" + keyword + "=ko&gl=KR&ceid=KR%3Ako"

    try:
        with requests.Session() as s:
            reponse = s.get(url)
            soup = BeautifulSoup(reponse.text, "lxml")

            news_clipping = data_extract(soup)
            for news in news_clipping:
                for k, v in news.items():
                    print(f"{k} : {v}")
                print()
    except HTTPError as e:
        print(e.code)


def data_extract(soup):
    base_url = "https://news.google.com"

    # 기사를 딕셔너리로 담고 리스트에 추가한후 리턴해보기
    news = []
    news_items = {}

    # #yDmH0d > c-wiz > div > main > div.UW0SDc > c-wiz > c-wiz:nth-child(1) > c-wiz > article > div.m5k28 > div.B6pJDd > div > a
    articles = soup.select("div.UW0SDc article")
    for article in articles:
        link_title = article.select_one("div > div:nth-child(2) a")

        # 제목 추출
        # title = link_title.text
        news_items["title"] = link_title.text

        # 뉴스기사 링크 추출
        # 추출 : ./articles/CBMiMGh0dHA6Ly93d3cuYm9hbm5ld3MuY29tL21lZGlhL3ZpZXcuYXNwP2lkeD05NTg4M9IBAA?hl=ko&gl=KR&ceid=KR%3Ako
        # 추출한걸 써먹을려면 ./ => https://news.google.com/ 이걸로 바꿔야 한다
        # href = base_url + link_title["href"][1:]
        news_items["href"] = base_url + link_title["href"][1:]

        # 작성자 추출
        # #yDmH0d > c-wiz > div > main > div.UW0SDc > c-wiz > c-wiz:nth-child(4) > c-wiz > article > div.m5k28 > div.B6pJDd > div > div > div.oovtQ > div > div
        # writer = article.select_one("div.a7P8l > div").text
        news_items["writer"] = article.select_one("div.a7P8l > div").text

        # 작성일자와 시간 추출
        # #yDmH0d > c-wiz > div > main > div.UW0SDc > c-wiz > c-wiz:nth-child(4) > c-wiz > article > div.UOVeFe > time
        # T 를 기준으로 분리
        time = article.select_one("div.UOVeFe > time")
        if time:
            time = time["datetime"].split("T")  # 리스트 형태로 리턴
            # time_date = time[0]
            news_items["time_date"] = time[0]
            # time_time = time[1]
            news_items["time_time"] = time[1]
        else:
            # time_date = ""
            news_items["time_date"] = ""
            # time_time = ""
            news_items["time_time"] = ""

        # print("제목 :", title)
        # print("뉴스링크 :", href)
        # print("작성자 :", writer)
        # print(f"작성일자 : {time_date} , 작성시간 : {time_time}")

        news.append(news_items)
        news_items = {}  # 기존꺼 내용 초기화 (루프한번 돌고 내용비우는 작업)

    # 확인
    # print(news[:3])
    return news


# [
#     {
#         "title": "오픈소스 커뮤니티 노리는 공급망 공격, 국내 연구팀 기술로 차단한다",
#         "href": "",
#         "writer": "",
#         "time_date": "",
#         "time_time": "",
#     }
# ]

# 모듈 테스트용
if __name__ == "__main__":
    main("아이폰")
