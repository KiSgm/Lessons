
proceeds = input("Введите выручку предприятия: ")
if proceeds.isdigit():
    proceeds = int(proceeds)
else:
    print("Ошибка ввода")
    exit()
expenses = input("Введите расходы предприятия: ")
if expenses.isdigit():
    expenses = int(expenses)
else:
    print("Ошибка ввода")
    exit()

if proceeds > expenses:
    roi = proceeds / expenses
    print("Предприятие приносит прибыль с рентабельностью =", roi)
    staff = input("Введите колличество сотрудников: ")
    if staff.isdigit():
        staff = int(staff)
    else:
        print("Ошибка ввода")
        exit()
    profit_in_staff = (proceeds - expenses) / staff
    print("прибыль предприятия составила:", profit_in_staff, "на каждого сотрудника")
else:
    lesion = expenses - proceeds
    print("Предприятие в убытке на", lesion)
