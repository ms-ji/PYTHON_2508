def main():
    """
    
    """
    score = {"이상무":85,"영희":92,"철수":78,"바둑이":95}
    p_high_score = {name:score for name,score in score.items() if score >=90}
    print(f'p_high_score:{p_high_score}') #{'영희': 92, '바둑이': 95}


if __name__ == '__main__':
    main()
