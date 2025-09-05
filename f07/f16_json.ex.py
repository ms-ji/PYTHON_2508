import json

from numpy.f2py.crackfortran import endifs


def main():
    """
    
    """
    users = [
        {"id": 1, 'name': '이상무', 'age': 22, 'email': 'mmm@gmail.com'},
        {"id": 2, 'name': '홍당무', 'age': 20, 'email': 'mmm@gmail.com'},
        {"id": 3, 'name': '영희', 'age': 28, 'email': 'mmm@gmail.com'}
    ]

    print(f'type: {type(users)}')

    with open('user.json','w',encoding='utf-8') as f:
        json.dump(users, f, ensure_ascii=False, indent=4)






if __name__ == '__main__':
    main()
