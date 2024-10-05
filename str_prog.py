import str_opers

def main():
    user_input = input("Введите строку: ")
    print("Выберите операцию:")
    print("1. Подсчет количества символов")
    print("2. Поиск подстроки")
    print("3. Замена символов")
    choice = input("Введите номер операции: ")
    if choice == '1':
        count = str_opers.count_characters(user_input)
        print(f"Количество символов: {count}")
    elif choice == '2':
        substring = input("Введите подстроку для поиска: ")
        result = str_opers.find_substring(user_input, substring)
        print(result)
    elif choice == '3':
        old_char = input("Введите символ для замены: ")
        new_char = input("Введите новый символ: ")
        new_text = str_opers.replace_characters(user_input, old_char, new_char)
        print("Новая строка:", new_text)
    else:
        print("Некорректный номер операции")
if __name__ == "__main__":
    main()