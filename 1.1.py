
check_type = [1, "a", 3, 5.14, "aasd"]
print(check_type)

result = {}
for check in check_type:
    result = {check: type(check)}
    print(result)