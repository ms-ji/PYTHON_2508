import requests
from bs4 import BeautifulSoup

def bs4_ex():
    htmlDoc = """
            <html>
            <head>
            <title>My First Webpage</title>
            </head>
            <body>
            <h1>Welcome to My Webpage</h1>
            <p class="description">This is a simple webpage.</p>
            <ul id="fruits">
              <li class="apple">Apple</li>
              <li class="banana">Banana</li>
              <li class="orange">Orange</li>
            </ul>
            </body>
            </html>
         """
    bs = BeautifulSoup(htmlDoc, 'html.parser')
    #단 건 조회 : <li class="apple">Apple</li>
    apple_text = bs.select_one('li.apple').text
    print(f'apple_text: {apple_text}')
    # apple_text: Apple

    #목록 조회 : <ul id="fruits"> 자식 태그
    for li in bs.select('ul#fruits li'):
        print(li.text)

    #<p class="description">This is a simple webpage.</p>
    print(bs.find('p').text)

    #속성<p class="description">
    print(bs.p['class']) #['description']


def main():
    """
    
    """
    bs4_ex()



if __name__ == '__main__':
    main()
