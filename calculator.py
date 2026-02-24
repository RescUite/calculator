try:
    a = float(input("первое число: "))
    b = float(input("второе число: "))
except ValueError:(
            print("вводить можно только числа"))
else:
    operation = input("операция (+, -, *, /): ")
    if operation == "+":
        print(a+b)
    elif operation == "-":
        print(a-b)
    elif operation == "*":
        print(a*b)
    elif operation == "/":
        if b == 0:
            print("делить на ноль нельзя")
        else:
            print(a/b)
    else:
        print("неизвестная операция")