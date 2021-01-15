str_input = input("Введите любую строку из нескольких слов: ")
count = 1
for word in str_input.split():
    if len(word) > 10:
        word = word[:10] + "..."
    print(f'{count} {word}')
    count += 1
