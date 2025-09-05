import requests
from bs4 import BeautifulSoup

def google_crawling():
    url = 'https://www.google.com/'
    responce = requests.get(url)
    #print(responce.status_code) #200 -- OK

    if responce.status_code == 200:
        print(f'접속 성공: {responce.status_code}')
        print(f'responce.text: {responce.text}')
    else:
        print(f'접속 실패: {responce.status_code}')

def main():
    """
    
    """
    google_crawling()


if __name__ == '__main__':
    main()
