def main():
    """
    and	두 조건이 모두 참일 때 참	(5 > 3) and (2 < 4)	TRUE
    or	둘 중 하나라도 참이면 참	(5 > 3) or (2 > 4)	TRUE
    not	조건의 반대값 (부정)	not(5 > 3)	FALSE
    """
    print(f'(5 > 3) and (2 < 4):{(5 > 3) and (2 < 4)}') # True
    print(f'(5 > 3) or (2 > 4):{(5 > 3) or (2 > 4)}') # True
    print(f'not(5 > 3):{not(5 > 3)}') # False

if __name__ == '__main__':
    main()
