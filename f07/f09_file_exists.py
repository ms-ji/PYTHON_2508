import os
from pathlib import Path

def main():
    """
    
    """
    if os.path.exists('pcwk.txt'):
        print('파일이 존재합니다.')
    else :
        print('파일이 존재하지 않습니다.')

    file = Path('pcwk.txt')

    if file.is_file():
        print('파일이 존재합니다.')
    else:
        print('파일이 존재하지 않습니다.')

if __name__ == '__main__':
    main()
