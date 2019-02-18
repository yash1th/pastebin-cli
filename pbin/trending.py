from get_api_keys import get_dev_api_key
import requests
from xml.etree import ElementTree as ET
import re



def get_trending():
    '''
    '''
    URL = 'https://pastebin.com/api/api_post.php'
    data = {
        'api_dev_key' : get_dev_api_key(),
        'api_option' : 'trends',
    }
    response = requests.post(URL, data)
    tree = '<root>\r\n' + response.text + '</root>'
    xmlData = ET.fromstring(tree)
    
    import colorama
    from colorama import init, Fore
    init()
    print('\033[31m'+ 'hits         title               url(pastebin.com/)')
    print('\033[37m')
    for paste in xmlData.iter('paste'):
        #for child in paste:
        print('{} {} {}'.format(paste.find('paste_hits').text.ljust(8), str(paste.find('paste_title').text).ljust(8), paste.find('paste_key').text.ljust(8)))


if __name__ == '__main__':
    get_trending()
