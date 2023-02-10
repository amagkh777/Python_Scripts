# -*- coding: utf-8 -*-
from pprint import pprint


def select_correct_passwd(check_data,min_passwd_len=8,spec_sym="@$#%&^"):
    correct_password = []
    incorrect_password = []

    for data in check_data:
        username, password = data
        if len(password) < min_passwd_len:
            incorrect_password.append([username, password])
        elif username.lower() in password.lower():
            incorrect_password.append([username, password])
        elif spec_sym and not set(spec_sym) & set(password):
            incorrect_password.append([username, password])
        else:
            correct_password.append([username, password])
    return correct_password, incorrect_password


data_to_check = [
    ["user10", "sdldfj"],
    ["user20", "sdf####klfdj"],
    ["user30", "ssdkfjsus#%er3df"],
]
yes, no = select_correct_passwd(data_to_check)
pprint(yes)
pprint(no)
"""
Example:

[['user20', 'sdf####klfdj'], ['user30', 'ssdkfjsus#%er3df']]
[['user10', 'sdldfj']]

"""
