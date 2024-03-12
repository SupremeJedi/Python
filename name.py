name = (input("what's your name  "))
if len(name) <3:
    print("Your name is too short.")
elif len(name) >50:
    print("Your name is too long.")
else:
    print(f"{name} is your name.")
