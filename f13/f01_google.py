from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


def main():
    """
    
    """
    #크롬 드라이버 경로
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    # 네이버 로그인
    url =

    # 구글 홈 열기
    driver.get('https://www.google.com/')
    time.sleep(3)

    #구글 검색창에 셀레니움 입력 후 검색 버튼 클릭
    search_box = driver.find_element(By.NAME,'q')
    print(f'search_box: {search_box}')

    search_box.send_keys('셀레니움')
    time.sleep(5)

    search_box.submit()
    time.sleep(2)

if __name__ == '__main__':
    main()
