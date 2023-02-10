
ip_list = ["10.1.1.1", "10.2.2.2", "10.3.3.3"]
for ip in ip_list:
    print(f"Подключились на {ip}")
    try:
        if ip == "10.1.1.1":
            raise ValueError("При подключении возникла ошибка")
    except ValueError as error:
        print(f"Timeout при подключении к {ip}")
        print(error)


"""
Example:

Подключились на 10.1.1.1
Timeout при подключении к 10.1.1.1
При подключении возникла ошибка
Подключились на 10.2.2.2
Подключились на 10.3.3.3

"""