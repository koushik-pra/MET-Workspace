#you are creating a simple program for 'VENTEX HOTEL'
#they serve INDIAN DISHES - IDLY< DOSA, VSDA, UPMA, POORI, WITH res. prices
#every cumstomer buys three items of any count
#print final bill
menu = {
    'energy drink': 50,
    'mazza': 30,
    'nestle coffee': 100,
    'cocoa shake': 70,
    'water': 20,
    'redbull': 95,
    'white monster': 110,
}
bill = 0

user_input1 = input("choose an drink: ")
if user_input1 in menu:
    no_of_items = int(input('enter number of items: '))
    bill += no_of_items * menu[user_input1]
else:
    print("Sorry, we don't have that drink")

user_input2 = input("choose an drink: ")
if user_input2 in menu:
    no_of_items = int(input('enter number of items: '))
    bill += no_of_items * menu[user_input2]
else:
    print("Sorry, we don't have that item")

user_input3 = input("choose an item: ")
if user_input3 in menu:
    no_of_items = int(input('enter number of items: '))
    bill += no_of_items * menu[user_input3]
else:
    print("Sorry, we don't have that item")

user_input4 = input("choose an item: ")
if user_input4 in menu:
    no_of_items = int(input('enter number of items: '))
    bill += no_of_items * menu[user_input4]
else:
    print("Sorry, we don't have that item")

print('your total bill is : ', bill)