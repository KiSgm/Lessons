
first_result = input("Введите результат первого дня тренировки: ")
if first_result.isdigit():
    first_result = float(first_result)
else:
    print("Ошибка ввода")
    exit()

finite_result = input("Введите результат которого вы хотите достичь: ")
if finite_result.isdigit():
    finite_result = float(finite_result)
else:
    print("Ошибка ввода")
    exit()

progress = 1.1
day = 1

while first_result < finite_result:
    print("результат", day, "дня =", first_result)
    first_result = first_result * progress
    day += 1
else:
    print("Спортсмен достигнет своей цели на ", day, "день.")