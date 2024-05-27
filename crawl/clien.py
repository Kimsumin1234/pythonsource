import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from xlsx_write import write_excel_template  # 내가 만든 엑셀 파일 저장 모듈 import
from datetime import datetime  # 오늘날짜

# 클리앙 팁과강좌 게시판 크롤링 해보기
# 원래는 크롤링을 할때 약간의 텀을 줘야한다, 텀을 안주고 지금처럼 빠르게 요청을 계속 보내면 공격으로 인식해서 응답을 안해줄수있다


userAgent = UserAgent()
headers = {"user-agent": userAgent.chrome}

lists = []  # 엑셀 파일 저장

with requests.Session() as s:

    for page in range(5):
        url = "https://www.clien.net/service/board/lecture?&od=T31&category=0&po="
        url = url + str(page)
        reponse = s.get(url, headers=headers)  # str(page) : 페이지번호 추가

        soup = BeautifulSoup(reponse.text, "lxml")

        # # 타이틀 출력
        # # #div_content > div.list_content > div:nth-child(7) > div.list_title > a.list_subject > span.subject_fixed
        # titles = soup.select("div.list_title > a > span.subject_fixed")

        # # 날짜 출력
        # # #div_content > div.list_content > div:nth-child(1) > div.list_time > span > span
        # times = soup.select("div.list_time > span > span")

        # for idx, title in enumerate(titles, 1):
        #     print(
        #         title.text.strip(), times[idx].text.strip()[:10]
        #     )  # 2017-05-07 01:52:42 - [:10]

        #     lists.append(
        #         [title.text.strip(), times[idx].text.strip()[:10]]
        #     )  # 엑셀 파일 저장 (이방법은 에러가 발생, idx 가 맞지않아서)
        # print()  # 한페이지가 끝나면 엔터주기

        # 행 가져오기
        rows = soup.select("div.list_content > div.list_item.symph_row")

        for row in rows:
            title = row.select_one("div.list_title > a > span.subject_fixed")
            time = row.select_one("div.list_time > span > span")

            print(title.text.strip(), time.text.strip()[:10])

            lists.append([title.text.strip(), time.text.strip()[:10]])
        print()

    # 파일 저장 : 파일명 - clien_240527.xlsx , 시트명 - 팁과강좌
    today = datetime.now().strftime("%Y%m%d")
    write_excel_template(f"clien_{today}.xlsx", "팁과강좌", lists)
