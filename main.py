# def main():
#     word_list = input("Ввести слова:").split()
#     print("Слова начинающиеся на а:")
#     for word in word_list:
#         if word.lower().startswith('а'):
#             print(word)
#
#
# if __name__ == "__main__":
#     main()
# emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'], 'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'], 'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'], 'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'], 'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'], 'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}
# result = []
# for dom in emails:
#     for mails in emails[dom]:
#         result.append(mails+"@"+dom)
# result.sort()
# print(*result, sep='\n')
# def main():
#     num_list = input("Введите список чисел").split()
#     sum = 0
#     for el in num_list:
#         try:
#             num = float(el)
#             sum += num
#         except ValueError:
#             print("Это не число", el)
#             return
#     print("Сумма чисел", sum)
#
# if __name__ == "__main__":
#     main()
# def func_exce(a, b):
#     return [a+b, a-b, a/b, a*b]
# print(*func_exce(4, 3))
# lst1 = [1, 3, 5, 7, 8, 9, 0, 3, 2, 1]
# lst2 = [1, 3, 5, 7, 8]
# def xz(lst):
#     if len(lst)%2==0: return [lst[len(lst)//2 - 1], lst[len(lst)//2]]
#     if len(lst)%2==1: return [lst[len(lst)//2]]
# print(*xz(lst1))
# print(*xz(lst2))
# from art import *
# def xbI():
#     tprint("VADIK")
# xbI()
# def xbI():
#     for i in range(1, 11):
#         c = "*"*i + "*"*i
#         c = c.center(20)
#         print(c)
# xbI()
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