from sys import excepthook


def main():
    """
    
    """
    try:
        with open('파일없음.txt','r') as f:
            content=f.read()
    except FileNotFoundError as e:
        print(f'파일이 존재하지 않습니다\n{e}')



if __name__ == '__main__':
    main()
