import os
from dotenv import load_dotenv

def main():
    """
    
    """
    #
    load_dotenv(dotenv_path="../.env")

    CLIENT_ID1 =os.getenv('CLIENT_ID')
    CLIENT_SECRET2 = os.getenv('CLIENT_SECRET')

    print(f'CLIENT_ID: {CLIENT_ID1}')
    print(f'CLIENT_SECRET: {CLIENT_SECRET2}')

if __name__ == '__main__':
    main()
