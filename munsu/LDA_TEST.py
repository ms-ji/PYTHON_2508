import pandas as pd
from kiwipiepy import Kiwi
from gensim import corpora
from gensim.models import LdaModel

# 1. KIWI 초기화
kiwi = Kiwi()

# 2. 데이터 불러오기
df = pd.read_csv('news01.csv', encoding='utf-8-sig')

# 3. 불용어 & 유사어 설정
stopwords = set(['것', '수', '등', '더', '이', '그', '저', '및', '를', '은', '는', '이', '가'])

merge_dict = {
    '재난 ': '재난'
}

# 4. 명사 추출 함수
def extract_nouns(text):
    if pd.isnull(text):
        return []
    tokens = [token.form.strip() for token in kiwi.analyze(text)[0][0] if token.tag.startswith('N')]
    return [merge_dict.get(word, word) for word in tokens if word not in stopwords]

# 5. 명사 추출
df['title_nouns'] = df['title'].apply(extract_nouns)
df['description_nouns'] = df['description'].apply(extract_nouns)
df['all_nouns'] = df['title_nouns'] + df['description_nouns']

# LDA를 위한 입력 형식 준비
texts = df['all_nouns'].tolist()  # 각 문서의 명사 리스트
dictionary = corpora.Dictionary(texts)  # 단어 사전
corpus = [dictionary.doc2bow(text) for text in texts]  # 문서-단어 행렬 (bow)

# LDA 모델 학습
lda_model = LdaModel(
    corpus=corpus,
    id2word=dictionary,
    num_topics=3,  # 토픽 개수 조절 가능
    random_state=42,
    passes=10,
    iterations=100
)

# 토픽 출력
print("\n[LDA 토픽 결과]")
for idx, topic in lda_model.print_topics(num_words=5):
    print(f"토픽 {idx + 1}: {topic}")
