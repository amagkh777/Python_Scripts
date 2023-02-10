username = input("Введите имя пользователя: ")
password = input("Введите пароль: ")

password_correct = False

while not password_correct:
    if len(password) < 8:
        print("Пароль слишком короткий\n")
    elif username in password:
        print("Пароль содержит имя пользователя\n")
    else:
        print("Пароль для пользователя {} установлен".format(username))
        password_correct = True
        continue
    password = input("Введите пароль еще раз: ")


"""
Example:

Введите имя пользователя: amagkh
Введите пароль: 123
Пароль слишком короткий

Введите пароль еще раз: 1q2w!Q@W
Пароль для пользователя amagkh установлен

"""