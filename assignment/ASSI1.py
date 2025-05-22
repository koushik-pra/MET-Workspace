#assignment 1
cart = [{"id":1, "name":"shirt","qty":1}]
product_id = int(input("enter product id: "))
product_name = input("enter product name: ")
HOLO = {'id':product_id , 'name':product_name}
print(HOLO)

if product_id in cart:
    print("it already present in cart")
else:
    cart.append(HOLO)
print(cart)
