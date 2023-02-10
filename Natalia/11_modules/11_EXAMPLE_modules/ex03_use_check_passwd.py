"""
Функции для подключения к оборудованию

"""
from pprint import pprint
from ex01_check_passwd import check_passwd
import sys


def printprefix():
    print(sys.prefix)


def select_correct_passwd(check_data, **kwargs):
    """
    ...
    """
    correct_password = []
    incorrect_password = []

    for user, passwd in check_data:
        # распаковка словаря в ключевые аргументы
        check = check_passwd(user, password=passwd, **kwargs)
        if check:
            correct_password.append([user, passwd])
        else:
            incorrect_password.append([user, passwd])
    pprint(locals())
    return correct_password, incorrect_password


data = [
    ["user10", "sdldfj"],
    ["user20", "sdf####klfdj"],
    ["user30", "ssdkfjsus#%er3df"],
]

if __name__ == "__main__":
    yes, no = select_correct_passwd(data, spec_sym="@#$", numbers=True)
    pprint(yes)
    pprint(no)

"""
Example:

{'check': True,
 'check_data': [['user10', 'sdldfj'],
                ['user20', 'sdf####klfdj'],
                ['user30', 'ssdkfjsus#%er3df']],
 'correct_password': [['user30', 'ssdkfjsus#%er3df']],
 'incorrect_password': [['user10', 'sdldfj'], ['user20', 'sdf####klfdj']],
 'kwargs': {'numbers': True, 'spec_sym': '@#$'},
 'passwd': 'ssdkfjsus#%er3df',
 'user': 'user30'}
[['user30', 'ssdkfjsus#%er3df']]
[['user10', 'sdldfj'], ['user20', 'sdf####klfdj']]

"""

