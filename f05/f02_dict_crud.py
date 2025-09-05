def main():
    """
    
    """
    person = {'name':' 영희','age':25}
    pairs = {('name', '영희'): ('age', '22')}

    # 값 접근
    print(person['name'])
    print(pairs[('name', '영희')]) #('age', '22')

    # 함수로 값 접근(안전한 접근)
    print(person.get('name'))
    print("#" * 54)

    # 값 추가
    person['city']='Seoul'
    print(person) #{'name': ' 영희', 'age': 25, 'city': 'Seoul'}

    # 리스트로 value 추가 가능
    person['item']=[1,2,3]

    # 값 수정
    person['age']=20
    print(person) #{'name': ' 영희', 'age': 20, 'city': 'Seoul'}

    # 값 삭제
    del person['city']
    print(person) #{'name': ' 영희', 'age': 20}

    # pop사용
    age = person.pop('age')
    print(age) #20
    print(person) #{'name': ' 영희'}

    # 전체 삭제
    person.clear()
    print(person) # {}


if __name__ == '__main__':
    main()
