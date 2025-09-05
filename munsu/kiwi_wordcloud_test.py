import pandas as pd
from kiwipiepy import Kiwi
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 1. Kiwi 초기화
kiwi = Kiwi()

# 2. CSV 파일 읽기
df = pd.read_csv('news01.csv', encoding='utf-8-sig', sep=",")
print(df.columns.tolist())  # 열 이름 확인

# 3. 명사 추출 함수
def extract_nouns(text):
    if pd.isnull(text):
        return []
    return [token.form for token in kiwi.analyze(text)[0][0] if token.tag.startswith('N')]

# 4. title 열에서 명사 추출
df['title_nouns'] = df['title'].apply(extract_nouns)
df['title_nouns'] = df['description'].apply(extract_nouns)

# 5. 명사 리스트를 하나의 문자열로 합치기
all_nouns = sum(df['title_nouns'].tolist(), [])  # 리스트 안의 리스트 펼치기
text = ' '.join(all_nouns)  # WordCloud 입력용 문자열

## 이미지 파일 읽어오기
# im = Image.open('C:/Users/user/Desktop/heart.png')
# mask_arr = np.array(im) #픽셀 값 배열 형태로 변환

# 6. 워드클라우드 생성 및 시각화
wordcloud = WordCloud(
    font_path='C:/Windows/Fonts/malgun.ttf',  # 한글 폰트 지정 (Windows 기준)
    background_color='white',
    colormap='autumn',
    #mask=mask_arr,
    prefer_horizontal=True,
    max_words=300,
    width=800,
    height=600
).generate(text)




plt.figure(figsize=(10, 10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
