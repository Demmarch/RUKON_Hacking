try:
    input_file_name = input("Введите имя исходного файла: ")
    with open(input_file_name, "r") as input_file:
        content = input_file.read()
except FileNotFoundError:
    print("Файл", input_file_name, "не найден")
try:
    output_file_name = input("Введите имя файла для копирования: ")
    with open(output_file_name, "w") as output_file:
        output_file.write(content)
        print("Содержимое успешно скопировано в", output_file_name)
except FileNotFoundError:
     print("Файл", output_file_name, "не найден")
except Exception as e:
    print("Ошибка:", e)