# -*- coding: utf-8 -*-

username = input("Введите имя пользователя: ")
password = input("Введите пароль: ")

if len(password) < 8:
    print("Пароль слишком короткий")
elif username in password:
    print("Пароль содержит имя пользователя")
else:
    print("Пароль для пользователя {} установлен".format(username))


"""
Example:

Введите имя пользователя: amagkh
Введите пароль: 1q2w!Q@W
Пароль для пользователя amagkh установлен
########################################

"""