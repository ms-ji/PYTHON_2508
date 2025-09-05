import re

def main():
    """
    
    """
    #527.협동조합[cooperative]

    text ='''
				527.
				협동조합
					[cooperative]
    '''
    text2 ='''
    로 인한 손익 변동을 쉽게 분석할 수 있다.\n
    '''
    # 한글만, 숫자
    # 한글 : 가-힣
    # 숫자 : 0-9
    # 영문자 : A-Z , (소문자) a-z
    # 대괄호 : \[,\]
    # . : .
    #[^가-힣0-9.a-zA-Z\[\]] 가 아닌 문자 전부 제외

    cleaned = re.sub(r'[^가-힣0-9.a-zA-Z\[\]]','',text)  #527.협동조합[cooperative]

    cleaned2 = re.sub(r'[\\n]', '', text2)  # 527.협동조합[cooperative]
    print(cleaned2)

if __name__ == '__main__':
    main()
