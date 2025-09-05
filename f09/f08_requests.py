import requests

def main():
    """

    """
    response = requests.get('https://www.naver.com/')
    print(f'response.status_code{response.status_code}') #200 -- OK
    print(f'response.content{response.content}')


if __name__ == '__main__':
    main()
