import pandas as pd
from kiwipiepy import Kiwi
import requests

# 명사 추출 객체 생성
kiwi = Kiwi()

# csv 파일 읽어오기
df = pd.read_csv('news01.csv',sep=",")
print(df.columns.tolist())

# 명사만 추출하는 함수
def extract_nouns(text):
    if pd.isnull(text):
        return []
    return [token.form for token in kiwi.analyze(text)[0][0] if token.tag.startswith('N')]

# title 열에서 명사 추출
df['nouns'] = df['title'].apply(extract_nouns)
df['nouns'] = df['description'].apply(extract_nouns)

# 결과 확인
print(df[['title', 'nouns']].head())

# 저장하고 싶다면
df.to_csv('명사추출결과.csv', index=False)




