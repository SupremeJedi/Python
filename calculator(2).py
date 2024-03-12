def add(x,y):
    return x+y


def sub(x,y):
    return x-y


def mult(x,y):
    return x*y


def div(x,y):
    return x/y


print("""
For:-
    Addition[1]
    Subraction[2]
    Multiplication[3]
    Division[4]
    """)
while True:
    choice = input("Enter (1/2/3/4): ")
    if choice in ("1","2","3","4"):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
        except ZeroDivisionError:
            print("Infinity")
            continue


        if choice == '1':
            print(num1, "+", num2, "=" ,add(num1,num2))
        elif choice == "2":
            print(num1, "-" , num2 , "=",sub(num1,num2))
        elif choice == "3":
            print(num1, "*" , num2 , "=",mult(num1,num2))
        elif choice == "4":
            print(num1, "/" , num2 , "=",div(num1,num2))
        
       


        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
                break
    else:
        print("Invalid Input")



