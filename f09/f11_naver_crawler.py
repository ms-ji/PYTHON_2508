import requests
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError

def news_crawler():
    url = 'https://news.naver.com/section/105'

    
    try:
        responce = requests.get(url)
        if responce.status_code ==200:
            print(f'접속 성공: {responce.status_code}')
            #print(responce.text)
    
            bs = BeautifulSoup(responce.text, 'html.parser')
            #제목 조회
            news_title = bs.select('strong.sa_text_strong')

            for title in news_title:
                print(title.text)
            print(f'len(news_title):{len(news_title)}')
            #뉴스 상세 링크
            news_links = bs.select('div.sa_text a.sa_text_title')
            print(f'len(news_links):{len(news_links)}')

            for link in news_links:
                print(f'link:href:{link['href']}')

        else:
            print(f'접속 실패: {responce.status_code}')

    except ConnectionError as e:
        print('-'*80)
        print(f'ConnectionError: {e}')
        print('-' * 80)
    else:
        print('*' * 80)
        print(f'정상 종료')
        print('*' * 80)
    finally:
        print('*' * 80)
        print(f'항상 수행')
        print('*' * 80)

def main():
    """
    
    """
    news_crawler()


if __name__ == '__main__':
    main()
