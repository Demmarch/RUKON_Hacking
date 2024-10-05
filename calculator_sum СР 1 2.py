def main():
    num_list = input("Введите список чисел").split()
    sum = 0
    for el in num_list:
        try:
            num = float(el)
            sum += num
        except ValueError:
            print("Это не число", el)
            return
    print("Сумма чисел", sum)

if __name__ == "__main__":
    main()
