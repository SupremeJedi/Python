print("""
   Chose Operation
    1. Add
    2. Subtract
    3. Multiply
    4. Division
""")
operation = input(">")
num1 = float(input("Enter first no. = "))
num2 = float(input("Enter second no. = "))
while True:
    if operation == "1":
        add = num1 + num2
        print(num1, "+" , num2 , "= " , add )
    elif operation == "2":
        sub = num1 - num2
        print(num1, "-" , num2 , "= " , sub )
    elif operation == "3":
        mupt = num1 * num2
        print(num1, "*" , num2 , "= " , mupt )
    elif operation == "4":
        div = num1 / num2
        print(print(num1, "/" , num2 , "= " , div))
    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation.lower() == "no":
          break
    elif next_calculation.lower() == "yes":
       print("""
   Chose Operation
    1. Add
    2. Subtract
    3. Multiply
    4. Division
    """)
    operation = input(">")
    nu1 = float(input("Enter first no. = "))
    nu2 = float(input("Enter second no. = "))

    if operation == "1":
        add = nu1 + nu2
        print(nu1, "+" , nu2 , "= " , add )
    elif operation == "2":
        sub = nu1 - nu2
        print(nu1, "-" , nu2 , "= " , sub )
    elif operation == "3":
        mupt = nu1 * nu2
        print(nu1, "*" , nu2 , "= " , mupt )
    elif operation == "4":
        div = nu1 / nu2
        print(print(nu1, "/" , nu2 , "= " , div))
    
    else:
        print("Invalid Input")
    break
    





