
persons_name = "Илья"
persons_age = 32

print("Привет, меня зовут", persons_name, "мне ", persons_age, "года")

users_name = input("Введите своё имя ")
users_age = input("Введите свой возраст ")

if users_age.isdigit():
    users_age = int(users_age)
else:
    print("Ошибка ввода возраста")
    exit()

print("Привет, ", users_name, "тебе ", users_age, "лет")