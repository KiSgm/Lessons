
number = input("Введите число: ")
if number.isdigit():
    print("Вычисляем сумму:")
else:
    print("Ошибка ввода")
    exit()
sum1 = number + number
sum2 = number + number + number
sum3 = int(number) + int(sum1) + int(sum2)


print(number, "+", sum1, "+", sum2, "=", sum3)