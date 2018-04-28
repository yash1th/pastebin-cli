import requests
import os
import sys
from get_api_keys import get_dev_api_key, get_user_api_key

LOGIN_URL = 'https://pastebin.com/api/api_login.php'

def login():
    '''
    To login into pastebin.com
    Args:
        username: username on pastebin.com
        password: password on pastebin.com
    '''
    username = input('Enter your username : ').strip().lower()
    password = input('Enter your password : ').strip().lower()
    data = {
        'api_dev_key' : get_dev_api_key(),
        'api_user_name' : username,
        'api_user_password' : password,
    }
    try:
        response = requests.post(LOGIN_URL, data)
        print('Attempting to Log in ....')
        user_api_key = response.content.decode('utf-8')
        if len(user_api_key) != 32:
            print('reached invalid creds exception')
            raise Exception('Invalid credentials, Try again')
        print('Successfully Logged In')
        if 'PASTEBIN_USER_API_KEY' in os.environ:
            raise Exception('There is already a key named PASTEBIN_USER_API_KEY, you can overwrite that value with "{0}" for the current pastebin user for further use'.format(user_api_key))
        else:
            print('New User API Key --- ',user_api_key)
            print('please create an environment variable PASTEBIN_USER_API_KEY="{}" in your system if you want further use of this user'.format(user_api_key))
            return user_api_key
    except Exception as e:
        print(str(e))
        sys.exit(-3)

if __name__ == '__main__':
    login('randomUsername', 'randomPassword')
