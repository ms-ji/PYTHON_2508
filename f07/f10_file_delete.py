import os

def main():
    """
    
    """

    if os.path.exists('pcwk.txt'):
        os.remove('pcwk.txt')
        print('파일이 삭제 되었습니다.')
    else:
        print('삭제할 파일이 없습니다.')


if __name__ == '__main__':
    main()
