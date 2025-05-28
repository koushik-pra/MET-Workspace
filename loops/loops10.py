names=  {'name': 'Alice', 'city': 'New York', 'hobby': 'coding'}
for key in names:
    value = names[key]
    if len(value) > 5:
         print(f"{key}: {value.upper()}")
    else:
            print(f"{key}: {value.lower()}")