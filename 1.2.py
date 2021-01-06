
new_list = list(input("Введите список для форматирования: "))
print(new_list)
for elem in range(1, len(new_list), 2):
    new_list[elem - 1], new_list[elem] = new_list[elem], new_list[elem - 1]

print(new_list)