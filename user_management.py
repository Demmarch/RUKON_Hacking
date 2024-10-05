import file_handing

def register_user():
    name = input("Введите ваше имя: ")
    surname = input("Введите вашу фамилию: ")
    email = input("Введите вашу почту: ")
    password = input("Введите пароль: ")

    data = file_handing.read_data_from_file()
    existing_emails = [user["email"] for user in data]
    if email in existing_emails:
        print("Пользователь с такой почтой уже есть")
    else:
        user = {"name": name, "surname": surname, "email": email, "password": password}
        data.append(user)
        file_handing.write_data_to_file(data)
        print("Регистрация прошла успешна")

def login_user():
    email = input("Введите вашу почту: ")
    password = input("Введите пароль: ")

    data = file_handing.read_data_from_file()
    for user in data:
        if user["email"] == email and user["password"] == password:
            print("Авторизация прошла успешно")
            print("желаете просмотреть остальных пользователей (Y - да N - нет)?")
            choice = input("Ваш выбор - ")
            if choice == "Y":
                for data_user in data:
                    print("Имя -", data_user["name"])
                    print("Фамилия -", data_user["surname"])
                    print("Почта -", data_user["email"])
                    print(f"\n")
            return
    print("Неправльный пароль или почта")

def update_user():
    email = input("Введите вашу почту: ")
    password = input("Введите пароль: ")
    data = file_handing.read_data_from_file()
    for user in data:
        if user["email"] == email and user["password"] == password:
            user["name"] = input("Введите ваше имя: ")
            user["surname"] = input("Введите вашу фамилию: ")
            user["email"] = input("Введите вашу почту: ")
            user["password"] = input("Введите пароль: ")
            file_handing.write_data_to_file(data)
            print("Данные успешно изменены")
            return
    print("Неправильная почта или пароль")

def delete_user():
    email = input("Введите вашу почту: ")
    password = input("Введите пароль: ")
    data = file_handing.read_data_from_file()
    for user in data:
        if user["email"] == email and user["password"] == password:
            data.remove(user)
            file_handing.write_data_to_file(data)
            print("Пользователь удалён")
            return
    print("Неправльный пароль или почта")