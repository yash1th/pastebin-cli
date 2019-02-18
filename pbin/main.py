from meta_data import *
import requests

def parse_args():
    parser = argparse.ArgumentParser(prog='pbin', description='use pastebin by command line')
    subparsers = parser.add_subparsers()
    parser_create = subparsers.add_parser('create', help='creates a new paste on pastebin')
    parser_login = subparsers.add_parser('login', help='generates a new user key from pastebin')
    parser_list = subparsers.add_parser('list', help='lists your pastes in pastebin')
    parser_trending = subparsers.add_parser('trending', help='lists trending pastes on pastebin')
    parser_delete = subparsers.add_parser('delete', help='deletes an existing paste on pastebin')
    parser_user_info = subparsers.add_parser('user_info', help='displays user information')
    parser_raw_paste = subparsers.add_parser('raw_paste', help='gets raw information of a paste')


def main():
    pass

if __name__ == '__main__':
    main()