from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains  # 2024-05-31
import time

# import urllib.request as req
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

# (venv) E:\source\pythonsource\venv\Scripts>pip install pandas
import pandas as pd


# 스크롤 길이를 알아야한다 (스크롤을 내리면 계속 스크롤이 생기기 때문에 )
def main():
    browser = set_chrome_driver()
    url = "https://www.youtube.com/watch?v=0XZCb5SA75g"
    browser.get(url)

    time.sleep(2)

    # 스크롤 제어 (동적으로 작성된 페이지)
    interval = 5
    # 유튜브는 body 가 아니라 documentElement 를 써야한다
    # prev_height = browser.execute_script("return document.body.scrollHeight")
    prev_height = browser.execute_script("return document.documentElement.scrollHeight")

    while True:
        browser.execute_script(
            "window.scrollTo(0, document.documentElement.scrollHeight)"
        )
        time.sleep(interval)
        cur_height = browser.execute_script(
            "return document.documentElement.scrollHeight"
        )

        if cur_height == prev_height:
            break

        prev_height = cur_height

    time.sleep(3)

    # 전체 소스를 BeautifulSoap 에 담기
    soup = BeautifulSoup(browser.page_source, "lxml")

    # 댓글 사용자의 아이디 및 코멘트 가져오기
    user_id = soup.select("#author-text > span")
    user_comment = soup.select("#content-text > span")

    # 확인
    # for idx in range(len(user_id)):
    #     print(user_id[idx].text.strip(), user_comment[idx].text.strip())

    # 리스트 구조로 만들기
    ids_list = []
    comments_list = []
    for idx in range(len(user_id)):
        clean_id = user_id[idx].text.strip()  # 공백제거
        clean_id = clean_id.replace("\n", " ")  # 공백제거
        clean_id = clean_id.replace("\t", " ")
        ids_list.append(clean_id)

        clean_comments = user_comment[idx].text.strip()
        clean_comments = clean_comments.replace("\n", " ")
        clean_comments = clean_comments.replace("\t", " ")
        comments_list.append(clean_comments)

    # 데이터프레임 생성
    # 판다스를 이용해서 크롤링한 데이터를 csv 파일로 간단하게 변환할수있다
    dict_data = {"Id": ids_list, "Comments": comments_list}
    df = pd.DataFrame(dict_data)

    df.to_csv("./crawl/file/youtube.csv", index=False, encoding="utf-8-sig")

    time.sleep(5)


def set_chrome_driver():
    options = ChromeOptions()
    # options.add_argument("--start-maximized")  # 최대화 시키면 스크롤이 잘 안내려가서 일단 막음
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    return driver


# 테스트 실행
if __name__ == "__main__":
    main()
