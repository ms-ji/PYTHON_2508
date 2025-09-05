
def main():
    """
    문자열(String Methods)은 다양한 내장 메서드를 제공하며, 문자열을 쉽게 다룰 수 있도록 합니다.
    이 메서드들을 사용하여 문자열을 변경, 검색, 변환, 분리, 합치는 등 다양한 작업을 할 수 있습니다.
    """

    my_string ='Hello, python'
    print(f'str_string: {my_string}')

    str_string = len(my_string)
    print(f'str_string: {str_string}')
    print('#'*53)

    #strip() 양 옆의 공백 제거
    padded_text = ' Hello, Python! '
    print(f'padded_text:{padded_text}')
    print(f'strip :{padded_text.strip()}')
    print('#' * 53)

    #replace() 특정 문자열을 다른 문자열로 교체
    org_text = 'Hello, Python!'
    print(f"org_text:{org_text}")

    replace_text = org_text.replace('Python','World')
    print(f"replace_text:{replace_text}")
    print('#' * 53)

    sentence = "오늘은 즐거운 목요일 4일전 입니다."

    words =  sentence.split()
    print(f"words:{words},{type(words)}") #<class 'list'>
    print('#' * 53)

    #find() 부분 문자열의 시작 인덱스를 반환
    full_text = "f01_string.py"

    index = full_text.find(".")
    print(f"index:{index}")

    endswith_index = full_text.endswith("py") #True/False 반환
    print(f"endswith_index:{endswith_index}")


if __name__ == '__main__':
    main()
