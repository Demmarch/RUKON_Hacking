try:
    with open("Дата/data.txt", "r", encoding="utf-8") as file_original:
        org_content = file_original.readlines()
        with open("Дата/new_data.txt", "w", encoding="utf-8") as file_new:
            for new in org_content:
                file_new.write(new[::-1])
        file_new.close()
        with open("Дата/new_data.txt", "r", encoding="utf-8") as file_new:
            for text in file_new.readlines()[1:]:
                print(text[:len(text)-1:])
finally:
    file_original.close()
