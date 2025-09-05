import json

# 딕셔너리 생성
data = {
    'name':'이상무',
    'age':22,
    'languages':['Java','Python','Oracle']

}
print(f'data: {data},type: {type(data)}')
#data: {'name': '이상무', 'age': 22, 'languages': ['Java', 'Python', 'Oracle']},type: <class 'dict'>

with open('data.json','w',encoding='utf-8') as f :
    json.dump(data,f,ensure_ascii=False,indent=4)

print(f'data.json 파일 생성 !')