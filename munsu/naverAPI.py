import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

# 네이버 API 키
client_id = "xLaZJaqshbjNp2fzcltj"
client_secret = "EIZG52R2R_"

# 검색어
query = "재난"

# 요청 URL (뉴스 검색)
url = "https://openapi.naver.com/v1/search/news.json"

# 요청 헤더 설정
headers = {
    "X-Naver-Client-Id": client_id,
    "X-Naver-Client-Secret": client_secret
}

# 요청 파라미터
params = {
    "query": query,
    "display": 10,  # 결과 5개만
    "start": 1,
    "sort": "date"  # 정확도순 , data : 날짜순 내림차순
}

# GET 요청
response = requests.get(url, headers=headers, params=params)

# 결과 저장용 리스트
results = []


# 결과 처리
if response.status_code == 200:
    news_data = response.json()
    for item in news_data['items']:
        title = re.sub(r'<.*?>', '', item['title'])  # HTML 태그 제거
        desc = re.sub(r'<.*?>', '', item['description'])
        link = item['link']

        combined_text = title + desc

        # if any(word in combined_text.lower() for word in exclude_keywords):
        #     continue

        results.append({
            "title": title,

            "link": link
        })

        print("제목:", title)
        print("내용:", desc)
else:
    print(response.status_code,response.text)

# 데이터 저장
df = pd.DataFrame(results)
df.to_csv("news01.csv", index=False, encoding="utf-8-sig")
