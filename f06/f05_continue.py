def main():
    """
    
    """
    for i in range(1,11):
        if i % 2 == 0:
            continue
        print(f'i:{i}',end=",") #i:1,i:3,i:5,i:7,i:9,
    print("\t")

    comments = ["좋아요!", "별로에요", "최고예요", "싫어요", "좋았어요"]

    for word in comments:
        if "좋" not in word:
            continue
        print(word)
    # 좋아요!
    # 좋았어요

if __name__ == '__main__':
    main()
