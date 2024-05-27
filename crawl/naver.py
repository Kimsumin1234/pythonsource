import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

# 네이버 증권 크롤링 해보기


url = "https://finance.naver.com/"

userAgent = UserAgent()
headers = {"user-agent": userAgent.chrome}

with requests.Session() as s:
    reponse = s.get(url, headers=headers)
    # print(reponse.text)
    print(reponse.status_code)  # 200 , 요청이 잘 들어감 확인
    soup = BeautifulSoup(reponse.text, "lxml")

    cotaniners = soup.select("div.aside_area.aside_stock > table > tbody > tr th a")
    for item in cotaniners:
        print(item.get_text())

print()

with requests.Session() as s:
    reponse = s.get(url, headers=headers)

    soup = BeautifulSoup(reponse.text, "lxml")

    cotaniners2 = soup.select("div.aside_area.aside_popular > table > tbody > tr")

    for item in cotaniners2:
        # 회사명
        company_name = item.select_one("a").string
        # 현재금액
        current_amount = item.select_one("td").string
        print(f"회사명 :{company_name} , 현재금액 :{current_amount}")
