import os
import sys
import schedule
import time


import urllib.parse
import urllib.request

import json
from re import search


def json_naver_new():
    print(f'json_naver_new')

    client_id = 'xLaZJaqshbjNp2fzcltj'
    client_secret = 'EIZG52R2R_'

    try:
        # 검색어
        search_word = input('검색어를 입력 하세요>')
        print(f'search_word: {search_word}')
        search_word = urllib.parse.quote(search_word, encoding='utf-8')
        print(f'url인코딩:{search_word}')

        url = 'https://openapi.naver.com/v1/search/news.json?query=' + search_word

        print(f'url:{url}')

        requests = urllib.request.Request(url)

        requests.add_header("X-Naver-Client-Id", client_id)
        requests.add_header("X-Naver-Client-Secret", client_secret)

        # 요청
        response = urllib.request.urlopen(requests)
        print(f'response.getcode: {response.getcode()}')
        if 200 == response.getcode():
            responseBody = response.read().decode('utf-8')
            print(f'responseBody: {responseBody}')
            data = responseBody
        else:
            print(f'접속 실패')
            data = None

        if data:
            jsonObject = json.loads(data)
            print(jsonObject)

            for item in jsonObject.get('items'):
                print(f'item[title]:{item['title']} \t {item['description']}')

        else:
            print('data가 없습니다.')


    except ConnectionError as e:
        print("*" * 80)
        print(f'ConnectionError:{e}')
        print("*" * 80)
    else:
        print("*" * 80)
        print(f'정상 종료')
        print("*" * 80)
    finally:
        print(f'finally___')


def main():
    """

    """

    # print(f'data:{type(data)}') #data:<class 'NoneType'>
    # jsonObject = json.loads(data)
    #
    # print(f'jsonObject: {jsonObject}')
    schedule.every().day.at('12:26').do(json_naver_new)
    # 루프를 돌리면서 작업 실행 여부 확인
    while True:
        schedule.run_pending()
        time.sleep(1)  # 1초 마다 확인
if __name__ == '__main__':
    main()
