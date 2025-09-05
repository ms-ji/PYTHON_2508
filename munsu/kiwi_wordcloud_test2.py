import pandas as pd
from kiwipiepy import Kiwi
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 1. Kiwi 초기화
kiwi = Kiwi()

# 2. CSV 파일 읽기
df = pd.read_csv('news01.csv', encoding='utf-8-sig', sep=",")
print(df.columns.tolist())

# 3. 불용어 설정
stopwords = set(['것', '수', '등', '더', '이', '그', '저', '및', '를', '은', '는', '이', '가'])

# 4. 유사어 통합 매핑 (공백 문제, 띄어쓰기/오타 등)
merge_dict = {
    '재난 ': '재난',
    '기후변화': '기후',
    '폭염': '더위',
    '한파': '추위',
    '산불': '화재',
    '홍수': '침수',
    # 필요하면 더 추가
}

# 4. 명사 추출 함수 (불용어 제외)
def extract_nouns(text):
    if pd.isnull(text):
        return []
    tokens = [token.form for token in kiwi.analyze(text)[0][0] if token.tag.startswith('N')]
    filtered = [merge_dict.get(word, word) for word in tokens if word not in stopwords]
    return [word for word in tokens if word not in stopwords]

# 5. 명사 추출
df['title_nouns'] = df['title'].apply(extract_nouns)
df['description_nouns'] = df['description'].apply(extract_nouns)

# 6. title + description 합치기
df['all_nouns'] = df['title_nouns'] + df['description_nouns']

# 7. 전체 명사 리스트 만들기
all_nouns = sum(df['all_nouns'].tolist(), [])
text = ' '.join(all_nouns)

# 8. 워드클라우드 생성
wordcloud = WordCloud(
    font_path='C:/Windows/Fonts/malgun.ttf',
    background_color='white',
    colormap='autumn',
    prefer_horizontal=True,
    max_words=300,
    width=800,
    height=600
).generate(text)

# 9. 시각화
plt.figure(figsize=(10, 10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
