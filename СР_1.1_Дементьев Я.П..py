def func(num, iter):
    return num * iter


while True:
    try:
        num = float(input("Введите число - "))
        print("Таблица умножения для числа - ", num)
        for _ in range(1, 11):
            print(f"{num} * {_} =", func(num, _))
        break
    except ValueError:
        print("Неправильно введённое число")
