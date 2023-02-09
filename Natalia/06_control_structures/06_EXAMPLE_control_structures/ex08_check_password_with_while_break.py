username = input("Введите имя пользователя: ")
password = input("Введите пароль: ")

while True:
    if len(password) < 8:
        print("Пароль слишком короткий\n")
    elif username in password:
        print("Пароль содержит имя пользователя\n")
    else:
        print("Пароль для пользователя {} установлен".format(username))
        # завершает цикл while
        break
    password = input("Введите пароль еще раз: ")


"""
Example:

Введите имя пользователя: amagkh
Введите пароль: 123
Пароль слишком короткий

Введите пароль еще раз: 1q2w!Q@W
Пароль для пользователя amagkh установлен

Process finished with exit code 0

"""