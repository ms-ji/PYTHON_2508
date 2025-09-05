import pandas as pd


def main():
    """
    
    """
    #데이터 프레임
    data = {
        "이름":['영희','철수','기훈'],
        "나이":[22,31,45],
        "점수":[75,78,95]
    }
    #엑셀 파일에 저장
    df = pd.DataFrame(data)
    df.to_excel('pandas_address.xlsx',index=False,engine='openpyxl')
    
    print(f'pandas_address.xlsx 생성 완료')

if __name__ == '__main__':
    main()
