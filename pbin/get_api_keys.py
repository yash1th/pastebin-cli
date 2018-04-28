import os
import sys

def get_dev_api_key():
    '''
    Gets an API Developer Key from the environment
    Returns:
       Pastebin API Developer Key 
    '''
    try:
        if 'PASTEBIN_DEV_API_KEY' in os.environ:
            return os.environ['PASTEBIN_DEV_API_KEY']
        raise Exception('Please set the environment variable PASTEBIN_DEV_API_KEY with the developer key') 
    except Exception as e:
        print(str(e))
        sys.exit(-1)

def get_user_api_key():
    '''
    Gets an API User Key from the environment
    Returns:
        Pastebin API User Key
    '''
    try:
        if 'PASTEBIN_USER_API_KEY' in os.environ:
            return os.environ['PASTEBIN_USER_API_KEY']
        raise Exception('You are currently not logged into Pastebin')
    except Exception as e:
        print(str(e))
        sys.exit(-2)

def main():
    get_dev_api_key()
    get_user_api_key()

if __name__ == '__main__':
    main()