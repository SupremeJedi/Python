
x = float(input("Enter first no.:"))
y = float(input("Enter second no.:"))
print("""
For:-
    Addition[1]
    Subraction[2]
    Multiplication[3]
    Division[4]
    """)
operation = input("Chose the operation:")

a = lambda x,y : x+y
b = lambda x,y : x-y
c = lambda x,y :x*y
d = lambda x,y : x/y

while True:

    if operation == "1":
        print(x, " + ",y," = ", a(x,y))
        break
    elif operation == "2":
        print(x, " - ",y," = ", b(x,y))
        break
    elif operation == "3":
        print(x, " * ",y," = ", c(x,y))
        break
    elif operation == "4":
        print(x, " / ",y," = ", d(x,y))
        break
    else :
        print("Invalid Output")
        

    


