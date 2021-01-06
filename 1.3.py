"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

while True:
    month = input("Введите номер месяца: ")
    if month.isdigit():
        month = int(month)
        if month <= 12 and month > 0:
            break
        else:
            print("Введенное число больше 12 или меньше 1")
    else:
        print("Ошибка ввода, Введите число")


"""
Dict
"""
dict_month = {
    1: "Январь, Зима",
    2: "Февраль, Зима",
    3: "Март, Весна",
    4: "Апрель, Весна",
    5: "Май, Весна",
    6: "Июнь, Лето",
    7: "Июль, Лето",
    8: "Август, Лето",
    9: "Сентябрь, Осень",
    10: "Октябрь, Осень",
    11: "Ноябрь, Осень",
    12: "Декабрь, Зима",
}

print(dict_month[month])



"""
list
"""
list_month = ["Январь, Зима", "Февраль, Зима", "Март, Весна", "Апрель, Весна",
              "Май, Весна", "Июнь, Лето", "Июль, Лето", "Август, Лето", "Сентябрь, Осень",
              "Октябрь, Осень", "Ноябрь, Осень", "Декабрь, Зима"]

print(list_month[month-1])



