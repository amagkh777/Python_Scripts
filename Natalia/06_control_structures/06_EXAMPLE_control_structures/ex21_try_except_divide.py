# Вариант с try/except
while True:
    a = input("Введите число: ")
    b = input("Введите второе число: ")
    try:
        result = int(a) / int(b)
    except ValueError:
        print("Поддерживаются только числа")
    except ZeroDivisionError:
        print("На ноль делить нельзя")
    else:
        print(result)
        break

# Аналогичное решение без try/except
while True:
    a = input("Введите число: ")
    b = input("Введите второе число: ")
    if a.isdigit() and b.isdigit():
        if int(b) == 0:
            print("На ноль делить нельзя")
        else:
            print(int(a) / int(b))
            break
    else:
        print("Поддерживаются только числа")

"""
Example:

Введите число: 23
Введите второе число: fgfg
Поддерживаются только числа
Введите число: 12
Введите второе число: 6
2.0
Введите число: 

"""
