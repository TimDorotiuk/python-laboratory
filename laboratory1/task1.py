print('Лабораторна робота №1; Варіант №7.Завдання №1:')
print('Користувач уводить суму вкладу в банк і річний відсоток.\
Знайти суму вкладу через 5 років (розглянути два способи нарахування відсотків.)')
print('Доротюк Т.В. КМ-91')

while True:
    print('Ця програма призначена для розрахунку відсотків по демозитам на 5 років.\
    \nЯкщо ви бажаєте продовжити роботу з програмою, натисніть "Y", а якщо ні - "N"')
    dec_1 = input()
    while dec_1 !="N" and dec_1 !="Y":
        print('Використовуйте для відповіді лише "Y" і "N"')
        del dec_1
        dec_1 = input()
    if dec_1=="Y":
        print('Існує 2 основних способи нарахування відсотків.\
        Перший - вкладчик одразу забирає нарахований від вкладу прибуток.\
        \nДругий спосіб - нараховані відсотки капіталізуються, тобто додаються до вкладу.\
        \nВиберіть той спосіб, який актуальний в вашому випадку. Щоб вибрати перший спосіб, натисніть "F", другий - "L"')
        dec_2 = input()
        while dec_2 !="F" and dec_2 !="L":
            print('Використовуйте для відповіді лише "F" і "L"')
            del dec_2
            dec_2 = input()
        if dec_2=="F":
            try:
                dep_1 = float(input('Введіть початкову суму'))
                per_1 = float(input('Введіть річний відсоток по депозиту'))
            except (ValueError, NameError):
                print('Ви ввели неправильний тип даних. Програма працює лише з числами!')
                continue

            res_1 = dep_1
            print('Через 5 років Ви отримаєте:' + str(res_1) + ' гривень')
        elif dec_2=="L":
            try:
                dep_2 = float(input('Введіть початкову суму'))
                per_2 = float(input('Введіть річний відсоток по депозиту'))
            except (ValueError, NameError):
                print('Ви ввели неправильний тип даних. Програма працює лише з числами!')
                continue
            res_2 = dep_2 / 100 * per_2 + dep_2
            res_2 = res_2 / 100 * per_2 + res_2
            res_2 = res_2 / 100 * per_2 + res_2
            res_2 = res_2 / 100 * per_2 + res_2
            res_2 = res_2 / 100 * per_2 + res_2
            print('Через 5 років Ви отримаєте: ' + str(res_2) + ' гривень')

    elif dec_1=="N":
        print('Роботу з програмою буде завершено. Сподіваємось, Ви повернетесь до неї пізніше')

    to_exit = input("Натисніть A, якщо бажаєте продовжити, або будь-який інший символ для завершення роботи. ")
    if to_exit == "A":
        continue
    else:
        break
print('Роботу з програмою завершено')