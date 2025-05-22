categories = {
            "cloths":["shirt","jeans"],
            "electronics":["phone","charger"]
            }

user_input = input("enter category name): ").lower()
if user_input in categories:
    print("products availabe: ",categories[user_input])
else:
    print("invalid category")