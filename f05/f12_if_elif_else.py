from wordcloud.tokenization import score


def main():
    """
    
    """
    age = 17

    if age >= 18:
        print("성인 입니다.")
    else:
        print("성인이 아닙니다.")
    ####################################

    score = 80

    if score >=90:
        print('A')
    elif score >=80:
        print('B')
    elif score >=70:
        print('C')
    else:
        print('D')

    age = 20
    is_student = True

    if age >= 18:
        #pass
        if is_student:
            print("성인이면서 학생 입니다.")
        else:
            print("성인이면서 학생 아닙니다.")
    else:
        print('미성년자')



if __name__ == '__main__':
    main()
