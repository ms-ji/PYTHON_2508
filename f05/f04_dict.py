def main():
    """
    
    """
    text = "apple banana apple orange banana apple"

    word_count = {}
    new_text = text.split()
    print(text.split())

    j = 0
    for i in new_text:
        word_count[i] = word_count.get(i,0)+1
    print(word_count)



if __name__ == '__main__':
    main()
