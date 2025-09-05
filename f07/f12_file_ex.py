def main():
    """
    
    """
    file_name = 'user_input.txt'
    while True:
        user_input = input('내용을 입력하세요!(exit:종료)> ')
        if user_input.lower() == 'exit':
            print('프로그램을 종료 합니다.')
            break
        else:
            print(user_input)

            with open(file_name, mode='a', encoding='utf-8') as f:
                f.write(user_input+'\n')


if __name__ == '__main__':
    main()
