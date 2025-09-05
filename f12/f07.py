import random
import schedule
import time

def lotto():
    print(f'lotto')

    result = []

    while len(result) < 6:
        num = random.randint(1,45)
        if num not in result: # 중복 숫자 방지
            result.append(num)
    print(f'result: {result}')
    result.sort()
    print(f'result aes: {result}')

def main():
    """
    
    """
    schedule.every(1).minutes.do(lotto)
    while True:
        schedule.run_pending()
        time.sleep(1)  # 1초 마다 확인

if __name__ == '__main__':
    main()
