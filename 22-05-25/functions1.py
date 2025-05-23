def add(a,b):
 print("res",a+b)
def sub(a,b):
    print("res",a-b)
def multiply(a,b):
    print("res",a*b)
def divide(a,b):
    if b!=0:
        print("res",a/b)
    else:
        print("cannot divide by zero")

N1=float(input("enter first number: "))
N2=float(input("enter second number: "))
operation = input("enter operation: ")

if operation == "add":
    add(N1,N2)
elif operation == "sub":
    sub(N1,N2)
elif operation == "multiply":
    multiply(N1,N2)
elif operation == "divide":
    divide(N1,N2)
else:
    print("invalid operation")

