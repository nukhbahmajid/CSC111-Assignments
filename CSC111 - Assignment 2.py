# ------------------------------------------------------
#        Name: <NUKHBAH MAJID AND EMAN BABAR>
#    Filename: CSC111 - Assignment 2.py
#   Description: Clunky Calculator that carries out
#  basic math functions (e.g. multiplication, division
#  addition, subtraction, and exponentiation
#        Date: <09/21/18>
# ------------------------------------------------------

num1 = eval(input("Enter the first number: "))
num2 = eval(input("Enter the second number: "))
operation = input("Enter an operation (+, -, *, /, **, or //): ")
ans = ("The answer is:")
error = "The input is invalid!" 


if (operation == "+" or
operation == "-" or
operation == "*" or
operation == "/" or
operation == "**" or
operation == "//"):
    if (operation == "+"):
        thesum = round((num1 + num2), 3)
        print(ans, thesum)
        
    if (operation == "-"):
        thediff = round((num1 - num2), 3)
        print(ans, thediff)

    if (operation == "/"):
        ratio = round((num1 / num2), 3)
        print(ans, ratio)

    if (operation == "**"):
        exp = round((num1 ** num2), 3)
        print(ans, exp)

    if (operation == "*"):
        product = round((num1 * num2), 3)
        print(ans, product)

    if (operation == "//"):
        intdiv = round(num1 // num2)
        themod = round((num1 % num2), 3)
        if (themod != 0):
            print(ans, intdiv,", remainder is:", themod)
        else:
            print(ans, intdiv)

else:
    print (error)


