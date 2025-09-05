import pandas as pd


def main():
    """

    """
    try:
        df = pd.read_excel('pandas_address.xlsx',engine='openpyxl')
        print(f'df: {df}')
        print(f'읽기 성공 !')

    except FileNotFoundError as e:
        print(f'파일을 찾을 수 없습니다 \n {e}')
    except ValueError as e:
        print(f'파일 읽기 실패 \n {e}')
    except Exception as e:
        print(f'Exception +{e}')

if __name__ == '__main__':
    main()


