# 사용자 정의 예외
class NegativeNumberError(Exception): # Exception 상속
    pass

def check_positive(num):
    if num < 0:
        raise NegativeNumberError('음수는 허용 되지 않습니다.')

    print(f'입력 숫자:{num}')
try:
    check_positive(-5)
except NegativeNumberError as e:
    print(f'NegativeNumberError{e}')