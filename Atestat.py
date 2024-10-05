import user_management
import file_handing

def main():
    while True:
        print("1 - регистрация")
        print("2 - авторизация")
        print("3 - обновление данных")
        print("4 - удаление пользователя")
        print("5 - выход")
        choice = int(input("Ваш выбор - "))
        if choice == 1:
            user_management.register_user()
        elif choice == 2:
            user_management.login_user()
        elif choice == 3:
            user_management.update_user()
        elif choice == 4:
            user_management.delete_user()
        elif choice == 5:
            break
        else:
            print("Неверный ввод, попробуйте ещё раз")

if __name__ == "__main__":
    main()