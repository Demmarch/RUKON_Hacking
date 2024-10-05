def main():
    word_list = input("Введите список слов").split()
    print("Слова начинающиеся с о")
    for el in word_list:
        if el.lower().startswith('о'):
            print(el)

if __name__ == "__main__":
    main()