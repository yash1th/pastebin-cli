import os
import sys

def get_api_key():
    '''
    Gets an API Key from the environment
    Returns:
       Pastebin API Key 
    '''
    if 'PASTEBIN_API_KEY' in os.environ:
        return os.environ['PASTEBIN_API_KEY']
    print('Please set the key PASTEBIN_API_KEY')
    sys.exit(0)

if __name__ == '__main__':
    get_api_key()
