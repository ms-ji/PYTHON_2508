import json
def main():
    """
    
    """
    with open('user.json', 'r', encoding='utf-8') as f:
        load_data = json.load(f)
        print(f'load_data: {load_data}, type: {type(load_data)}')

        for user in load_data:
            print(f"{user['id']}  {user['name']}  {user['age']}  {user['email']}")


    load_data.append({"id": 4, 'name': '철수', 'age': 23, 'email': 'mmm@gmail.com'})

    with open('user2.json', 'w', encoding='utf-8') as f:
        json.dump(load_data, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    main()
