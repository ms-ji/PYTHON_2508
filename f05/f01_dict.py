def main():
    """
    딕셔너리(Dictionary)는 키(key)와 값(value)의 쌍으로 데이터를 저장하는 자료형 입니다.

    딕셔너리(Dictionary)는 데이터를 효율적으로 검색, 수정, 추가, 삭제할 수 있는 구조를 제공합니다.
    """

    empty_dict = {}
    print(f'empty_dict: {empty_dict}') #{}

    person = {"name":'Alice',"age":25,"city":'seoul'}
    print(f'person: {person}') #{'name': 'Alice', 'age': 25, 'city': 'seoul'}
    print(type(person)) #<class 'dict'>

    new_person = dict(name='이상무',age=21,city='Busan')
    print(f'new_person: {new_person}')

    pairs ={('name','영희'):('age','22')}
    print(type(pairs))
    print(f'pairs: {pairs}')



if __name__ == '__main__':
    main()
