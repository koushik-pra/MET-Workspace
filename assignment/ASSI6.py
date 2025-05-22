order = {
        "product1": {"name": "massager","price":2500},
        "product2":{ "name": "speakers", "price": 5000}
        }
product_input = input("choose a product : ")

if product_input == "product1":
         print("product:",order["product1"]["name"])
         print("price:",order["product1"]["price"])
elif product_input == "product2":
         print("product:",order["product2"]["name"])
         print("price:",order["product2"]["price"])
else:
    print("product not found.")
