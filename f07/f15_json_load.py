import json

def main():
    """
    ## JSON 데이터 읽기(Read from JSON)
    :  json.load()
    """
    with open('data.json','r',encoding='utf-8') as f:
        load_data = json.load(f)
        print(f'load_data: {load_data}, type: {type(load_data)}')
        # type<class 'dict'>

        print(f'load_data[\'name\'] : {load_data['name']}')
        print(f'load_data[\'age\'] : {load_data['age']}')
        print(f'load_data[\'languages\'] : {load_data['languages']}')

if __name__ == '__main__':
    main()
