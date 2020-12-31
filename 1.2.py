
time_sec = input("Введите колличество секунд ")

if time_sec.isdigit():
    time_sec = int(time_sec)
else:
    print("Ошибка ввода, введите число")
    exit()

time_hour = 0
time_minute = 0

time_minute = int(time_sec) // 60
time_hour = time_minute // 60
time_minute = time_minute % 60
time_sec_remainder = int(time_sec) % 60

time_message = "{} секунд - это {} часов {} минут {} секунд".format(time_sec, time_hour, time_minute, time_sec_remainder)

print(time_message)