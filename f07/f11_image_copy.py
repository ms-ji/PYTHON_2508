def main():
    """
    
    """
    #image.png copy 새로운 new_wave.png
    with open('image.png','rb') as src:
        with open('new_wave.png','wb') as dest:
            dest.write(src.read())


if __name__ == '__main__':
    main()
