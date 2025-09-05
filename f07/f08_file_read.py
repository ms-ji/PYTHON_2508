
def main():
    """
    
    """
    with open(file = 'pcwk.txt', mode='w', encoding='utf-8') as f:
        f.write('Hello,World!\n')
        f.write('Python is fun!\n')

    with open(file = 'pcwk.txt', mode='r', encoding='utf-8') as f:
        content = f.read()
        print(content)

    with open(file = 'pcwk.txt', mode='r', encoding='utf-8') as f:
        for line in f :
            print(line)

    # 파일 여러줄 쓰기
    lines=['첫 번쨰 줄\n','두 번쨰 줄\n','세 번쨰 줄\n']
    with open(file = 'multiful.txt', mode='w', encoding='utf-8') as f:
        f.writelines(lines)

    with open(file = 'pcwk.txt', mode='a', encoding='utf-8') as f:
        f.write('이 줄은 추가된 내용입니다.')

if __name__ == '__main__':
    main()
