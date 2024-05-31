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


def main():
    browser = set_chrome_driver()
    # 네이버 사이트 띄우기
    browser.get("https://www.naver.com/")
    time.sleep(2)

    # 검색어 입력
    element = browser.find_element(By.ID, "query")
    element.send_keys("아이스크림")
    element.send_keys(Keys.ENTER)
    time.sleep(3)

    # 이미지 버튼 클릭
    # element = browser.find_element(
    #     By.XPATH, "//*[@id='lnb']/div[1]/div/div[1]/div/div[1]/div[1]/a"
    # )
    element = browser.find_element(By.CSS_SELECTOR, "div.api_flicking_wrap > div > a")
    element.click()
    time.sleep(2)

    # 스크롤 제어 (동적으로 작성된 페이지)
    interval = 2

    prev_height = browser.execute_script("return document.body.scrollHeight")

    while True:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        time.sleep(interval)

        cur_height = browser.execute_script("return document.body.scrollHeight")

        if cur_height == prev_height:
            break

        prev_height = cur_height

    # 다시 스크롤을 처음으로 움직이기
    # element2 = browser.find_element(
    #     By.XPATH,
    #     "//*[@id='main_pack']/section[2]/div[1]/div/div/div[1]/div[1]/div/div/div/img",
    # )
    # actions = ActionChains(browser)
    # actions.move_to_element(element2).perform()
    browser.execute_script("window.scrollTo(0,0)")
    time.sleep(5)

    # 작은 이미지들 찾아오기
    images = browser.find_elements(By.CSS_SELECTOR, ".mod_vw_thumb.link_thumb img")

    # 이미지 자동으로 다운로드 받기
    count = 1
    for img in images[:10]:
        try:
            img.click()
            time.sleep(2)
            # 큰이미지
            # //*[@id="main_pack"]/section[1]/div/div/div[1]/div[2]/div[1]/img
            # div.viewer_image._fe_image_viewer_main_image img
            # urlretrieve("다운로드 받을 파일 경로","저장 경로")
            img_url = browser.find_element(
                By.CSS_SELECTOR, "div.viewer_image._fe_image_viewer_main_image img"
            ).get_attribute("src")
            print(img_url)

            urlretrieve(img_url, "./crawl/download/" + str(count) + ".jpg")

            count += 1
        except:
            pass

    time.sleep(5)


def set_chrome_driver():
    options = ChromeOptions()
    options.add_argument("--start-maximized")  # 창 띄울때 최대화 해서 띄워준다
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    return driver


# 테스트 실행
if __name__ == "__main__":
    main()
