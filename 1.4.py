
number = input("Введите целое положительное число: ")
if number.isdigit():
    number = int(number)
else:
    print("Ошибка ввода")
    exit()
max_number = 0

while number > 9:
    a = number % 10
    if a >= max_number:
        max_number = a
    number = number // 10

print(max_number)



