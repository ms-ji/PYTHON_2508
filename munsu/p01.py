from kiwipiepy import Kiwi
import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

# 명사 추출
kiwi = Kiwi()

text = "카카오워크를 효과적으로 사용하려면"
result = kiwi.tokenize(text)

word_list = []

for token in result:
    if (token.tag).startswith('N'):
        word_list.append([token.form, token.tag])
print(word_list)

